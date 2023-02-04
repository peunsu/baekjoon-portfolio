import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def postorder(first, end):
    if first >= end:
        return

    root = tree_pre[first]
    mid = end

    for i in range(first, end):
        if tree_pre[i] > root:
            mid = i
            break

    postorder(first+1, mid)
    postorder(mid, end)
    print(root)

tree_pre = []
while True:
    try:
        tree_pre.append(int(input()))
    except:
        break
postorder(0, len(tree_pre))