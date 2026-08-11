from github_api import fetch_commits


def main() -> None:
    owner = input("请输入GitHub用户名：").strip()
    repo = input("请输入仓库名称：").strip()

    if not owner or not repo:
        print("用户名和仓库名不能为空")
        return
    try:
        count = int(
            input("请输入要查看的Commit数量（1-20）：")
        )

    except ValueError:
        print("请输入数字")
        return

    if not 1 <= count <= 20:
        print("数量必须在1到20之间")
        return

    commits = fetch_commits(
        owner,
        repo,
        per_page=count
    )

    if not commits:
        print("没有获取到Commit信息")
        return

    print(f"\n最近{len(commits)}次Commit：")

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