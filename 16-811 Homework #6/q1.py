import numpy as np
from matplotlib import pyplot as plt
import sys

def findConvexHull(points):
    points = np.array(points, dtype=np.float32)
    
    if points.shape[0] < 3:
        print ("Minimum 3 points required")
        sys.exit(1)

    rotated_points = np.rot90(points)
    points = points[np.lexsort(rotated_points)]

    lower, upper = [], []
    N = points.shape[0]
    for i in range(0,N):
        while len(lower)>=2 and -1*np.cross((points[i]-lower[-2]), (lower[-1]-lower[-2])) <= 0:
            lower.pop()
        lower.append(points[i])

    for j in range(N-1, -1,-1):
        while len(upper)>=2 and -1*np.cross((points[j]-upper[-2]), (upper[-1]-upper[-2])) <= 0:
            upper.pop()

        upper.append(points[j])

    hull = np.array(lower[:-1]+upper[:-1])
    return hull

if __name__ == "__main__":
    points = 120*np.random.rand(500, 2)+50
    hull = findConvexHull(points)
    hull_x = hull[:,0]
    hull_y = hull[:,1]
    hull_x = np.append(hull_x, hull_x[0])
    hull_y = np.append(hull_y, hull_y[0])
    plt.plot(points[:,0],points[:,1], 'bo')
    plt.plot(hull_x, hull_y, 'r-')
    plt.show()