from github_client import github_get


def main():

    username = input(
        "请输入GitHub用户名："
    ).strip()

    user = github_get(
        f"/users/{username}"
    )

    if not user:
        print("没有获取用户信息")
        return

    print("\n用户信息")
    print(
        f"用户名：{user['login']}"
    )
    print(
        f"昵称：{user['name']}"
    )
    print(
        f"公开仓库数量：{user['public_repos']}"
    )
    print(
        f"Followers：{user['followers']}"
    )
    print(
        f"主页：{user['html_url']}"
    )


if __name__ == "__main__":
    main()