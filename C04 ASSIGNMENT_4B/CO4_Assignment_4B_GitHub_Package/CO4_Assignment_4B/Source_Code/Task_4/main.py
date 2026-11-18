# Task 4: Two assembly lines with predecessor reconstruction.
def schedule(a,t,entry,exit_):
    n=len(a[0]);f=[[0]*n for _ in range(2)];pred=[[-1]*n for _ in range(2)]
    for line in range(2):f[line][0]=entry[line]+a[line][0]
    for j in range(1,n):
        for line in range(2):
            stay=f[line][j-1]+a[line][j]
            change=f[1-line][j-1]+t[1-line][j-1]+a[line][j]
            if stay<=change:f[line][j]=stay;pred[line][j]=line;choice='stay'
            else:f[line][j]=change;pred[line][j]=1-line;choice='transfer'
            print('station',j+1,'line',line+1,'stay',stay,'transfer',change,'chosen',choice)
    last=min(range(2),key=lambda line:f[line][-1]+exit_[line]);total=f[last][-1]+exit_[last]
    route=[last]
    for j in range(n-1,0,-1):last=pred[last][j];route.append(last)
    route=[x+1 for x in route[::-1]]
    return total,route,[(j+1,route[j-1],route[j]) for j in range(1,n) if route[j]!=route[j-1]]
if __name__=='__main__':
    a=[[7,9,3,4,8,4],[8,5,6,4,5,7]];t=[[2,3,1,3,4],[2,1,2,2,1]];entry=[2,4];exit_=[3,2]
    print('BASE',schedule(a,t,entry,exit_))
    tt=[x[:] for x in t];tt[0][1]+=20
    print('PREDICTION: increasing L1 station2 -> L2 station3 transfer cost may change route; optimum cannot decrease')
    print('TRANSFER CHANGE',schedule(a,tt,entry,exit_))
    aa=[x[:] for x in a];aa[0][2]+=20
    print('PREDICTION: slowing L1 station3 may move job to line 2; optimum cannot decrease')
    print('DISRUPTION',schedule(aa,t,entry,exit_))
