import numpy as np
#from testingIntersection import createVisibilityGraph

vertex_list = [[0.0,0.0], [0.0, 1.0], [1.0, 6.0], [2.0, 4.0], [4.0, 4.0], [6.0, 8.0], [7.0, 4.0], [8.0,8.0]]
# p1 = np.array([[0, 1], [2, 4], [1, 6]])
# p2 = np.array([[4, 4], [7, 4], [6, 8]])
# p1n = p1.tolist()
# p2n = p2.tolist()
# polygons = [p1n, p2n]
#vGraph = createVisibilityGraph(polygons, vertex_list)

test = {}
test2 = {}
start = 'a'

for i in range(len(vertex_list)):
    test[chr(ord(start) + i)] = vertex_list[i]
    test2[chr(ord(start) + i)] = vertex_list[i]


x = [letter for letter, point in test.items() if point == [0.0,1.0]]
print(x[0])
y = [letter for letter, point in test.items() if point == [1.0,6.0]]
print(y[0])
l = {}
l['x'] = 3
l['y'] = 4
test2['a'] = l 
print(test2)
# start = 'a'
# for i in range(10):
#     letter = chr(ord(a) + i)
#     print(letter)