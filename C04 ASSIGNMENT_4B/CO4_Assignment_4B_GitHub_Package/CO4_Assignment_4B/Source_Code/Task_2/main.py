# Task 2: Fractional greedy, 0/1 ratio heuristic, exact 0/1 dynamic programming.
def fractional(items,cap):
    selected=[];value=0;ops=0
    for name,w,v in sorted(items,key=lambda x:x[2]/x[1],reverse=True):
        ops+=1;fraction=min(1,cap/w)
        if fraction>0:selected.append((name,fraction));value+=v*fraction;cap-=w*fraction
    return value,selected,ops
def ratio_01(items,cap):
    chosen=[];value=0
    for name,w,v in sorted(items,key=lambda x:x[2]/x[1],reverse=True):
        if w<=cap:chosen.append(name);cap-=w;value+=v
    return value,chosen
def exact_01(items,cap):
    n=len(items);dp=[[0]*(cap+1) for _ in range(n+1)];ops=0
    for i,(_,w,v) in enumerate(items,1):
        for c in range(cap+1):
            ops+=1;dp[i][c]=dp[i-1][c]
            if w<=c:dp[i][c]=max(dp[i][c],v+dp[i-1][c-w])
    chosen=[];c=cap
    for i in range(n,0,-1):
        if dp[i][c]!=dp[i-1][c]:chosen.append(items[i-1][0]);c-=items[i-1][1]
    return dp[n][cap],chosen[::-1],ops,(n+1)*(cap+1)
if __name__=='__main__':
    for label,items,cap in [('normal',[('A',10,60),('B',20,100),('C',30,120)],50),('counterexample',[('A',10,60),('B',20,100),('C',30,120)],50),('exact-match',[('P',2,12),('Q',3,20),('R',4,25)],5)]:
        print('\n',label,'capacity',cap,'items',items)
        print('Fractional:',fractional(items,cap))
        print('Ratio-based 0/1 (not guaranteed):',ratio_01(items,cap))
        print('Exact 0/1:',exact_01(items,cap))
