'''
Members of the group: Hao Guo, Zirui Fang
'''
import heapq
import math
# We cite dijkstra_queue(graph, s) code from Shortest Path Algorithms.py, which is provided by professor Pablo Ezequiel TERLISKY on Moodle
def dijkstra_queue(graph, s):
    n = len(graph)
    distance = [float('inf')]*n
    parent = [-1]*n
    distance[s]=0
    parent[s]=s
    s_set = set()
    process_queue = []
    heapq.heappush(process_queue, (0,s))
    while process_queue:
        v = heapq.heappop(process_queue)[1]
        if not v in s_set:
            s_set.add(v)
            for (u,w,_) in graph[v]:
                if distance[v]+w < distance[u]:
                    distance[u] = distance[v]+w
                    parent[u] = v
                    heapq.heappush(process_queue,(distance[u],u))
    return (distance, parent)

# We cite dijkstra_vector(graph, s) code from Shortest Path Algorithms.py, which is provided by professor Pablo Ezequiel TERLISKY on Moodle
def dijkstra_vector(graph, s):
    n = len(graph)
    distance = [float('inf')]*n
    parent = [-1]*n
    distance[s]=0
    parent[s]=s
    s_set = set()
    reachable_remaining = True
    while len(s_set)<n and reachable_remaining:
        min_dist = float('inf')
        v = None
        for i in range(n):
            if distance[i]<min_dist and (i not in s_set):
                min_dist = distance[i]
                v = i
        if min_dist == float('inf'):
            reachable_remaining = False
        else:
            s_set.add(v)
            for (u,w,_) in graph[v]:
                if distance[v]+w < distance[u]:
                    distance[u] = distance[v]+w
                    parent[u] = v
    return (distance, parent)

# Decide dense or sparse
def select_dijkstra_algorithm(n, m):
    V_squared = n * n
    if n > 1:
        E_log_V = m * math.log2(n) 
    else:
        E_log_V = 0
    if V_squared <= E_log_V:
        return dijkstra_vector
    else:
        return dijkstra_queue
    
# We cite generate_adj_list_from_edge_list code from Shortest Path Algorithms.py, which is provided by professor Pablo Ezequiel TERLISKY on Moodle
def generate_adj_list_from_edge_list(n, E, is_digraph=True):
    #Initialization
    G_l = []
    for _ in range(n):
        G_l.append([])
    #Adding all the edges
    for (u,v,w,p) in E:
        G_l[u].append((v,w,p))
        if not is_digraph:
            G_l[v].append((u,w,p))
    return G_l

# Standard input of graph
def read_graph_from_input():
    # The first line with n, m, s, t
    first_line = input().strip()
    n, m, s, t = map(int, first_line.split())

    # The following m lines with u, v, w, p
    E = []
    for _ in range(m):
        edge_line = input().strip()
        u, v, w, p = map(int, edge_line.split())
        E.append((u, v, w, p))

    return E, s, t, n

# Build the shortest path from s to u
def build_path_s_to_u(parent, u):
    path = []
    while parent[u] != u:
        path.append(u)
        u = parent[u]
    path.append(u)
    path.reverse()
    return path


# Build the shortest path from v to t
def build_path_v_to_t(parent, v):
    path = []
    while parent[v] != v:
        path.append(v)
        v = parent[v]
    path.append(v)
    return path

def main():
    E, s, t, n = read_graph_from_input()
    
    # Select best dijkstra implementation
    dijkstra = select_dijkstra_algorithm(n, len(E))
    
    # Construct a graph by ignoring special edges
    no_special_edges = [edge for edge in E if edge[3] == 0]
    no_special_edges_Graph = generate_adj_list_from_edge_list(n, no_special_edges, is_digraph=True)

    # Construct a reverse graph by ignoring special edges
    rev_no_special_edges = [(edge[1],edge[0],edge[2],edge[3]) for edge in no_special_edges]
    rev_no_special_edges_Graph = generate_adj_list_from_edge_list(n, rev_no_special_edges, is_digraph=True)
    
    # Compute distances from s to u and path parents from s to u
    dist_s_to_u, parent_s_to_u = dijkstra(no_special_edges_Graph, s)

    # Compute distances from v to t and path parents from v to t
    dist_v_to_t, parent_v_to_t = dijkstra(rev_no_special_edges_Graph, t)
    
    # Iterate through all edges to find special edges (p = 1)
    dist_with_one_specialEdges = float('inf')
    path_with_one_specialEdges = None
    for u, v, w, p in E:
        if p == 1:
            # Check if there exists a path s->u and v->t
            if dist_s_to_u[u] != float('inf') and dist_v_to_t[v] != float('inf'):
                # Calculate total distance: s->u + special edge + v->t
                current_dist = dist_s_to_u[u] + w + dist_v_to_t[v]
                # Update distance if current distance is better
                if current_dist < dist_with_one_specialEdges:
                    dist_with_one_specialEdges = current_dist                        
                    # Combine paths: s->u + special edge +v->t 
                    path_s_to_u = build_path_s_to_u(parent_s_to_u, u)
                    path_v_to_t = build_path_v_to_t(parent_v_to_t, v)
                    path_with_one_specialEdges = path_s_to_u + [v] + path_v_to_t[1:]
    
    if dist_with_one_specialEdges == float('inf'):
        print("infeasible")
    else:
        print(f"({dist_with_one_specialEdges},{path_with_one_specialEdges})")

# Run the program
main()
