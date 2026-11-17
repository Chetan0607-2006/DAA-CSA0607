import math,random,time

def brute(points,stats):
    best=(float('inf'),None)
    for i in range(len(points)):
        for j in range(i+1,len(points)):
            stats[0]+=1;d=math.dist(points[i],points[j])
            if d<best[0]:best=(d,(points[i],points[j]))
    return best

def closest(points,stats):
    px=sorted(points);py=sorted(points,key=lambda p:p[1])
    def solve(px,py):
        n=len(px)
        if n<=3:return brute(px,stats)
        m=n//2;mid=px[m][0];left=px[:m];right=px[m:];ids=set(left)
        ly=[p for p in py if p in ids];ry=[p for p in py if p not in ids]
        a=solve(left,ly);b=solve(right,ry);best=min((a,b),key=lambda t:t[0]);d=best[0]
        strip=[p for p in py if abs(p[0]-mid)<d]
        for i in range(len(strip)):
            for j in range(i+1,min(i+8,len(strip))):
                if strip[j][1]-strip[i][1]>=d:break
                stats[0]+=1;dist=math.dist(strip[i],strip[j])
                if dist<d:d=dist;best=(d,(strip[i],strip[j]))
        return best
    return solve(px,py)
if __name__=='__main__':
    rng=random.Random(42)
    for n in (8,32,128,512):
        points=rng.sample([(i,j) for i in range(100) for j in range(100)],n)
        c=[0];t=time.perf_counter();a=brute(points,c);ms1=(time.perf_counter()-t)*1000
        d=[0];t=time.perf_counter();b=closest(points,d);ms2=(time.perf_counter()-t)*1000
        assert abs(a[0]-b[0])<1e-9
        print('n=',n,'distance=',round(b[0],4),'distance checks=',c[0],d[0],'ms=',round(ms1,3),round(ms2,3))
