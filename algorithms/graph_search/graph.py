# https://www.python-course.eu/graphs_python.php
# set up graph by detailing nodes and edges

# Graph = dict
# key = graph nodes
# value = list of edges

graph = { "a" : ["c"],
          "b" : ["c", "e"],
          "c" : ["a", "b", "d", "e"],
          "d" : ["c"],
          "e" : ["c", "b"],
          "f" : []
        }

# function to list all edges of all nodes
def show_edges(graph):
    edges = []
    # cycle through all nodes of graph
    for node in graph:
        # cycle through list of edges for each node
        for neighbour in graph[node]:
            # add node with list of edges to array
            edges.append((node, neighbour))
    print("i am edges", edges)
    return(edges)

# function to find isolated nodes
def find_isolated_nodes(graph):
    isolated = []
    # cycle through all nodes in graphs
    for node in graph:
        # if there are no nodes for this value
        if not graph[node]:
            # add to isolated list
            isolated += node
    print("i am isolated node", isolated)
    return(isolated)

show_edges(graph)
find_isolated_nodes(graph)
