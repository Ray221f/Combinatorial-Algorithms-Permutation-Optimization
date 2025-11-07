'''
Members of the group: Hao Guo, Zirui Fang
The approximation factor of Algorithm 1 is 2, more justifications will be written in the report.
The complexity of my algorithm is O(|V| + |E|), more complexity analysis will be written in the report.
'''
# Standard input of graph
def read_graph_from_input():
    # The first line with n, m
    first_line = input().strip()
    n, m = map(int, first_line.split())

    # The following m lines with u, v
    E = []
    for _ in range(m):
        edge_line = input().strip()
        u, v = map(int, edge_line.split())
        E.append((u, v))

    return E, n

# O(|V| + |E|) implementation of the approximation algorithm for vertex cover
def vertex_cover_approximation(E, n):
    # Initialize cover and working edge set
    cover = [0] * n 
    edges_list = E.copy()
    # Use a set for fast lookup of covered vertices
    covered = set()
    # Set an index to deal with remaining_edges list
    edge_index = 0    
    
    # Process edges, pick an arbitrary edge, but we'll pick the first one, this ensures the same output for the same input
    while edge_index < len(edges_list):
        u, v = edges_list[edge_index]
        edge_index += 1
        # Remove all edges incident to u or v
        if u not in covered and v not in covered:
            # Add both endpoints to cover
            cover[u] = 1
            cover[v] = 1
            covered.add(u)
            covered.add(v)
    
    cover_size = sum(cover) 
    return cover_size, cover

def main():
    E, n = read_graph_from_input()
    cover_size, cover = vertex_cover_approximation(E, n)
    print(f"({cover_size}, {cover})")

# Run the program
main()
