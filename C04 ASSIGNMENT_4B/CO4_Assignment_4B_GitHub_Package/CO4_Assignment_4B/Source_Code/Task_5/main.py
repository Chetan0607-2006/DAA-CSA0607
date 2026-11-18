# Task 5: Three MST algorithms with edge selection traces.
V=list('ABCDEF')
E=[('A','B',4),('A','C',2),('B','C',1),('B','D',5),('C','D',8),('C','E',10),('D','E',2),('D','F',6),('E','F',3),('B','F',9)]
class DSU:
    def __init__(self):self.p={v:v for v in V}
    def find(self,x):
        while x!=self.p[x]:self.p[x]=self.p[self.p[x]];x=self.p[x]
        return x
    def union(self,a,b):
        a=self.find(a);b=self.find(b)
        if a==b:return False
        self.p[b]=a;return True
def kruskal(edges):
    ds=DSU();chosen=[]
    for u,v,w in sorted(edges,key=lambda e:(e[2],e[0],e[1])):
        if ds.union(u,v):chosen.append((u,v,w));print('Kruskal select',chosen[-1])
    return chosen
def prim(edges):
    visited={'A'};chosen=[]
    while len(visited)<len(V):
        candidates=[(w,u,v) for u,v,w in edges if (u in visited)!=(v in visited)]
        if not candidates:raise ValueError('disconnected')
        w,u,v=min(candidates);chosen.append((u,v,w));visited.add(u);visited.add(v);print('Prim select',chosen[-1])
    return chosen
def boruvka(edges):
    ds=DSU();chosen=[]
    while len(chosen)<len(V)-1:
        cheapest={}
        for u,v,w in edges:
            a,b=ds.find(u),ds.find(v)
            if a==b:continue
            for component in (a,b):
                if component not in cheapest or (w,u,v)<(cheapest[component][2],cheapest[component][0],cheapest[component][1]):cheapest[component]=(u,v,w)
        progress=False
        for u,v,w in cheapest.values():
            if ds.union(u,v):chosen.append((u,v,w));progress=True;print('Boruvka select',chosen[-1])
        if not progress:raise ValueError('disconnected')
    return chosen
def run(edges):
    for method in (kruskal,prim,boruvka):
        chosen=method(edges);print(method.__name__,'edges',chosen,'total',sum(w for _,_,w in chosen))
if __name__=='__main__':
    print('BASE');run(E)
    print('TIED WEIGHTS');run([(u,v,2 if w in (1,2,3) else w) for u,v,w in E])
