import json
from pathlib import Path

from github_api import fetch_repository


DATA_DIR = Path(__file__).resolve().parent / "data"


def save_repository(repository: dict) -> Path:
    DATA_DIR.mkdir(exist_ok=True)

    full_name = repository["full_name"].replace("/", "_")
    file_path = DATA_DIR / f"{full_name}.json"

    with open(
        file_path,
        "w",
        encoding="utf-8"
    ) as file:
        json.dump(
            repository,
            file,
            ensure_ascii=False,
            indent=4
        )

    return file_path


def main() -> None:
    owner = input("请输入GitHub用户名：").strip()
    repo = input("请输入仓库名称：").strip()

    if not owner or not repo:
        print("用户名和仓库名不能为空")
        return

    repository = fetch_repository(owner, repo)

    if not repository:
        print("没有获取到仓库信息")
        return

    file_path = save_repository(repository)

    print("仓库信息获取成功")
    print(f"仓库名称：{repository['full_name']}")
    print(f"项目描述：{repository['description']}")
    print(f"默认分支：{repository['default_branch']}")
    print(f"Star数量：{repository['stargazers_count']}")
    print(f"Fork数量：{repository['forks_count']}")
    print(f"开放Issue数量：{repository['open_issues_count']}")
    print(f"仓库地址：{repository['html_url']}")

    print(f"\nJSON数据已保存：{file_path}")


if __name__ == "__main__":
    main()