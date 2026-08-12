# Day32 - Requests API Client

## 今日目标

- 学习 requests 第三方库
- 使用 requests 发送 HTTP 请求
- 处理 API 返回数据
- 对比 urllib 和 requests

## 对比

urllib:

Request
→ urlopen
→ decode
→ json.loads


requests:

requests.get()
→ response.json()