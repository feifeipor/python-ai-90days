from pathlib import Path
from datetime import datetime


REPORT_DIR = Path(__file__).parent / "reports"


def create_report(
    repository,
    user,
    analysis
):

    REPORT_DIR.mkdir(
        exist_ok=True
    )

    safe_name = repository["name"].replace("/", "_")

    filename = (
            REPORT_DIR
            / f"{safe_name}_report.md"
    )


    content = f"""
# GitHub项目分析报告


## 基本信息

项目名称：

{repository['name']}


GitHub地址：

{repository['url']}


## 项目数据

⭐ Stars:

{repository['stars']}


🍴 Forks:

{repository['forks']}


## 作者信息

用户名：

{user['login']}


公开仓库数量：

{user['public_repos']}


## Commit情况

最近提交数量：

{repository['commit_count']}


## 项目分析

活跃度：

{analysis['activity']}


评分：

{analysis['score']} / 100


## 生成时间

{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

"""


    with open(
        filename,
        "w",
        encoding="utf-8"
    ) as file:

        file.write(content)


    return filename