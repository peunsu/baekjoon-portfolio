import sys
input = sys.stdin.readline

def preorder(v: str) -> str:
    if v == '.':
        return ''

    result = v
    result += preorder(tree[v][0])
    result += preorder(tree[v][1])
    
    return result
    
def inorder(v: str) -> str:
    if v == '.':
        return ''

    result = inorder(tree[v][0])
    result += v
    result += inorder(tree[v][1])
    
    return result

def postorder(v: str) -> str:
    if v == '.':
        return ''
    
    result = postorder(tree[v][0])
    result += postorder(tree[v][1])
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