# Claim transfer example

Select one or more claim records from an existing claim-verification sidecar and preserve their audit context for downstream use.

```bash
python core/claim_transfer.py \
  claim-audits/run-42.claim-audit.json \
  --claim-id claim_1 \
  --claim-id claim_2 \
  --purpose scientific-figure-handoff \
  --output transfers/run-42.claim-transfer.json
```

Without `--claim-id`, all indexed claim records are transferred.

The transfer preserves source/evidence refs, conflicts, structural observations, heuristic-score observations and audit state while keeping full claim prose out of the sidecar by default.

```text
transfer != acceptance
evidence ref != evidence sufficiency
conflict visible != conflict adjudicated
audit state != scientific verdict
heuristic score != probability
```
