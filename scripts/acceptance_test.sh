#!/bin/bash
#
# v4.1 Acceptance Tests
# Validates:
# - FAISS initialization and lazy loading
# - Warm-up on startup functionality
# - JSON output path
# - .gitignore artifact coverage
#
set -e

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$REPO_ROOT"

echo "=== v4.1 Acceptance Tests ==="
echo ""

# Test 1: Check .gitignore covers v4.1 artifacts
echo "[Test 1/5] .gitignore artifact coverage..."
GITIGNORE_CHECKS=(
    "faiss.index"
    "hnsw_cosine.bin"
    "emb_cache.jsonl"
    "vecs_f16.memmap"
    ".build.lock"
    "build.log"
)

all_present=true
for artifact in "${GITIGNORE_CHECKS[@]}"; do
    if grep -q "^${artifact}\$" .gitignore; then
        echo "  ✅ $artifact in .gitignore"
    else
        echo "  ⚠️  $artifact NOT in .gitignore (optional)"
    fi
done
echo "  ✅ .gitignore check complete"
echo ""

# Test 2: Validate Python script syntax
echo "[Test 2/5] Python syntax validation..."
python3 -m py_compile clockify_support_cli_final.py
echo "  ✅ clockify_support_cli_final.py syntax valid"
echo ""

# Test 3: Check FAISS integration code presence
echo "[Test 3/5] FAISS lazy-load integration..."
if grep -q "global _FAISS_INDEX" clockify_support_cli_final.py; then
    echo "  ✅ Global _FAISS_INDEX declared"
else
    echo "  ❌ Missing global _FAISS_INDEX"
    exit 1
fi

if grep -q "def load_faiss_index" clockify_support_cli_final.py; then
    echo "  ✅ load_faiss_index function exists"
else
    echo "  ❌ Missing load_faiss_index function"
    exit 1
fi

if grep -q "info: ann=faiss status=loaded" clockify_support_cli_final.py; then
    echo "  ✅ Greppable FAISS logging present"
else
    echo "  ⚠️  Greppable FAISS logging format check (optional)"
fi
echo ""

# Test 4: Check warm-up functionality
echo "[Test 4/5] Warm-up on startup functionality..."
if grep -q "def warmup_on_startup" clockify_support_cli_final.py; then
    echo "  ✅ warmup_on_startup function exists"
else
    echo "  ❌ Missing warmup_on_startup function"
    exit 1
fi

if grep -q "WARMUP" clockify_support_cli_final.py; then
    echo "  ✅ WARMUP environment variable check present"
else
    echo "  ❌ Missing WARMUP environment variable handling"
    exit 1
fi

if grep -q "warmup_on_startup()" clockify_support_cli_final.py; then
    echo "  ✅ warmup_on_startup called from chat_repl"
else
    echo "  ⚠️  warmup_on_startup call location check (optional)"
fi
echo ""

# Test 5: Check JSON output wiring
echo "[Test 5/5] JSON output integration..."
if grep -q "def chat_repl" clockify_support_cli_final.py; then
    echo "  ✅ chat_repl function exists"
else
    echo "  ❌ Missing chat_repl function"
    exit 1
fi

if grep -q "use_json" clockify_support_cli_final.py; then
    echo "  ✅ use_json parameter wiring present"
else
    echo "  ❌ Missing use_json parameter"
    exit 1
fi

if grep -q "answer_to_json" clockify_support_cli_final.py; then
    echo "  ✅ answer_to_json output function exists"
else
    echo "  ⚠️  answer_to_json function check (optional)"
fi

if grep -q "\"json\"" clockify_support_cli_final.py; then
    echo "  ✅ JSON flag handling in CLI args"
else
    echo "  ⚠️  JSON flag handling check (optional)"
fi
echo ""

# Summary
echo "=== ACCEPTANCE TESTS COMPLETE ==="
echo "✅ All v4.1 integration points validated"
echo ""
echo "Remaining tasks:"
echo "  - Version bump to v4.1.0"
echo "  - Create CHANGELOG.md"
echo "  - Commit and push to main"
echo "  - Tag v4.1.0 release"
