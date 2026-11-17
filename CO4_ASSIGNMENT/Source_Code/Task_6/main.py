# Task 6: Weighted interval scheduling - dynamic programming
from bisect import bisect_right

def weighted_schedule(jobs,trace=False):
    jobs=sorted(jobs,key=lambda x:x[2]) # (id,start,finish,value)
    finishes=[j[2] for j in jobs];n=len(jobs)
    prev=[bisect_right(finishes,jobs[i][1],0,i) for i in range(n)]
    dp=[0]*(n+1)
    for i in range(1,n+1):
        name,start,end,value=jobs[i-1]
        include=value+dp[prev[i-1]];exclude=dp[i-1]
        dp[i]=max(include,exclude)
        if trace:print(f'{name}: compatible prefix={prev[i-1]}, include={include}, exclude={exclude}, best={dp[i]}')
    selected=[];i=n
    while i>0:
        if jobs[i-1][3]+dp[prev[i-1]]>dp[i-1]:
            selected.append(jobs[i-1][0]);i=prev[i-1]
        else:i-=1
    return dp[n],list(reversed(selected)),dp
if __name__=='__main__':
    jobs=[('J1',1,3,20),('J2',2,5,50),('J3',4,6,30),('J4',6,8,40),('J5',5,9,60),('J6',8,10,30),('J7',9,11,50),('J8',11,13,40)]
    print('Task 6 official dataset')
    print('Result:',weighted_schedule(jobs,True)[:2])
    print('Adversarial dataset:')
    challenge=[('A',0,10,100),('B',0,2,30),('C',2,4,30),('D',4,6,30),('E',6,8,30),('F',8,10,30)]
    print('Result:',weighted_schedule(challenge,True)[:2])
