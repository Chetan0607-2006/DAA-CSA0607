import random,time,bisect

def mom_select(a,k):
    if len(a)<=5:return sorted(a)[k]
    medians=[sorted(a[i:i+5])[len(a[i:i+5])//2] for i in range(0,len(a),5)]
    pivot=mom_select(medians,len(medians)//2)
    lo=[x for x in a if x<pivot];eq=[x for x in a if x==pivot];hi=[x for x in a if x>pivot]
    if k<len(lo):return mom_select(lo,k)
    if k<len(lo)+len(eq):return pivot
    return mom_select(hi,k-len(lo)-len(eq))

def quickselect(a,k,mode='random',rng=None):
    rng=rng or random.Random(42);depth=0
    while True:
        depth+=1
        if len(a)==1:return a[0],depth
        pivot=a[0] if mode=='first' else rng.choice(a)
        lo=[x for x in a if x<pivot];eq=[x for x in a if x==pivot];hi=[x for x in a if x>pivot]
        if k<len(lo):a=lo
        elif k<len(lo)+len(eq):return pivot,depth
        else:k-=len(lo)+len(eq);a=hi

def subsets(a):
    sums=[0]
    for x in a:sums += [s+x for s in sums]
    return sums

def mitm(a,target):
    mid=len(a)//2;left=subsets(a[:mid]);right=sorted(subsets(a[mid:]))
    for s in left:
        i=bisect.bisect_left(right,target-s)
        if i<len(right) and right[i]==target-s:return True,len(left)+len(right)
    return False,len(left)+len(right)

def brute_subset(a,target):
    return target in subsets(a)
if __name__=='__main__':
    for n in (10,30,100):
        a=list(range(n));k=n//2
        print('selection n=',n,'median of medians=',mom_select(a,k),'quick random=',quickselect(a,k),'quick poor first=',quickselect(a,k,'first'))
    for n in (8,12,16,20):
        a=list(range(1,n+1));target=n*(n+1)//4
        answer,space=mitm(a,target)
        assert answer==brute_subset(a,target)
        print('subset n=',n,'target=',target,'found=',answer,'MITM stored sums=',space,'brute candidates=',2**n)
