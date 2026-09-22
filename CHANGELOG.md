# Changelog · 更新记录

## v0.2 — 2026-09-22 · 中文 / English

- 重写中英 16 章，以同一张双孔连接片贯穿尺寸、图层、路径和检验。 / Rewrote all 16 chapters in both languages around one two-hole plate.
- 合并重复学习路线；增加判断依据、具体例子和可核对的练习结果。 / Unified the reading path with worked examples and observable checks.
- 增加静态阅读站：章节目录、同章语言切换、正文搜索、图片放大、手机布局。 / Added a static reader with chapter navigation, same-page language switching, text search, image zoom and mobile layout.
- 修正单位练习的导入条件、割缝默认值建议及首件放行示例。 / Corrected importer-dependent unit behavior, default-kerf advice and the first-part acceptance example.
- CI 必须实际解析 DXF，并检查生成站点的链接和资源。 / CI now requires actual DXF parsing and checks generated site links and assets.
- 实际软件导入、机床动作和切割结果仍需指定设备验证。 / Software imports, machine motion and cutting results still require validation on the specified equipment.

## v0.1 — 2026-09-22 · 中文 / English

### 新增 / Added

- 中英双语 00–15 章完整正文 / Full bilingual chapters 00–15
- 12 张共享示意图、8 个 DXF、预览、折叠答案 / 12 diagrams, 8 DXF files, previews, collapsible answers
- 术语表、版本范围、来源索引、已知缺口 / glossary, version scope, sources, known gaps
- 可填写表单 6 类 / 6 fill-in templates
- `scripts/check_content.py` 与 GitHub Actions / checker and Actions workflow
- Issue / PR 模板、贡献与许可说明 / templates, contributing, license policy

### 已知未验证 / Still unverified

- 实机首件、UI 截图、展会官方指南、Plus 完整授权、无痕微连默认留根比例  
- Live first part, UI screenshots, vendor demo guide, full Plus licensing, default seamless root ratio

### 语言同步 / Language sync

- v0.1 中英文同批发布，章节 ID 对应 / v0.1 ships both languages with matching chapter IDs
