from github_client import github_get


def main():

    owner = "feifeipor"
    repo = "python-ai-90days"

    repository = github_get(
        f"/repos/{owner}/{repo}"
    )

    if not repository:
        print("没有获取数据")
        return

    print("仓库信息")
    print(
        f"名称：{repository['full_name']}"
    )

    print(
        f"Stars：{repository['stargazers_count']}"
    )


if __name__ == "__main__":
    main()