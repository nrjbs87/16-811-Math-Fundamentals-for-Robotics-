import numpy as np
import random
import os
from q1Raj import grahamScan
from matplotlib import pyplot as plt
import math

def computeDistance(p1, p2):
    return round(math.sqrt(abs(p1[0] - p2[0]) **2 + 
                    abs(p1[1] - p2[1]) **2 ), 2)

def createVisibilityGraph(polygons, vertex_list):

    edge_list = []
    poly_edge_list = []

    # create list of edges EXCLUSIVLEY WITHIN THE POLYGONS
    for poly in polygons:
        for i in range(len(poly)):
            for j in range(1, len(poly) - i):
                poly_edge_list.append([poly[i], poly[i+j]])

    # create list of all edges between nodes we'd like to test
    for i in range(len(vertex_list)):
        #for j in range(len(vertex_list[:i+1])):
        for j in range(len(vertex_list)):
            if vertex_list[i] != vertex_list[j]:
                edge_list.append([vertex_list[i], vertex_list[j]])

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


    
    counter = 0 

    test = {}
    visible_edges = {}
    start = 'a'
    keys = []
    for i in range(len(vertex_list)):
        test[chr(ord(start) + i)] = vertex_list[i]
        keys.append(chr(ord(start) + i))
    print(test)
    
    for key in keys:
        visible_edges[key] = {}
    print(visible_edges)

    for path in edge_list:
        temp = {}
        for obstacle in poly_edge_list:
            intersection = do_intersect(path[0], path[1], obstacle[0], obstacle[1])     
            if intersection:
                #print("path " + str(path) + "intersected with " + str(obstacle))
                break  
        else:
            counter += 1
            letter1 = [l for l, point in test.items() if point == path[0]]
            letter2 = [l for l, point in test.items() if point == path[1]]
            temp[letter2[0]] = computeDistance(path[0], path[1])
            visible_edges[letter1[0]].update(temp)
            

        #print("visible edges for path" + str(path[0]) + str(path[1]))
    print(visible_edges)
    #return(visible_edges)



p1 = np.array([[0, 1], [2, 4], [1, 6]])
p2 = np.array([[4, 4], [7, 4], [6, 8]])
p1n = p1.tolist()
p2n = p2.tolist()


vertex_list = [[0.0,0.0], [0.0, 1.0], [1.0, 6.0], [2.0, 4.0], [4.0, 4.0], [6.0, 8.0], [7.0, 4.0], [8.0,8.0]]
polygons = [p1n, p2n]
createVisibilityGraph(polygons, vertex_list)

#print(computeDistance([1,6], [6,8]))