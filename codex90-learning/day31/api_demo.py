import json
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


API_URL = "https://api.github.com"


def fetch_github_api() -> dict:
    request = Request(
        API_URL,
        headers={
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2026-03-10",
            "User-Agent": "python-ai-90days",
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
    data = fetch_github_api()

    if not data:
        print("没有获取到数据")
        return

    print("API请求成功")
    print(f"返回字段数量：{len(data)}")
    print("前5个字段：")

    for key in list(data.keys())[:5]:
        print(f"- {key}")


if __name__ == "__main__":
    main()