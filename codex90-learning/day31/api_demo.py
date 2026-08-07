import json
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


API_URL = "https://api.github.com"


def fetch_github_api() -> tuple[dict, int, str, str]:
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
            status_code = response.status

            content_type = response.headers.get(
                "Content-Type",
                "未知"
            )

            rate_limit_remaining = response.headers.get(
                "X-RateLimit-Remaining",
                "未知"
            )

            response_text = response.read().decode("utf-8")
            data = json.loads(response_text)

            return (
                data,
                status_code,
                content_type,
                rate_limit_remaining,
            )

    except HTTPError as error:
        print(f"HTTP请求失败，状态码：{error.code}")

    except URLError as error:
        print(f"网络连接失败：{error.reason}")

    except json.JSONDecodeError:
        print("服务器返回的内容不是有效JSON")

    return {}, 0, "未知", "未知"


def main() -> None:
    data, status_code, content_type, rate_limit = fetch_github_api()

    if not data:
        print("没有获取到数据")
        return

    print("API请求成功")
    print(f"HTTP状态码：{status_code}")
    print(f"数据类型：{content_type}")
    print(f"剩余请求次数：{rate_limit}")
    print(f"返回字段数量：{len(data)}")

    print("\n前5个字段：")

    for key in list(data.keys())[:5]:
        print(f"- {key}")


if __name__ == "__main__":
    main()