import numpy as np

n = np.random.randint(20, 51)
adj = np.random.rand(n, n).round().astype(int)

print(f"n = {n}")
print(adj)

# Edge table: edges[e] = [end1, end2, used_flag]
edges = []
# Vertex table: incident[v] = list of edge ids incident on v
incident = [[] for _ in range(n)]
for i in range(n):
    for j in range(n):
        if adj[i, j]:
            e = len(edges)
            edges.append([i, j, False])
            incident[i].append(e)

N = [0] * n   # N[v]: index of the current item in v's list
P = []        # the resulting path (list of edge ids)

def trace(s, P):
    v = s
    while N[v] < len(incident[v]):          # N(v) points to an edge
        e = incident[v][N[v]]
        if edges[e][2]:                     # edge is used
            N[v] += 1                       # move to next item in the list
        else:
            edges[e][2] = True              # mark e as used
            P.append(e)                     # add e to the end of P
            u = edges[e][1]
            v = u

start_vertex = np.random.randint(0, n)
trace(start_vertex, P)

print("Path (as vertex pairs) starting from vertex", start_vertex, ":", [(edges[e][0], edges[e][1]) for e in P])
print("Path Length is:", len(P))

def connected(adj):
    A = adj.copy()
    Ak = adj.copy()
    B = adj.copy()
    for _ in range(2, n + 1):
        Ak = ((Ak @ A) > 0).astype(int)   # clip to 0/1 to avoid unnecessarily large numbers
        B = B + Ak

    path = (B > 0).astype(int)

    # Connected if every vertex reaches every other vertex (ignore the diagonal)
    off_diag = path[~np.eye(n, dtype=bool)]
    connected = off_diag.all()

    print("Connected:", connected)
    
connected(adj)