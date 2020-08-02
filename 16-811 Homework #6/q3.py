import numpy as np
from q1 import findConvexHull
from q2 import VisibiltyGraph
import matplotlib.pyplot as plt

if __name__ == "__main__":
    # overlapping test case
    # points = [[[1.0, 2.0], [4.0, 3.0], [4.0, 2.0]], [[4.0, 8.0], [6.0, 7.0], [4.0, 4.0], [7.0, 6.0]], [[6.0, 8.0], [9.84, 8.87], [7.16, 11.76]], [[6.0, 10.0], [8.0, 10.0], [5.0, 11.74], [6.0, 13.46], [8.0, 13.46], [9.0, 11.73]]]
    
    # isolated test case
    points = [[[2.0, 2.0], [0.0, 6.0], [4.0, 10.0], [10.0, 7.0], [7.0, 3.0]], [[7.0, -2.0], [7.0, 0.0], [9.0, 0.0], [9.0, -2.0]], [[22.0, 0.0], [20.0, 4.0], [24.0, 8.0], [30.0, 5.0], [27.0, 1.0]], [[12.0, 18.0], [10.0, 24.0], [14.0, 30.0], [20.0, 23.0], [17.0, 18.0]], [[12.0, 12.0], [17.0, 15.0], [26.0, 15.0], [23.0, 12.0]], [[25.0, 20.0], [23.0, 28.0], [29.0, 29.0], [34.0, 21.0]]]
    # points = [[[2.0, 2.0], [0.0, 6.0], [4.0, 10.0], [10.0, 7.0], [7.0, 3.0]], [[7.0, -2.0], [7.0, 0.0], [9.0, 0.0], [9.0, -2.0]], [[22.0, 0.0], [20.0, 4.0], [24.0, 8.0], [30.0, 5.0], [27.0, 1.0]], [[12.0, 14.0], [10.0, 21.0], [14.0, 30.0], [20.0, 23.0], [17.0, 14.0]], [[12.0, 12.0], [17.0, 15.0], [26.0, 15.0], [23.0, 12.0]], [[25.0, 20.0], [23.0, 28.0], [29.0, 29.0], [34.0, 21.0]]]
    
    # another isolated test case
    points = [[[0.7, 4.06], [0.6, 2.01], [2.42, 2.95]], [[4.5, 2.59], [5.76, 1.95], [5.14, 3.81], [6.4, 3.17]], [[4.98, 4.87], [6.0, 5.0], [6.4, 5.95], [5.77, 6.77], [4.75, 6.64], [4.36, 5.69]]]
    # yet another isolated case
    # points = [[[0.0, 1.0], [1.5, 4.0], [1.0, 6.0]], [[4.0, 4.0], [7.0, 4.0], [5.5, 8.0]]]

    # overlapping test case
    # points = [[[0.0, 1.0], [4.0, 2.0], [4.0, 0.0]], [[4.0, 8.0], [6.0, 7.0], [4.0, 5.0], [7.0, 6.0]], [[6.0, 8.0], [9.84, 8.87], [7.16, 11.76]], [[6.0, 10.0], [8.0, 10.0], [5.0, 11.74], [6.0, 7.46], [8.0, 13.46], [9.0, 11.73]]]

    start = np.array([0, 0])
    end = np.array([8, 8])
    
    # robot = np.array([[0,0],[0,0.5],[0.5,0]], np.float32)
    robot = np.array([[0,1],[-1,-1],[1,-1]], np.float32)

    # works with isolated case 1 and end = 20,20
    # robot = np.array([[-1,-1],[-1,1],[0,1],[1,1],[1,-1]], np.float32)
    
    vg = VisibiltyGraph(points, start, end)
    vg.getMinkowskiSum(robot)
    vg.findShortestPath()
    print (vg.shortestPath)
    vg.plotPolygonsAndPaths(robot, isRobot=True)