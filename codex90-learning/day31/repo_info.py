import json
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen
import os
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parent / "data"


def fetch_repository(owner: str, repo: str) -> dict:
    api_url = f"https://api.github.com/repos/{owner}/{repo}"

    token = os.getenv("GITHUB_TOKEN")

    if not token:
        print("没有找到 GITHUB_TOKEN")
        return {}

    request = Request(
        api_url,
        headers={
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2026-03-10",
            "User-Agent": "python-ai-90days",
            "Authorization": f"Bearer {token}",
        },
    )

    try:
        with urlopen(request, timeout=10) as response:
            response_text = response.read().decode("utf-8")
            return json.loads(response_text)

    except HTTPError as error:
        print(f"HTTP请求失败，状态码：{error.code}")

    except URLError as error:
        print(f"网络连接失败：{error.reason}")

    except json.JSONDecodeError:
        print("服务器返回的内容不是有效JSON")

    return {}


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


if __name__ == "__main__":
    main()