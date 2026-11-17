# Task 3: 0/1 knapsack with reconstruction

def knapsack(items,capacity):
    if capacity<0 or any(w<0 for _,w,_ in items): raise ValueError('Invalid weights/capacity')
    n=len(items);dp=[[0]*(capacity+1) for _ in range(n+1)]
    for i in range(1,n+1):
        name,weight,value=items[i-1]
        for c in range(capacity+1):
            dp[i][c]=dp[i-1][c]
            if weight<=c:dp[i][c]=max(dp[i][c],value+dp[i-1][c-weight])
    chosen=[];c=capacity
    for i in range(n,0,-1):
        if dp[i][c]!=dp[i-1][c]:
            chosen.append(items[i-1][0]);c-=items[i-1][1]
    return dp[n][capacity],list(reversed(chosen)),dp
if __name__=='__main__':
    value,chosen,dp=knapsack([('P',2,12),('Q',3,20),('R',4,25),('S',5,30)],7)
    print('Task 3 0/1 knapsack: optimum',value,'items',chosen)
    print('Final DP row:',dp[-1])
