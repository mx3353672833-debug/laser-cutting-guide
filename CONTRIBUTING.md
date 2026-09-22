# Contributing · 贡献说明

[简体中文](#简体中文) | [English](#english)

## 简体中文

感谢你改进本教程。请保持中英文同步的事实、版本、条件与未验证标签。

### 如何提问

使用 Issue 模板三选一：

1. **学习疑问** — 看不懂、想更细的例子。请附章号与软件运行版本。  
2. **勘误** — 错字、错图、错步骤、错数值。请附复现步骤与截图。  
3. **版本差异** — 你的界面/菜单/授权与文中不同。请附「关于」版本、手册版本、照片（遮住客户信息）。

### 如何改文

1. 开分支（贡献者可用任意前缀；维护者用 `codex/`）。  
2. 同时改 `docs/zh-CN` 与 `docs/en` 对应文件；图注、答案、表单、术语也要同步。  
3. 不把研究 PDF、客户资料、绝对路径放进仓库。  
4. 跑 `python3 scripts/check_content.py`。  
5. 提 PR，使用 PR 模板勾选清单。

### 内容约定

- 步骤写清：做什么 → 在哪里 → 应该看到什么 → 如何检查。  
- 无实测界面时不编按钮位置；标 `待对应机器验证`。  
- 数值必须带条件；不写跨机型通用开关机/气压/速度。  
- 示意图标明「示意/Diagram」，不冒充截图。

## English

Please keep Chinese and English aligned on facts, versions, conditions, and unverified tags.

### Issues

Use one of three templates: **Learning question**, **Erratum**, **Version difference**. Include chapter id and runtime version; add screenshots with customer data removed.

### Pull requests

1. Branch (maintainers use `codex/` prefix).  
2. Update `docs/zh-CN` and `docs/en` counterparts (captions, answers, templates, glossary too).  
3. Do not commit research PDFs, customer data, or absolute machine paths.  
4. Run `python3 scripts/check_content.py`.  
5. Fill the PR checklist.

### Style

- Steps: do → where → expect → how to verify.  
- No invented button positions; mark `Pending machine verification`.  
- Numbers stay conditional.  
- Diagrams say “Diagram / 示意”, never pretend to be screenshots.
