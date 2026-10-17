# Contributing / 参与贡献

## 贡献范围 / Scope

欢迎提交能够提高证据可追溯性、双语一致性、作者控制和来源清晰度的修改。这个项目收录的是可复用的 Skill、Prompt 和审查规则，不收录未经授权的截图、私人信息、未经授权的整段网络复制内容或虚构的研究结果。

Contributions that improve evidence traceability, bilingual consistency, author control, and provenance clarity are welcome. This project accepts reusable Skills, prompts, and review rules. Do not submit unauthorized screenshots, private information, unauthorized copied web passages, or fabricated research results.

## 提交前检查 / Before submitting

1. 说明改动解决的具体科研写作问题。
2. 对新增或改写内容提供来源；来源不明时写明“来源于网络，自行整理汇总”或“许可证待核验”。
3. 保持中文和英文语义、证据强度和限制披露一致。
4. 不改变用户提供的数字、单位、样本量、统计量、引用或运行结果。
5. 检查没有选择性删除阴性结果、失败实验、关键限制或报告要求。
6. 运行 `python3 scripts/validate_project.py`、`ruby scripts/validate_frontmatter.rb` 和 `git diff --check`。

1. State the concrete research-writing problem the change addresses.
2. Provide provenance for new or rewritten material; when provenance is unknown, say “collected from public online material and independently organized” or “license unverified.”
3. Keep Chinese and English aligned in meaning, evidential strength, and disclosures.
4. Do not change supplied numbers, units, sample sizes, statistics, citations, or execution results.
5. Check that null findings, failed experiments, material limitations, and required reporting items were not selectively removed.
6. Run `python3 scripts/validate_project.py`, `ruby scripts/validate_frontmatter.rb`, and `git diff --check`.

## 内容规则 / Content rules

- Skill 的 frontmatter 必须有小写连字符格式的 `name` 和实际用途描述。
- Skill 必须包含适用场景、边界、输入、流程、输出、质量检查、局限、完整示例、信息不足示例和来源。
- Prompt 必须包含使用场景、输入要求、输出要求、禁止编造、信息不足处理、双语示例和来源。
- 对照论文时记录链接、定位信息和阅读层级。摘要级来源不能支持未经全文核验的实验或证明判断。
- 不把来源论文的 Oral 身份、会议排名或处理数量写成录用保证或科学正确性证明。
- 不用项目规避 AI 检测、掩盖抄袭、伪造作者贡献或替作者决定研究主线。

- Skill frontmatter must include a lowercase hyphenated `name` and a description of the actual use.
- A Skill must include use cases, boundaries, inputs, workflow, outputs, quality checks, limitations, a complete example, an insufficient-information example, and provenance.
- A prompt must include use case, inputs, outputs, a fabrication ban, missing-information handling, a bilingual example, and provenance.
- For paper comparisons, record the link, locator, and reading level. An abstract-level source cannot support an experimental or proof claim that was not checked in the full text.
- Do not present Oral status, venue ranking, or corpus counts as acceptance guarantees or proof of scientific correctness.
- Do not use the project to evade AI detection, conceal plagiarism, misrepresent authorship, or choose the research story for the author.

## Pull request description / Pull Request 说明

请在 Pull Request 中说明：

Please include:

- 改动摘要 / Summary of changes;
- 来源和许可证状态 / Sources and license status;
- 已完成检查 / Checks completed;
- 待核验内容 / Items still unverified;
- 是否包含真实论文案例；如果包含，请去除私人信息并确认作者有权公开 / Whether real manuscript examples are included; remove private information and confirm publication permission.

## 自动检查 / Automated checks

提交到 `main` 的 Push 和 Pull Request 会运行 [`.github/workflows/validate.yml`](.github/workflows/validate.yml)。本地提交前应运行贡献规则中列出的两个脚本和 `git diff --check`。

Pushes and pull requests targeting `main` run [`.github/workflows/validate.yml`](.github/workflows/validate.yml). Before submitting locally, run the two scripts listed above and `git diff --check`.
