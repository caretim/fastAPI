from itertools import combinations
n,m,k= map(int,input().split())


all_com = [*combinations( [i for i in range(n)],m)]

result= 0

for a in all_com:
    count =0
    for j in range(m):
        if a[j]<m:
            count+=1
    if count>=k:
        result+=1
    
print(result/len(all_com))
        
