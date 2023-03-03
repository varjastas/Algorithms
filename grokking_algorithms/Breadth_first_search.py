from collections import deque

def breadth_first_search(graph : dict, name, searched_element):
    '''
    graph type : dict
    rtype : int
    '''
    search_queue = deque()
    search_queue += graph[name]
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if not person in searched:
            if person == searched_element:
                print(f"Person {person} is mango seller")
                return True
            else: 
                search_queue += graph[person]
                searched.append(person)
                

def create_graph():
    # Created Dict that will store our graph
    graph = {}
    # Creating nodes and edges between them(key: value)
    # This is a directed graph, because we`re pointing from one node to another
    graph["you"] = ["alice", "bob", "claire"]
    graph["bob"] = ["anuj", "peggy"]
    graph["alice"] = ["peggy"]
    graph["claire"] = ["thom", "jonny"]
    graph["anuj"] = []
    graph["peggy"] = []
    graph["thom"] = []
    graph["jonny"] = []
    return graph

def tests():
    graph = create_graph()
    assert breadth_first_search(graph, "you", "anuj") == True

tests()

