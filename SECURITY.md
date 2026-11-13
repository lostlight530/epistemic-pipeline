# Security Policy

Please report security-sensitive issues privately to the maintainer rather than opening a public issue.

### 双语安全与数据边界 / Bilingual security and data boundary

**中文**：安全问题通过私密渠道报告；公开 issue、PR 或运行日志不得携带令牌、凭据、个人资料和未公开的漏洞细节；状态机验证、checkpoint 摘要和静态扫描只能证明声明范围内的性质，不认证外部提供方、来源可信度或完整的端到端安全性

**English**: Report security-sensitive findings privately; avoid placing credentials, private data or undisclosed exploit details in public issues, PRs or run logs. State validation, checkpoint digests and static scans establish only their declared properties, not external-provider authenticity, source trustworthiness or end-to-end security certification

## Scope

Security reports should concern repository-owned code, automation, validation logic, runtime-policy handling, workflows, or documentation that could materially mislead users about a security boundary.

Do not include credentials, private data, or exploit details in public issues or pull requests. External providers, source material, and downstream systems retain their own security and trust boundaries.

Passing repository checks is evidence only for the tested revision and declared scope; it is not a general security certification.
