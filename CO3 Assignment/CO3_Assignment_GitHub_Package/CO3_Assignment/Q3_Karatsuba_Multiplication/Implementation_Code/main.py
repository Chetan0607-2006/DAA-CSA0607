import random,time

def schoolbook(a,b):
    # Digit multiplication, count single-digit products
    x=list(map(int,str(a)[::-1]));y=list(map(int,str(b)[::-1]));z=[0]*(len(x)+len(y));count=0
    for i,u in enumerate(x):
        for j,v in enumerate(y):z[i+j]+=u*v;count+=1
    for k in range(len(z)-1):z[k+1]+=z[k]//10;z[k]%=10
    return sum(d*10**i for i,d in enumerate(z)),count

def karatsuba(a,b,stats):
    if a<10 or b<10:
        stats[0]+=1;return a*b
    n=max(len(str(a)),len(str(b)));m=n//2;base=10**m
    ah,al=divmod(a,base);bh,bl=divmod(b,base)
    z0=karatsuba(al,bl,stats);z2=karatsuba(ah,bh,stats)
    z1=karatsuba(al+ah,bl+bh,stats)-z0-z2
    return z2*base**2+z1*base+z0

if __name__=='__main__':
    rng=random.Random(42)
    for digits in (2,4,8,16,32,64):
        a=rng.randrange(10**(digits-1),10**digits);b=rng.randrange(10**(digits-1),10**digits)
        t=time.perf_counter();v,c=schoolbook(a,b);school_ms=(time.perf_counter()-t)*1000
        st=[0];t=time.perf_counter();w=karatsuba(a,b,st);kara_ms=(time.perf_counter()-t)*1000
        assert v==w==a*b
        print('digits=',digits,'school digit products=',c,'karatsuba leaf products=',st[0],'time ms=',round(school_ms,3),round(kara_ms,3))
