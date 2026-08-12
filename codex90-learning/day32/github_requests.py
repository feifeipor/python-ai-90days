import os
import requests


BASE_URL = "https://api.github.com"


def github_get(path: str) -> dict:
    token = os.getenv("GITHUB_TOKEN")

    if not token:
        print("没有找到 GITHUB_TOKEN")
        return {}

    url = f"{BASE_URL}{path}"

    headers = {
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2026-03-10",
        "Authorization": f"Bearer {token}",
    }

    try:
        response = requests.get(
            url,
            headers=headers,
            timeout=10
        )

        response.raise_for_status()

        return response.json()

    except requests.exceptions.HTTPError:
        print(
            f"HTTP错误：{response.status_code}"
        )

    except requests.exceptions.RequestException as error:
        print(
            f"请求失败：{error}"
        )

    return {}


def main():

    data = github_get(
        "/repos/feifeipor/python-ai-90days"
    )

    if not data:
        print("没有获取数据")
        return

    print("请求成功")
    print(
        f"仓库名称：{data['full_name']}"
    )
    print(
        f"Stars：{data['stargazers_count']}"
    )


if __name__ == "__main__":
    main()