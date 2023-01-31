import sys
input = sys.stdin.readline

def preorder(v: str) -> str:
    result = v
    if tree[v][0] != '.':
        result += preorder(tree[v][0])
        if tree[v][1] != '.':
            result += preorder(tree[v][1])
    else:
        if tree[v][1] != '.':
            result += preorder(tree[v][1])
    
    return result
    
def inorder(v: str) -> str:
    result = v
    if tree[v][0] != '.':
        result = inorder(tree[v][0]) + result
        if tree[v][1] != '.':
            result += inorder(tree[v][1])
    else:
        if tree[v][1] != '.':
            result += inorder(tree[v][1])
    
    return result

def postorder(v: str):
    result = ''
    if tree[v][0] != '.':
        result = postorder(tree[v][0]) + result
        if tree[v][1] != '.':
            result += postorder(tree[v][1])
    else:
        if tree[v][1] != '.':
            result = postorder(tree[v][1]) + result
    
    result += v

    return result


n = int(input())
tree = dict()

for _ in range(n):
    root, left, right = input().rstrip().split()
    tree[root] = (left, right)

print(preorder('A'))
print(inorder('A'))
print(postorder('A'))