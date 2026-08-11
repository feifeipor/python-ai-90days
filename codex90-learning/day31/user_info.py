from github_api import fetch_user


def main() -> None:
    username = input("请输入GitHub用户名：").strip()

    if not username:
        print("用户名不能为空")
        return

    user = fetch_user(username)

    if not user:
        print("没有获取到用户信息")
        return

    print("\nGitHub用户信息")
    print(f"用户名：{user['login']}")
    print(f"昵称：{user['name']}")
    print(f"公开仓库数量：{user['public_repos']}")
    print(f"Followers：{user['followers']}")
    print(f"Following：{user['following']}")
    print(f"主页：{user['html_url']}")


if __name__ == "__main__":
    main()