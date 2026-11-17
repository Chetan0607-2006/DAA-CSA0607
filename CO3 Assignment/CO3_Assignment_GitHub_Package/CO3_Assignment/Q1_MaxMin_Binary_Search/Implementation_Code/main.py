import random

def minmax(a, count):
    if len(a) == 1: return a[0], a[0]
    if len(a) == 2:
        count[0] += 1
        return (a[0],a[1]) if a[0]<a[1] else (a[1],a[0])
    mid=len(a)//2
    lmin,lmax=minmax(a[:mid],count)
    rmin,rmax=minmax(a[mid:],count)
    count[0]+=2
    return min(lmin,rmin),max(lmax,rmax)

def binary_search(a,target):
    lo,hi,comparisons=0,len(a)-1,0
    while lo<=hi:
        mid=(lo+hi)//2
        comparisons+=1
        if a[mid]==target:return mid,comparisons
        if a[mid]<target:lo=mid+1
        else:hi=mid-1
    return -1,comparisons

if __name__=='__main__':
    for n in (8,16,32,64,128):
        a=list(range(n));random.Random(42).shuffle(a)
        c=[0];lo,hi=minmax(a,c)
        print('n=',n,'min=',lo,'max=',hi,'D&C comparisons=',c[0], 'naive=',2*(n-1))
        s=sorted(a)
        for target in (n//2,n+1):print(' binary target=',target,'index/comparisons=',binary_search(s,target))
