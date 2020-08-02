import math
# graph = {'a':{'b':10, 'c':3}, 'b':{'d':2, 'c':1}, 'c':{'b':4, 'e':2, 'd':8}, 'd':{'e':7}, 'e':{'d':9}}
graph = {'a':{'b':1, 'd':4.47, 'e':5.56, 'g':8.06, 'f':10}, 
         'b':{'a':1, 'd':3.61, 'e':5, 'g':7.62, 'c':5.1}, 
         'c':{'b':5.1, 'd':2.24, 'f':5.39, 'e':3.61},
         'd':{'b':3.61, 'c':2.24, 'a':4.47, 'e':2, 'f':5.66},
         'e':{'f':4.47, 'g':3, 'c':3.61, 'd':2, 'a':5.56, 'b':4.47},
         'f':{'h':2, 'c':5.39, 'd':5.66, 'g':4.12, 'e':4.47, 'a':10},
         'g':{'h':4.12, 'f':4.12, 'e':3, 'a':8.06, 'b':7.62},
         'h':{'f':2, 'g':4.12}
        }

# graph = {'a':[{'b':1, 'd':4.47, 'e':5.56, 'g':8.06, 'f':10}], 
#     'b':[{'a':1, 'd':3.61, 'e':5, 'g':7.62, 'c':5.1}], 
#     'c':[{'b':5.1, 'd':2.24, 'f':5.39, 'e':3.61}],
#     'd':[{'b':3.61, 'c':2.24, 'a':4.47, 'e':2, 'f':5.66}],
#     'e':[{'f':4.47, 'g':3, 'c':3.61, 'd':2, 'a':5.56, 'b':4.47}],
#     'f':[{'h':2, 'c':5.39, 'd':5.66, 'g':4.12, 'e':4.47, 'a':10}],
#     'g':[{'h':4.12, 'f':4.12, 'e':3, 'a':8.06, 'b':7.62}],
#     'h':[{'f':2, 'g':4.12}]
# }

def dijkstra(graph, start, goal):
    shortest_distance = {}
    predecessor = {}
    unseenNodes = graph
    infinity = math.inf
    path = []

    for node in unseenNodes:
        shortest_distance[node] = infinity
    shortest_distance[start] = 0

    while unseenNodes:
        minNode = None
        for node in unseenNodes:
            if minNode is None:
                minNode = node
            elif shortest_distance[node] < shortest_distance[minNode]:
                minNode = node
            
        for childNode, weight in graph[minNode].items():
            if weight + shortest_distance[minNode] < shortest_distance[childNode]:
                shortest_distance[childNode] = weight + shortest_distance[minNode]
                predecessor[childNode] = minNode

        unseenNodes.pop(minNode)

    currentNode = goal

    while currentNode != start:
        try: 
            path.insert(0, currentNode)
            currentNode = predecessor[currentNode]
        except KeyError:
            print("Path not reachable")
            break
    path.insert(0, start)
    if shortest_distance[goal] != infinity:
        print("Shortest distance is " + str(shortest_distance[goal]))
        print("Path is " + str(path))
        
    points = []
    for i in path:
        print(path[str(i)])
        #points.append(path[i])
    print(points)
    

dijkstra(graph, 'c', 'g')