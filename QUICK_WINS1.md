# Quick Wins (Top 10)

All items require <30 minutes, offer high impact, and are low risk.

1. **Import fixes for clockify_rag.http_utils**  
   Add missing imports at top of module:  
   ```python
   import logging
   import os
   import requests
   ```  
   Impact: prevents immediate NameError when module imported.【F:clockify_rag/http_utils.py†L1-L40】

2. **Raise local embedding batch size constant**  
   Match CLI tuning by bumping `_ST_BATCH_SIZE` to 96.  
   ```python
   _ST_BATCH_SIZE = int(os.getenv("EMB_BATCH", "96"))
   ```  
   Impact: ~2x faster SentenceTransformer batches.【F:clockify_rag/embedding.py†L9-L32】

3. **Honor query logging privacy flags**  
   Before writing `answer` in `log_query`, gate on `LOG_QUERY_INCLUDE_ANSWER`.  
   ```python
   from clockify_rag.config import LOG_QUERY_INCLUDE_ANSWER, LOG_QUERY_ANSWER_PLACEHOLDER
   if LOG_QUERY_INCLUDE_ANSWER:
       log_entry["answer"] = answer
   elif LOG_QUERY_ANSWER_PLACEHOLDER:
       log_entry["answer"] = LOG_QUERY_ANSWER_PLACEHOLDER
   ```  
   Impact: avoids leaking sensitive answers in logs.【F:clockify_support_cli_final.py†L2388-L2458】

4. **Expose retrieval profiling summary in debug logs**  
   After `log_kpi`, add:  
   ```python
   if logger.isEnabledFor(logging.DEBUG) and RETRIEVE_PROFILE_LAST:
       logger.debug(json.dumps({"event": "retrieve_profile", **RETRIEVE_PROFILE_LAST}))
   ```  
   Impact: immediate visibility into ANN reuse.【F:clockify_support_cli_final.py†L1508-L1692】

5. **Document query expansion override**  
   Add docstring snippet to README showing `CLOCKIFY_QUERY_EXPANSIONS` usage.  
   Impact: encourages tuning without code changes.【F:clockify_support_cli_final.py†L167-L238】

6. **Remove legacy CLI stub**  
   Delete `clockify_support_cli.py` (17 LOC) or replace with import to main entrypoint.  
   Impact: prevents accidental import of outdated module.【F:clockify_support_cli.py†L1-L17】

7. **Update Makefile default target**  
   Point `run` target to `python -m clockify_support_cli_final chat`.  
   Impact: ensures contributors run maintained CLI.【F:Makefile†L1-L123】

8. **Add `set -euo pipefail` to shell scripts**  
   Prepend safety flags to scripts under `scripts/`.  
   ```bash
   set -euo pipefail
   ```  
   Impact: avoids silent failures in automation.【F:scripts/acceptance_test.sh†L1-L80】

9. **Surface JSON confidence in tests**  
   Extend `tests/test_json_output.py` to assert `confidence` field exists.  
   Impact: locks in Rank 28 change.【F:tests/test_json_output.py†L1-L36】

10. **Add README link to benchmark suite**  
    Insert quick command snippet referencing `python benchmark.py --quick`.  
    Impact: makes performance tooling discoverable.【F:README.md†L1-L525】
