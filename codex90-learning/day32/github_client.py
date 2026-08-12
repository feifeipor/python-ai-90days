import os
import requests


BASE_URL = "https://api.github.com"


def github_get(path: str):

    token = os.getenv("GITHUB_TOKEN")

    if not token:
        print("没有找到 GITHUB_TOKEN")
        return {}

    url = f"{BASE_URL}{path}"

    headers = {
        "Accept": "application/vnd.github+json",
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

    except requests.exceptions.RequestException as error:
        print(f"请求失败：{error}")

        return {}