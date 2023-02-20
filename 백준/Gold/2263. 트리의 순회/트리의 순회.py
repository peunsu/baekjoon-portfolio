import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

'''
프리오더: 루트, 왼쪽, 오른쪽
인오더: 왼쪽, 루트, 오른쪽
포스트오더: 왼쪽, 오른쪽, 루트
'''

def in_and_post_to_pre(in_start, in_end, post_start, post_end):
    if in_start > in_end or post_start > post_end:
        return

    root = postorder[post_end]
    root_idx = root_idx_arr[root]
    left_in_start = in_start
    left_in_end = root_idx - 1
    left_post_start = post_start
    left_post_end = post_start + root_idx - in_start - 1
    right_in_start = root_idx + 1
    right_in_end = in_end
    right_post_start = post_start + root_idx - in_start
    right_post_end = post_end - 1

    print(root, end=" ")
    in_and_post_to_pre(left_in_start, left_in_end, left_post_start, left_post_end)
    in_and_post_to_pre(right_in_start, right_in_end, right_post_start, right_post_end)


n = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))

root_idx_arr = [0] * (n+1)
for i in range(n):
    root_idx_arr[inorder[i]] = i

in_and_post_to_pre(0, n-1, 0, n-1)