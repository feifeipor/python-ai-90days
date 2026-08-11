import json
import os
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen
from urllib.parse import urlencode


BASE_URL = "https://api.github.com"


def github_get(path: str) -> dict | list:
    token = os.getenv("GITHUB_TOKEN")

    if not token:
        print("没有找到 GITHUB_TOKEN")
        return {}

    api_url = f"{BASE_URL}{path}"

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


def fetch_repository(owner: str, repo: str) -> dict:
    return github_get(
        f"/repos/{owner}/{repo}"
    )


def fetch_user(username: str) -> dict:
    return github_get(
        f"/users/{username}"
    )

def fetch_commits(
    owner: str,
    repo: str,
    per_page: int = 5
) -> list:

    params = urlencode({
        "per_page": per_page
    })

    data = github_get(
        f"/repos/{owner}/{repo}/commits?{params}"
    )

    if isinstance(data, list):
        return data

    return []