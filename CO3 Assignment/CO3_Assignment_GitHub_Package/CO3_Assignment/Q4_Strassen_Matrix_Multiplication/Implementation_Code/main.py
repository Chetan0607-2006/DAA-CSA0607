import random,time

def conventional(A,B):
    n=len(A);C=[[0]*n for _ in range(n)];count=0
    for i in range(n):
        for k in range(n):
            for j in range(n):C[i][j]+=A[i][k]*B[k][j];count+=1
    return C,count

def add(A,B,sign=1):return [[x+sign*y for x,y in zip(r,s)] for r,s in zip(A,B)]
def split(A):
    m=len(A)//2
    return [ [r[:m] for r in A[:m]], [r[m:] for r in A[:m]], [r[:m] for r in A[m:]], [r[m:] for r in A[m:]] ]
def join(a,b,c,d):return [x+y for x,y in zip(a,b)]+[x+y for x,y in zip(c,d)]
def strassen(A,B,threshold=2):
    n=len(A)
    if n<=threshold:return conventional(A,B)
    a,b,c,d=split(A);e,f,g,h=split(B)
    args=[(add(a,d),add(e,h)),(add(c,d),e),(a,add(f,h,-1)),(d,add(g,e,-1)),(add(a,b),h),(add(c,a,-1),add(e,f)),(add(b,d,-1),add(g,h))]
    results=[strassen(x,y,threshold) for x,y in args]
    p,q,r,s,t,u,v=[z[0] for z in results];count=sum(z[1] for z in results)
    return join(add(add(add(p,s),v),t,-1),add(r,t),add(q,s),add(add(add(p,q,-1),r),u)),count

def pad(A,n):return [row+[0]*(n-len(row)) for row in A]+[[0]*n for _ in range(n-len(A))]
def multiply(A,B):
    n=len(A);size=1<<(n-1).bit_length()
    C,count=strassen(pad(A,size),pad(B,size))
    return [row[:n] for row in C[:n]],count
if __name__=='__main__':
    rng=random.Random(42)
    for n in (2,3,4,8,16):
        A=[[rng.randint(-5,5) for _ in range(n)] for _ in range(n)]
        B=[[rng.randint(-5,5) for _ in range(n)] for _ in range(n)]
        t=time.perf_counter();x,c=conventional(A,B);ms1=(time.perf_counter()-t)*1000
        t=time.perf_counter();y,d=multiply(A,B);ms2=(time.perf_counter()-t)*1000
        assert x==y
        print('size=',n,'products conventional/Strassen=',c,d,'ms=',round(ms1,3),round(ms2,3))
