# Claim transfer example

## 中文技术对应 / Chinese subject counterpart

**具体责任 / Owning subject:** 本地 Claim Transfer 示例展示来源、冲突、claim 标识和启发式值的保留，不意味着该 claim 已经可靠验证

**English owner:** Claim transfer example

**可重复检查 / Reproducibility:** 应先固定 Graph/profile、state、checkpoint 及上下游 sidecar 的精确版本和 bytes，再按原文命令判断返回结果，不能把测试定义、Provider 说明或高分视为已经独立复现 / Freeze actual source and sidecar identity, execution inputs, real receipts and unknown outcomes, a declared audit cannot certify truth

| English chapter / 原章节 | 中文对应定位 / Chinese meaning |
| --- | --- |


**保存不确定性 / Preserve unknowns:** 原始冲突、缺失来源、非概率 score 与失败注入观察保持各自身份，本节不新增科学或外部效果验证 / Historical and local evidence states are not silently promoted


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
