import numpy as np
from matplotlib import pyplot as plt
from math import atan2

N = 100
data = 120*np.random.rand(N, 2)+50



# data = np.array([[0.0, 1.0], [1.5, 4.0], [1.0, 6.0], [4.0, 4.0], [7.0, 4.0], [5.5, 8.0]])
# data = np.array([[4.0, 4.0], [7.0, 4.0], [5.5, 8.0]])
# print(type(data))

def grahamScan(data, N):
    global anchor
    minIndex = np.where(data[:, 1] == np.amin(data[:, 1]))
    anchor = data[minIndex][0]
    
    # remove lowest y point so we don't double calculate
    _data = np.delete(data, minIndex[0][0], 0)
    sortedData = sortByPolarAngle(_data)

    hull = [anchor, sortedData[0]]

    for i in sortedData[1:]:
        while det(hull[-2], hull[-1], i) <= 0:
            del hull[-1]
        hull.append(i)
    return np.array(hull)

def det(p1,p2,p3):
	return   (p2[0]-p1[0])*(p3[1]-p1[1]) \
			-(p2[1]-p1[1])*(p3[0]-p1[0])

def polar_angle(p0):
    p1 = anchor
    x_delta = p0[0] - p1[0]
    y_delta = p0[1] - p1[1]
    return np.arctan2(y_delta, x_delta) 

def sortByPolarAngle(data):
    return np.array(sorted(data, key = polar_angle))

if __name__ == "__main__":
    hull = grahamScan(data, N)
    hull_x = hull[:,0]
    hull_y = hull[:,1]
    hull_x = np.append(hull_x, hull_x[0])
    hull_y = np.append(hull_y, hull_y[0])
    plt.scatter(data[:,0], data[:,1])
    plt.plot(hull_x, hull_y, 'r-')
    plt.show()


