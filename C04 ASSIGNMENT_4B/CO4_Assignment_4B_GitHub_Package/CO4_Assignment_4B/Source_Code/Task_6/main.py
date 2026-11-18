# Task 6: Held-Karp bitmask DP, exact route reconstruction and exhaustive validation.
from itertools import permutations
from time import perf_counter
def held_karp(cost):
    n=len(cost);dp={(1<<(j-1),j):(cost[0][j],0) for j in range(1,n)};states=len(dp)
    for mask in range(1,1<<(n-1)):
        for j in range(1,n):
            if not (mask&(1<<(j-1))):continue
            key=(mask,j)
            if key in dp:continue
            previous=mask^(1<<(j-1));choices=[]
            for k in range(1,n):
                if previous&(1<<(k-1)) and (previous,k) in dp:choices.append((dp[(previous,k)][0]+cost[k][j],k))
            if choices:dp[key]=min(choices);states+=1
    full=(1<<(n-1))-1
    best,end=min((dp[(full,j)][0]+cost[j][0],j) for j in range(1,n))
    path=[];mask=full;j=end
    while j:
        path.append(j);_,prev=dp[(mask,j)];mask^=1<<(j-1);j=prev
    return best,[0]+path[::-1]+[0],states
def brute(cost):
    return min((sum(cost[route[i]][route[i+1]] for i in range(len(route)-1)),route) for order in permutations(range(1,len(cost))) for route in [[0,*order,0]])
def matrix(n):
    return [[0 if i==j else 5+abs(i-j)*3+((i*7+j*11)%9) for j in range(n)] for i in range(n)]
if __name__=='__main__':
    small=matrix(5);print('SMALL COST MATRIX');[print(row) for row in small]
    print('DP VALIDATION',held_karp(small));print('BRUTE VALIDATION',brute(small))
    for delivery in (4,5,6,7,8):
        cost=matrix(delivery+1);start=perf_counter();best,route,states=held_karp(cost);elapsed=perf_counter()-start
        print('delivery locations',delivery,'states',states,'time_sec',round(elapsed,6),'estimated_DP_entries',states,'best',best,'route',route)
    print('200 locations: exact exponential DP intentionally not attempted')
