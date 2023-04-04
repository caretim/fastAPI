import sys
input = sys.stdin.readline

N = int(input())

straw=[]
for _ in range(N):
    straw.append(int(input()))

straw.sort()


result = 0
for i in range(len(straw)-2):
    if straw[i] < straw[i+1] + straw[i+2]:
        result = straw[i] + straw[i+1] + straw[i+2]
        break
    else:
        result=-1

print(result)