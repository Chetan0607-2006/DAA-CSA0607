# Task 5: Dijkstra, Bellman-Ford, Floyd-Warshall
from math import inf
V=['A','B','C','D','E']
E=[('A','B',4),('A','C',7),('B','C',2),('B','D',6),('C','D',1),('D','E',3),('C','E',8)]
def dijkstra(vertices,edges,start):
    if any(w<0 for _,_,w in edges):raise ValueError('Dijkstra requires nonnegative weights')
    dist={v:inf for v in vertices};prev={v:None for v in vertices};dist[start]=0
    pending=set(vertices)
    while pending:
        u=min(pending,key=lambda v:dist[v]);pending.remove(u)
        if dist[u]==inf:break
        for a,b,w in edges:
            if a==u and b in pending and dist[u]+w<dist[b]:
                dist[b]=dist[u]+w;prev[b]=u
    return dist,prev
def bellman_ford(vertices,edges,start):
    dist={v:inf for v in vertices};dist[start]=0
    for _ in range(len(vertices)-1):
        changed=False
        for u,v,w in edges:
            if dist[u]!=inf and dist[u]+w<dist[v]:dist[v]=dist[u]+w;changed=True
        if not changed:break
    cycle=any(dist[u]!=inf and dist[u]+w<dist[v] for u,v,w in edges)
    return dist,cycle
def floyd(vertices,edges):
    d={i:{j:(0 if i==j else inf) for j in vertices} for i in vertices}
    for u,v,w in edges:d[u][v]=min(d[u][v],w)
    for k in vertices:
        for i in vertices:
            for j in vertices:d[i][j]=min(d[i][j],d[i][k]+d[k][j])
    return d
if __name__=='__main__':
    print('Task 5 Dijkstra:',dijkstra(V,E,'A'))
    print('Bellman-Ford:',bellman_ford(V,E,'A'))
    print('Floyd from A:',floyd(V,E)['A'])
