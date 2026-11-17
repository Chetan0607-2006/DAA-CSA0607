import random

def merge_sort(a, stats, depth=1):
    stats['merge_depth']=max(stats['merge_depth'],depth)
    if len(a)<2:return a[:]
    m=len(a)//2;l=merge_sort(a[:m],stats,depth+1);r=merge_sort(a[m:],stats,depth+1)
    out=[];i=j=0
    while i<len(l) and j<len(r):
        stats['merge_comparisons']+=1
        if l[i]<=r[j]:out.append(l[i]);i+=1
        else:out.append(r[j]);j+=1
    return out+l[i:]+r[j:]

def quick_sort(a, stats, depth=1):
    stats['quick_depth']=max(stats['quick_depth'],depth)
    if len(a)<2:return a[:]
    pivot=a[-1];less=[];equal=[];greater=[]
    for x in a:
        stats['quick_comparisons']+=1
        if x<pivot:less.append(x)
        elif x>pivot:greater.append(x)
        else:equal.append(x)
    stats['partitions'].append((len(less),len(equal),len(greater)))
    return quick_sort(less,stats,depth+1)+equal+quick_sort(greater,stats,depth+1)

def test(a):
    s={'merge_depth':0,'quick_depth':0,'merge_comparisons':0,'quick_comparisons':0,'partitions':[]}
    m=merge_sort(a,s);q=quick_sort(a,s)
    assert m==q==sorted(a)
    print('n=',len(a),'merge depth=',s['merge_depth'],'quick depth=',s['quick_depth'],'comparisons=',s['merge_comparisons'],s['quick_comparisons'])
    print('first 5 partition sizes:',s['partitions'][:5])
if __name__=='__main__':
    test([7,2,9,1,5,3,8]);test(list(range(64)));test(random.Random(42).sample(range(1000),64))
