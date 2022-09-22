n, k = map(int, input().split())

pos = [-1] * 100001
pos[n] = 0

target = {n: {2*n, n-1, n+1}}
while pos[k] == -1:
    after_target = dict()
    for x in target.keys():
        for i in target[x]:
            if i < 0 or i > 100000:
                continue
            if pos[i] == -1:
                pos[i] = pos[x] + 1
                after_target[i] = {2*i, i-1, i+1}
    target = after_target

print(pos[k])