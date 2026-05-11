<!-- This file is generated from sphinx-notes/cookiecutter. --> 

## 基本说明

这是一个由 SphinxNotes 开发的 Sphinx Extension，由 `sphinxnotes/cookiecutter` 生成，很多基础文件来自模板。

## 首先阅读

- 开始了解项目时，优先阅读 `docs/index.rst`。
- 如果任务和文档、Sphinx 配置或示例有关，继续阅读 `docs/` 下的其他文件

## 通用知识

- 使用 `make` 会构建 `docs/` 下的文档，文档自依赖当前项目，因此文档构建成功也意味着项目基本能正常构建
  - `docs/_build` 存放构建好的文档，`make clean` 清除所有构建结果
  - `make test` 运行测试，测试位于 `tests/`，可能的 e2e 测试位于 `tests/test_e2e.py`
  - `make doctest` 运行 Sphinx 文档测试
  - `make install` 使用 `pip install --user` 将项目安装到本地，跨项目测试时常用
- `make tmpl-*` 用于模板同步，参看 "模板同步" 小节

## 关于 SphinxNotes 项目

- 同为 `sphinxnotes` 项目的其他仓库通常位于当前项目的上一级目录
- 如果你在阅读代码时遇到本地依赖、模板来源或跨仓库复用关系，可以直接读取这些本地仓库文件，不必先猜测实现，也不必优先去远程搜索。
- 当我提到 "所有项目" 的时候，请从当前项目的上一级目录的 `cookiecutter/project-list.txt` 获取项目列表
- `docs/conf.py` 往往会直接从源码树导入当前项目，因此排查文档构建问题时，要同时检查运行时依赖和文档依赖。

## 模板同步

- 先确认任务是当前项目问题，还是模板问题；如果是模板问题，优先在 `sphinxnotes/cookiecutter` 中修复。
- 模板变更完成后，优先使用 `make tmpl-update` 把改动同步回项目，而不是手工重复修改生成文件。
- 如果 `make tmpl-update` 产生 `.rej`、冲突或三方合并失败，优先尝试 `make tmpl-apply-rej`，再手工解决冲突。
- 手工解决冲突时，重点检查 `README.rst`、`pyproject.toml`、`.github/workflows/`、`docs/conf.py`、`docs/requirements.txt` 这些常见受影响文件。
- 当模板同步结果确认无误后，优先使用 `make tmpl-update-done` 完成后续收尾步骤。

### 修改约定

- 修改模板生成文件时，保留原有注释，除非模板本身已经统一移除了这些注释。
- 遇到 `CUSTOM ... START` / `END` 这类用户自定义区块时，必须保留这些锚点，并尽量保留区块中的用户内容。
- 如果模板更新和项目内手工修改发生冲突，优先保护用户自定义内容，再整理模板变更。
