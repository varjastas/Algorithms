def find_shortest():
    graph, costs, parents = create_graphs()
    processed = []
    node = find_lowest_code_node(costs, processed)
    while node is not "":
        cost = costs[node]
        neighbors = graph[node]
        for n in neighbors.keys():
            new_cost = cost + neighbors[n]
            if costs[n] > new_cost:
                costs[n] = new_cost
                parents[n] = node
        
        processed.append(node)
        node = find_lowest_code_node(costs, processed)
    return parents
def create_graphs():
    graph = {}
    graph["a"] = {}
    graph["a"]["fin"] = 1
    graph["b"] = {}
    graph["b"]["a"] = 3
    graph["b"]["fin"] = 5
    graph["fin"] = {}
          
    infinity = float("inf")
    costs = {}
    costs["a"] = 6
    costs["b"] = 2
    costs["fin"] = infinity
          
    parents = {}
    parents["a"] = "start"
    parents["b"] = "start"
    parents["fin"] = None

    return graph, costs, parents

def find_lowest_code_node(costs : dict, processed):
    min_cost = float("inf")
    min_node = ""

    for node in costs:
        value = costs[node]
        if value < min_cost and node not in processed:
            min_cost = value
            min_node = node
    return min_node

def tests():
    print(find_shortest())

tests()