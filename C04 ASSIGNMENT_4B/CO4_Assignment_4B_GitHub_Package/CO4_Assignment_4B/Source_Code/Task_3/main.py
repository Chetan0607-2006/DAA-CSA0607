# Task 3: Directed graph routing, negative edges/cycles and all-pairs matrices.
V=list('ABCDEFGH')
E=[('A','B',4),('A','C',8),('B','C',3),('B','D',7),('C','D',2),('C','E',6),('D','E',2),('D','F',5),('E','F',1),('E','G',7),('F','G',2),('G','H',3),('C','H',20)]
def dijkstra(edges,source='A'):
    import heapq
    if any(w<0 for _,_,w in edges):raise ValueError('Dijkstra requires nonnegative weights')
    adj={v:[] for v in V}
    for a,b,w in edges:adj[a].append((b,w))
    d={v:float('inf') for v in V};prev={v:None for v in V};d[source]=0;pq=[(0,source)];order=[]
    while pq:
        cost,u=heapq.heappop(pq)
        if cost!=d[u]:continue
        order.append(u)
        for v,w in adj[u]:
            if cost+w<d[v]:d[v]=cost+w;prev[v]=u;heapq.heappush(pq,(d[v],v))
    return d,prev,order
def bellman(edges,source='A'):
    d={v:float('inf') for v in V};prev={v:None for v in V};d[source]=0
    for k in range(len(V)-1):
        changed=False
        for u,v,w in edges:
            if d[u]!=float('inf') and d[u]+w<d[v]:d[v]=d[u]+w;prev[v]=u;changed=True
        print('pass',k+1,'distances',d)
        if not changed:break
    if any(d[u]!=float('inf') and d[u]+w<d[v] for u,v,w in edges):raise ValueError('reachable negative cycle')
    return d,prev
def floyd(edges):
    n=len(V);d=[[0 if i==j else float('inf') for j in range(n)] for i in range(n)]
    for u,v,w in edges:d[V.index(u)][V.index(v)]=min(d[V.index(u)][V.index(v)],w)
    for k in range(n):
        for i in range(n):
            for j in range(n):d[i][j]=min(d[i][j],d[i][k]+d[k][j])
    return d
def warshall(edges):
    n=len(V);r=[[i==j for j in range(n)] for i in range(n)]
    for u,v,_ in edges:r[V.index(u)][V.index(v)]=True
    for k in range(n):
        for i in range(n):
            for j in range(n):r[i][j]|=r[i][k] and r[k][j]
    return r
def path(prev,dest):
    p=[]
    while dest is not None:p.append(dest);dest=prev[dest]
    return p[::-1]
if __name__=='__main__':
    d,p,order=dijkstra(E);print('Finalization',order)
    for v in V:print('route',v,d[v],path(p,v),'predecessor',p[v])
    neg=E+[('F','B',-12)] # creates negative cycle B-C-D-E-F-B
    print('Negative edge prediction: may create a negative cycle; Dijkstra rejected')
    try:dijkstra(neg)
    except ValueError as e:print('Expected Dijkstra guard:',e)
    try:bellman(neg)
    except ValueError as e:print('Expected Bellman-Ford detection:',e)
    # separate acyclic negative edge, suitable for Bellman-Ford comparison
    safe=E+[('A','G',-1)]
    print('Negative edge without cycle:',bellman(safe)[0]);print('Floyd distances')
    for row in floyd(E):print(row)
    print('Warshall reachability')
    for row in warshall(E):print([int(x) for x in row])
