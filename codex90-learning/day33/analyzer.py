def analyze_repository(repository, commits):

    result = {}

    result["name"] = repository["full_name"]

    result["stars"] = repository["stars"]

    result["forks"] = repository["forks"]

    result["commit_count"] = len(commits)


    if len(commits) >= 5:
        result["activity"] = "活跃"

    elif len(commits) >= 1:
        result["activity"] = "一般"

    else:
        result["activity"] = "暂无提交"


    score = 0

    if result["stars"] > 10:
        score += 30

    if result["forks"] > 5:
        score += 30

    if result["commit_count"] >= 5:
        score += 40


    result["score"] = score


    return result