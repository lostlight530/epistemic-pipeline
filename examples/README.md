# epistemic-pipeline 示例 / Example

本目录包含 epistemic-pipeline 的认知流水线使用示例。

## 示例：文献综述流水线 / Literature Review Pipeline

```bash
# 1. 使用线性依赖图执行文献综述
python core/engine.py run graphs/linear.yaml --inputs papers/

# 2. 使用自适应依赖图（根据输入规模自动选择策略）
python core/engine.py run graphs/adaptive.yaml --inputs papers/ --threshold 50

# 3. 并行执行：多个子任务并行分析
python core/engine.py run graphs/parallel.yaml --inputs papers/ --workers 4

# 4. 菱形流水线：分散→并行分析→聚合
python core/engine.py run graphs/diamond.yaml --inputs papers/
```

## 流水线阶段 / Pipeline Stages

```
discover → analyze → verify → synthesize → archive
  收集      分析       验证       综合        归档
```

## 图模板选择 / Graph Template Guide

| 场景 | 图模板 | 说明 |
|------|--------|------|
| 简单文献分析 | linear | 串行执行，适合 < 10 篇论文 |
| 批量对比分析 | parallel | 分组并行，适合 10-50 篇 |
| 深度综合研究 | diamond | 分散→并行→聚合，适合 > 50 篇 |
| 不确定性输入 | adaptive | 运行时根据规模自动选择 |
