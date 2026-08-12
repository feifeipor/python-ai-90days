from github_client import (
    get_repository,
    get_user,
    get_commits
)

from analyzer import analyze_repository

from report import create_report


def main():

    owner = input(
        "请输入GitHub用户名："
    ).strip()

    repo = input(
        "请输入仓库名称："
    ).strip()


    print("\n正在获取仓库信息...")

    repository = get_repository(
        owner,
        repo
    )


    if not repository:
        print("仓库获取失败")
        return


    print("正在获取用户信息...")

    user = get_user(
        owner
    )


    if not user:
        print("用户获取失败")
        return


    print("正在获取Commit...")

    commits = get_commits(
        owner,
        repo,
        5
    )


    print("正在分析项目...")


    analysis = analyze_repository(
        {
            "full_name": repository["full_name"],
            "stars": repository["stargazers_count"],
            "forks": repository["forks_count"],
            "commit_count": len(commits)
        },
        commits
    )


    report_repository = {
        "name": repository["full_name"],
        "url": repository["html_url"],
        "stars": analysis["stars"],
        "forks": analysis["forks"],
        "commit_count": analysis["commit_count"]
    }


    filename = create_report(
        report_repository,
        user,
        analysis
    )


    print("\n分析完成")
    print(
        f"报告生成：{filename}"
    )


if __name__ == "__main__":
    main()