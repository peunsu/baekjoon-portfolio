import sys
input = sys.stdin.readline

def dfs(v, visited, n, dp, costs):
    # 전체 방문한 상태일 경우 마지막 노드에서 0번 노드로 가는 비용 리턴
    if visited == (1 << n) - 1:
        return costs[v][0] if costs[v][0] > 0 else float('inf')
    
    # 이미 방문한 노드인 경우 리턴
    if dp[v][visited] != 0:
        return dp[v][visited]
    
    # 초기값 설정
    dp[v][visited] = float('inf')
    
    # 방문하지 않은 노드 중 비용이 0보다 큰 경우에 대해서만 탐색
    for i in range(1, n):
        if visited & (1 << i) == 0 and costs[v][i] > 0:
            dp[v][visited] = min(dp[v][visited], dfs(i, visited | (1 << i), n, dp, costs) + costs[v][i])

    return dp[v][visited]
    

def solve():
    n = int(input())
    costs = [list(map(int, input().split())) for _ in range(n)]
    
    # dp[v][visited]: v번 노드에서 출발하여 visited에 포함된 노드들을 방문한 상태일 때, 0번 노드로 돌아가는 최소 비용
    dp = [[0] * (1 << n) for _ in range(n)]
    
    ans = dfs(0, 1 << 0, n, dp, costs)
    print(ans)
    
solve()