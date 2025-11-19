#!/usr/bin/env python3
"""Environment verification script for RAG system.

Checks:
- Python version
- Required environment variables
- Ollama endpoint reachability
- Required Python packages
- Index artifacts presence
- Disk space

Usage:
    python scripts/verify_env.py
    python scripts/verify_env.py --strict  # Exit with error on warnings
"""

import argparse
import os
import sys
from pathlib import Path


def check_python_version() -> tuple[bool, str]:
    """Check Python version is 3.8+."""
    version = sys.version_info
    if version.major == 3 and version.minor >= 8:
        return True, f"Python {version.major}.{version.minor}.{version.micro}"
    return False, f"Python {version.major}.{version.minor} (need 3.8+)"


def check_env_vars() -> tuple[bool, list[str]]:
    """Check critical environment variables."""
    required = []
    warnings = []

    # Check if ENVIRONMENT is set for production
    env_type = os.getenv("ENVIRONMENT", os.getenv("APP_ENV", "dev"))
    if env_type in ("prod", "production", "ci"):
        warnings.append(f"ENVIRONMENT={env_type} (production mode)")
    else:
        warnings.append(f"ENVIRONMENT={env_type} (development mode)")

    # Check Ollama URL
    ollama_url = os.getenv("RAG_OLLAMA_URL", os.getenv("OLLAMA_URL"))
    if not ollama_url:
        warnings.append("RAG_OLLAMA_URL not set (will use default)")
    else:
        warnings.append(f"RAG_OLLAMA_URL={ollama_url}")

    return len(required) == 0, required + warnings


def check_ollama_connectivity() -> tuple[bool, str]:
    """Check if Ollama endpoint is reachable."""
    try:
        import httpx
    except ImportError:
        return False, "httpx not installed (cannot check connectivity)"

    base_url = os.getenv("RAG_OLLAMA_URL", os.getenv("OLLAMA_URL", "http://10.127.0.192:11434"))
    try:
        response = httpx.get(f"{base_url}/api/tags", timeout=3.0)
        if response.status_code == 200:
            data = response.json()
            models = data.get("models", [])
            return True, f"Ollama reachable at {base_url} ({len(models)} models)"
        return False, f"Ollama returned {response.status_code}"
    except httpx.TimeoutException:
        return False, f"Ollama timeout at {base_url} (VPN down?)"
    except httpx.ConnectError:
        return False, f"Cannot connect to {base_url} (check firewall/VPN)"
    except Exception as e:
        return False, f"Error: {e}"


def check_packages() -> tuple[bool, list[str]]:
    """Check required Python packages."""
    required = [
        "numpy",
        "httpx",
        "langchain_ollama",  # Production requirement
    ]
    optional = [
        "faiss",
        "torch",
        "sentence_transformers",
    ]

    missing_required = []
    missing_optional = []

    for pkg in required:
        try:
            __import__(pkg)
        except ImportError:
            missing_required.append(pkg)

    for pkg in optional:
        try:
            __import__(pkg)
        except ImportError:
            missing_optional.append(pkg)

    messages = []
    if missing_required:
        messages.append(f"Missing REQUIRED: {', '.join(missing_required)}")
    if missing_optional:
        messages.append(f"Missing optional: {', '.join(missing_optional)}")

    if not missing_required and not missing_optional:
        messages.append("All packages installed")

    return len(missing_required) == 0, messages


def check_index_artifacts() -> tuple[bool, list[str]]:
    """Check if index artifacts exist."""
    required_files = [
        "chunks.jsonl",
        "vecs_n.npy",
        "meta.jsonl",
        "bm25.json",
    ]

    missing = []
    present = []

    for filename in required_files:
        path = Path(filename)
        if path.exists():
            size_mb = path.stat().st_size / (1024 * 1024)
            present.append(f"{filename} ({size_mb:.1f}MB)")
        else:
            missing.append(filename)

    messages = []
    if present:
        messages.append(f"Found: {', '.join(present)}")
    if missing:
        messages.append(f"Missing: {', '.join(missing)} (run 'make build')")

    return len(missing) == 0, messages


def check_disk_space() -> tuple[bool, str]:
    """Check available disk space."""
    try:
        import shutil
        total, used, free = shutil.disk_usage(".")
        free_gb = free / (1024 ** 3)
        if free_gb < 1:
            return False, f"Only {free_gb:.1f}GB free (need at least 1GB)"
        return True, f"{free_gb:.1f}GB free"
    except Exception as e:
        return False, f"Could not check disk space: {e}"


def main(strict: bool = False) -> int:
    """Run all checks and print results."""
    print("=" * 60)
    print("RAG Environment Verification")
    print("=" * 60)
    print()

    checks = [
        ("Python Version", check_python_version),
        ("Environment Variables", check_env_vars),
        ("Ollama Connectivity", check_ollama_connectivity),
        ("Python Packages", check_packages),
        ("Index Artifacts", check_index_artifacts),
        ("Disk Space", check_disk_space),
    ]

    all_passed = True
    warnings = []

    for name, check_fn in checks:
        print(f"[{name}]")
        try:
            passed, message = check_fn()

            if passed:
                icon = "✅"
            else:
                icon = "❌"
                all_passed = False

            if isinstance(message, list):
                for msg in message:
                    print(f"  {icon} {msg}")
                    if not passed or (strict and "warning" in msg.lower()):
                        warnings.append((name, msg))
            else:
                print(f"  {icon} {message}")
                if not passed:
                    warnings.append((name, message))
        except Exception as e:
            print(f"  ❌ Error: {e}")
            all_passed = False
            warnings.append((name, str(e)))

        print()

    print("=" * 60)

    if all_passed:
        print("✅ All checks passed! System ready.")
        return 0
    else:
        print("❌ Some checks failed. See above for details.")
        print()
        print("Common fixes:")
        print("  - Install packages: pip install -e .[dev]")
        print("  - Build index: make build")
        print("  - Check VPN connection for Ollama endpoint")
        print("  - Set ENVIRONMENT=dev for development mode")
        return 1


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Verify RAG environment")
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Treat warnings as errors",
    )
    args = parser.parse_args()

    sys.exit(main(strict=args.strict))
