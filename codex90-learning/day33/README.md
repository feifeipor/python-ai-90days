# Day33 - GitHub Project Analyzer


## 项目目标

通过 GitHub API 获取仓库信息，
自动生成项目分析报告。


## 功能

- 查询仓库信息
- 查询用户信息
- 获取最近Commit
- 分析项目活跃度
- 自动生成Markdown报告


## 技术

- Python
- requests
- GitHub API
- JSON
- Markdown


## 运行

```bash
python main.py
```

## 示例输出

生成报告：

reports/
└── feifeipor_python-ai-90days_report.md


## 项目流程

用户输入
↓
GitHub API
↓
数据分析
↓
Markdown报告


## 学习收获

- requests调用API
- Token认证
- 模块化设计
- 数据处理
- 文件生成