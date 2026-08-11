from github_api import fetch_commits


def main() -> None:
    owner = input("请输入GitHub用户名：").strip()
    repo = input("请输入仓库名称：").strip()

    if not owner or not repo:
        print("用户名和仓库名不能为空")
        return

    commits = fetch_commits(
        owner,
        repo,
        per_page=5
    )

    if not commits:
        print("没有获取到Commit信息")
        return

    print("\n最近5次Commit：")

    for index, item in enumerate(
        commits,
        start=1
    ):
        message = item["commit"]["message"]
        author = item["commit"]["author"]["name"]
        date = item["commit"]["author"]["date"]
        sha = item["sha"][:7]

        print(f"\n{index}. {message}")
        print(f"   作者：{author}")
        print(f"   时间：{date}")
        print(f"   SHA：{sha}")


if __name__ == "__main__":
    main()