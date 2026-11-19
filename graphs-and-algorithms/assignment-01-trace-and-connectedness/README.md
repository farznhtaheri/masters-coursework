# Trace a Path in a Random Directed Graph & Check Strong Connectivity

This program generates a random directed graph, traces a trail through it by repeatedly following unused edges, and checks whether the graph is strongly connected.

## What it does

1. **Generates a random graph.** It picks a vertex count `n` between 20 and 50 and builds a random 0/1 adjacency matrix.
2. **Builds an edge table and incidence lists.** Each edge is stored as `[end1, end2, used_flag]`, and each vertex keeps a list of its outgoing edge IDs.
3. **Traces a path.** Starting from a random vertex, `trace` follows the next unused outgoing edge, marks it as used, and moves to its head. A pointer `N[v]` per vertex remembers where it left off in that vertex's list, so no edge is rescanned. It stops when the current vertex has no unused outgoing edges left.
4. **Checks connectivity.** `connected` computes reachability by taking powers of the adjacency matrix and reports whether every vertex can reach every other vertex.

## Requirements

- Python 3.8+
- NumPy

```bash
pip install numpy
```

## Usage

```bash
python HW1.py
```

Each run uses a new random graph, so the output differs every time. It prints:

- the number of vertices `n` and the adjacency matrix
- the traced path as a list of `(from, to)` vertex pairs, with its length
- whether the graph is connected (`True` / `False`)

## Example output

```
n = 36
[[0 0 1 ... 1 1 1]
 [0 0 0 ... 0 1 1]
 [1 1 0 ... 0 1 1]
 ...
 [1 0 0 ... 1 0 0]
 [0 0 0 ... 1 0 0]
 [1 0 0 ... 1 0 0]]
Path (as vertex pairs) starting from vertex 7 : [(8, 0), (0, 2), (2, 0), (0, 4), ...]
Path Length is: 148
Connected: True
```

## Complexity

Let `n` be the number of vertices and `m` the number of edges (`m ≤ n²`).

| Step | Time |
|------|------|
| Build edge table and incidence lists | O(n²) |
| `trace` | O(m), since each edge is used or skipped at most once |
| `connected` | O(n⁴), from n matrix multiplications of O(n³) each |
## Notes and limitations

- `trace` produces a **trail** (a walk that never reuses an edge). It does not guarantee that every edge is covered. In a general random graph it may stop anywhere.
- No random seed is set
