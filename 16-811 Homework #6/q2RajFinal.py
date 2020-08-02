import numpy as np
from matplotlib import pyplot as plt
import math
from q1Raj import grahamScan

def computeDistance(p1, p2):
    return round(math.sqrt(abs(p1[0] - p2[0]) **2 + 
                    abs(p1[1] - p2[1]) **2 ), 2)

def dijkstra(graph, start, goal, vertexKeyList):
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
    
    pointPath = []
    for node in path:
        pointPath.append(vertexKeyList[node])
    print("Path in Coordinates is " + str(pointPath))
    return pointPath

def createVertexKey(vertexList):
    vertexList = vertexList.tolist()
    start = 'a'
    keys = []
    temp = {}
    visible_edges = {}

    for i in range(len(vertexList)):
        temp[chr(ord(start) + i)] = vertexList[i]
        keys.append(chr(ord(start) + i))
    
    for key in keys:
        visible_edges[key] = {}

    return temp, visible_edges

def createVisibilityGraph(polygons, vertexList, vertexKeyList, visible_edges):

    edge_list = []
    poly_edge_list = []
    vertexList = vertexList.tolist()
    polygons = polygons.tolist()
    #print(polygons.tolist())

    # print(polygons)
    # for i in range(len(polygons)):
    #     for j in range(len(polygons)):
    #         if polygons[i] != polygons[j]:
    #             poly_edge_list.append([polygons[i], polygons[j]])
    # print(poly_edge_list)
    
    #create list of edges EXCLUSIVLEY WITHIN THE POLYGONS
    for poly in polygons:
        for i in range(len(poly)):
            for j in range(1, len(poly) - i):
                poly_edge_list.append([poly[i], poly[i+j]])

    # create list of all edges between nodes we'd like to test
    for i in range(len(vertexList)):
        #for j in range(len(vertex_list[:i+1])):
        for j in range(len(vertexList)):
            if vertexList[i] != vertexList[j]:
                edge_list.append([vertexList[i], vertexList[j]])

    def on_segment(p, q, r):
        '''Given three colinear points p, q, r, the function checks if 
        point q lies on line segment "pr"
        '''
        if (q[0] <= max(p[0], r[0]) and q[0] >= min(p[0], r[0]) and
            q[1] <= max(p[1], r[1]) and q[1] >= min(p[1], r[1])):
            return True
        return False

    def orientation(p, q, r):
        '''Find orientation of ordered triplet (p, q, r).
        The function returns following values
        0 --> p, q and r are colinear
        1 --> Clockwise
        2 --> Counterclockwise
        '''

        val = ((q[1] - p[1]) * (r[0] - q[0]) - 
                (q[0] - p[0]) * (r[1] - q[1]))
        if val == 0:
            return 0  # colinear
        elif val > 0:
            return 1   # clockwise
        else:
            return 2  # counter-clockwise

    def do_intersect(p1, q1, p2, q2):
        '''Main function to check whether the closed line segments p1 - q1 and p2 
        - q2 intersect'''
        o1 = orientation(p1, q1, p2)
        o2 = orientation(p1, q1, q2)
        o3 = orientation(p2, q2, p1)
        o4 = orientation(p2, q2, q1)

        if q1 == p2 or q1 == q2 or p1 == p2 or q2 == p1:
            return False

        # General case
        if (o1 != o2 and o3 != o4):
            return True

        # Special Cases
        # p1, q1 and p2 are colinear and p2 lies on segment p1q1
        if (o1 == 0 and on_segment(p1, p2, q1)):
            return True

        # p1, q1 and p2 are colinear and q2 lies on segment p1q1
        if (o2 == 0 and on_segment(p1, q2, q1)):
            return True

        # p2, q2 and p1 are colinear and p1 lies on segment p2q2
        if (o3 == 0 and on_segment(p2, p1, q2)):
            return True

        # p2, q2 and q1 are colinear and q1 lies on segment p2q2
        if (o4 == 0 and on_segment(p2, q1, q2)):
            return True

        return False # Doesn't fall in any of the above cases

    for path in edge_list:
        temp = {}
        for obstacle in poly_edge_list:
            intersection = do_intersect(path[0], path[1], obstacle[0], obstacle[1])     
            if intersection:
                break  
        else:
            letter1 = [l for l, point in vertexKeyList.items() if point == path[0]]
            letter2 = [l for l, point in vertexKeyList.items() if point == path[1]]
            temp[letter2[0]] = computeDistance(path[0], path[1])
            visible_edges[letter1[0]].update(temp)
            
    return visible_edges
    
def plotPolygons(polygons, N, start, goal, vertexList, vertexKeyList, pointPath):
  
    for shape in polygons:
        hull = grahamScan(shape, N)
        hull_x = hull[:,0]
        hull_y = hull[:,1]
        hull_x = np.append(hull_x, hull_x[0])
        hull_y = np.append(hull_y, hull_y[0])
        plt.scatter(shape[:,0], shape[:,1])
        plt.plot(hull_x, hull_y)
    
    for i in range(0, len(pointPath)-1):
      
        plt.plot([pointPath[i][0], pointPath[i+1][0]], 
        [pointPath[i][1], pointPath[i+1][1]], 'r-')
 
    

    plt.plot(start[0], start[1], 'ro')
    plt.plot(goal[0], goal[1], 'go')
    plt.grid()
    plt.show()

if __name__ == "__main__":
    
    # DOES NOT CURRENTLY WORK WITH POLYGONS THAT ARE NOT THE SAME SHAPE

    # p1 = np.array([[0.7, 4.06], [0.6, 2.01], [2.42, 2.95]])
    # p2 = np.array([[4.5, 2.59], [5.76, 1.95], [5.14, 3.81], [6.4, 3.17]])
    # p3 = np.array([[4.98, 4.87], [6.0, 5.0], [6.4, 5.95], [5.77,6.77], [4.75, 6.64], [4.36, 5.69]])
   
    
    p1 = np.array([[0, 1], [2, 4], [1, 6], [0,7]])
    p2 = np.array([[3, 4], [5, 4], [3, 2], [5,2]])
    p3 = np.array([[8, 2], [7, 1], [7, 8], [6,8]])
    p4 = np.array(([[3,3], [5, 3], [5,10], [3,10]]))
    # does not work
    #polygons = np.concatenate([[p1, p2]])
    # works
    polygons = np.array([p1, p2, p3, p4])
    start = [[0.0, 0.0]]
    goal = [[8.0,8.0]]
    vertexList = np.concatenate((start, p1, p2, p3, p4, goal))

 
    vertexKeyList, visible_edges = createVertexKey(vertexList)
    visibilityGraph = createVisibilityGraph(polygons, vertexList, vertexKeyList, visible_edges)
    start_node = [l for l, point in vertexKeyList.items() if point == start[0]]
    goal_node = [l for l, point in vertexKeyList.items() if point == goal[0]]
    pointPath = dijkstra(visibilityGraph, start_node[0], goal_node[0], vertexKeyList)
    plotPolygons(polygons, len(polygons), start[0], goal[0], vertexList, vertexKeyList, pointPath)