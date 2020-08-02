import numpy as np
import random
import os
from matplotlib import pyplot as plt

#points = np.array([[0,0], [1,1], [1,0], [0,1], [0.5,1.5], [0.5,0.5]])

class blob(object):
    points = np.array([1])
    lowDex = np.array([-1,-1])
    hullPts = np.array([])

    def __init__(self, x_cent, y_cent, width, point_count=20):

        self.points = np.array([[x_cent+width*random.random(), y_cent+width*random.random()]])
        for i in range(19):
            newPoint = np.array([[x_cent+width*random.random(), y_cent+width*random.random()]])
            self.points = np.vstack([self.points, newPoint])

        lowDex, hullx, hully = self.getConvexPoly(self.points)
        self.hullPts = np.transpose( np.vstack([hullx, hully]) )




    def getAngle(self, point1, point2, point3):
        mag1 = np.sqrt( (point1[0] - point2[0])**2 + (point1[1] - point2[1])**2 )
        mag2 = np.sqrt( (point3[0] - point2[0])**2 + (point3[1] - point2[1])**2 )

        dotProd = np.dot((point1 - point2), (point3 - point2))

        theta = np.arccos(dotProd / (mag1*mag2))
        return theta

    def getNextHullPoint(self, hullDexes, points, firstPoint=False):
        maxAngle = -1 #set starting point lower than any real point would be
        nextDex = -1

        for i in range(len(points)):
            if i != hullDexes[-1]:
                if firstPoint:
                    newAngle = self.getAngle([points[hullDexes[0],0]+1, points[hullDexes[0],1]], points[hullDexes[0]], points[i])
                else:
                    newAngle = self.getAngle(points[hullDexes[-2]], points[hullDexes[-1]], points[i])

                if newAngle > maxAngle:
                    maxAngle = newAngle
                    nextDex = i

        return nextDex

    def getConvexPoly(self, points):
        lowDex = 4
        for i in range(len(points[:,0])):
            if i != lowDex:

                if points[i,1] < points[lowDex,1]:
                    #if point is further left than current min
                    lowDex = i
                elif points[i,1] == points[lowDex, 1]:
                    if points[i,0] < points[lowDex,0]:
                        #if point is as left and lower than current min
                        lowDex = i

        currDex = lowDex
        hullPoints = np.array([ lowDex ])

        currDex = self.getNextHullPoint(hullPoints, points, firstPoint=True)
        hullPoints = np.append(hullPoints, [currDex])

        while (currDex != lowDex):
            currDex = self.getNextHullPoint(hullPoints, points)
            hullPoints = np.append(hullPoints, [currDex])

        x_vals = [ ]
        y_vals = [ ]

        for i in hullPoints:
            x_vals.append(points[i,0])
            y_vals.append(points[i,1])

        return lowDex, x_vals, y_vals


    def onSegment(self, p, q, r):
        # Taken from geeksforgeeks.com:
        # https://www.geeksforgeeks.org/check-if-two-given-line-segments-intersect/
        if ( (q[0] <= max(p[0], r[0])) and (q[0] >= min(p[0], r[0])) and (q[1] <= max(p[1], r[1])) and (q[1] >= min(p[1], r[1]))):
            return True
        return False

    def orientation(self, p, q, r):
        # Taken from geeksforgeeks.com:
        # https://www.geeksforgeeks.org/check-if-two-given-line-segments-intersect/

        # to find the orientation of an ordered triplet (p,q,r)
        # function returns the following values:
        # 0 : Colinear points
        # 1 : Clockwise points
        # 2 : Counterclockwise

        # See https://www.geeksforgeeks.org/orientation-3-ordered-points/amp/
        # for details of below formula.

        val = (float(q[1] - p[1]) * (r[0] - q[0])) - (float(q[0] - p[0]) * (r[1] - q[1]))
        if (val > 0):

            # Clockwise orientation
            return 1
        elif (val < 0):

            # Counterclockwise orientation
            return 2
        else:

            # Colinear orientation
            return 0

    # The main function that returns true if
    # the line segment 'p1q1' and 'p2q2' intersect.
    def doIntersect(self, p1,q1,p2,q2):
        # Taken from geeksforgeeks.com:
        # https://www.geeksforgeeks.org/check-if-two-given-line-segments-intersect/

        # Find the 4 orientations required for
        # the general and special cases
        o1 = self.orientation(p1, q1, p2)
        o2 = self.orientation(p1, q1, q2)
        o3 = self.orientation(p2, q2, p1)
        o4 = self.orientation(p2, q2, q1)

        # General case
        if ((o1 != o2) and (o3 != o4)):
            return True

        # Special Cases

        # p1 , q1 and p2 are colinear and p2 lies on segment p1q1
        if ((o1 == 0) and self.onSegment(p1, p2, q1)):
            return True

        # p1 , q1 and q2 are colinear and q2 lies on segment p1q1
        if ((o2 == 0) and self.onSegment(p1, q2, q1)):
            return True

        # p2 , q2 and p1 are colinear and p1 lies on segment p2q2
        if ((o3 == 0) and self.onSegment(p2, p1, q2)):
            return True

        # p2 , q2 and q1 are colinear and q1 lies on segment p2q2
        if ((o4 == 0) and self.onSegment(p2, q1, q2)):
            return True

        # If none of the cases
        return False

    def getIntersection(self, p1, q1, p2, q2):
        # Used logic form a stack overflow answer:
        # https://stackoverflow.com/questions/3838329/how-can-i-check-if-two-segments-intersect
        m1 = (q1[1] - p1[1]) / (q1[0] - p1[0])
        m2 = (q2[1] - p2[1]) / (q2[0] - p2[0])
        b1 = p1[1] - m1*p1[0]
        b2 = p2[1] - m2*p2[0]

        x_int = (b2 - b1) / (m1 - m2)
        y_int = m1*x_int + b1

        inv_slope = -1 / m2

        return np.array([x_int, y_int]), inv_slope

    def detectIntersection(self, pathPts):
        for i in range(1, len(pathPts)):
            #loop through all path points
            pt1 = pathPts[i-1]
            pt2 = pathPts[i]

            for j in range(1,len(self.hullPts)):
                #loop through all line segments that form object boudnary
                start = self.hullPts[j-1]
                end = self.hullPts[j]

                if self.doIntersect(start, end, pt1, pt2):
                    # add intersection point to path, then add one of the endpoints
                    # of the side of the polygon (whichever is closer to where we want to go)
                    intersection, iSlope = self.getIntersection(start, end, pt1, pt2)

                    dist1 = np.sqrt( (start[0] - pt2[0])**2 + (start[1] - pt2[1])**2 )
                    dist2 = np.sqrt( (end[0] - pt2[0])**2 + (end[1] - pt2[1])**2 )


                    if dist1 > dist2:
                        pathPts = np.vstack([ pathPts[:i], intersection, end, pathPts[i:] ])
                        return pathPts
                    else:
                        pathPts = np.vstack([ pathPts[:i], intersection, start, pathPts[i:] ])
                        return pathPts


        return pathPts







startPt = np.array([0,0])
finishPt = np.array([8,8])

pathPts = np.array([startPt, finishPt])
obstructed = False

obj1 = blob(2, 1, 2)
obj2 = blob(5 ,2, 1.5)
obj3 = blob(2, 5, 2)
obj4 = blob(6, 5, 2)

"""
if (pathPts): #check for obstruction
    obstructed = True
    iter = 0

while(obstructed and iter < 1e3):
    print("a")
    # add point to fix current obstruction
    # check again to see if obstructed, set obstructed variable accoringly
"""

"""
ptsAdded = 1
iter = 0
while(ptsAdded != 0 and iter<100):
    ptsAdded = 0
    initLen = len(pathPts)
    pathPts = obj1.detectIntersection(pathPts)
    pathPts = obj2.detectIntersection(pathPts)
    pathPts = obj3.detectIntersection(pathPts)
    pathPts = obj4.detectIntersection(pathPts)
    ptsAdded = len(pathPts) - initLen
    iter += 1
"""
pathPts = obj1.detectIntersection(pathPts)
pathPts = obj2.detectIntersection(pathPts)
pathPts = obj3.detectIntersection(pathPts)
pathPts = obj4.detectIntersection(pathPts)

print(len(pathPts), pathPts)

plt.title("Convex Hull Demonstration")
plt.xlabel("X [m]")
plt.ylabel("Y [m]")
plt.scatter(obj1.points[:,0], obj1.points[:,1], color='blue', label='Points')
plt.scatter(obj2.points[:,0], obj2.points[:,1], color='blue')
plt.scatter(obj3.points[:,0], obj3.points[:,1], color='blue')
plt.scatter(obj4.points[:,0], obj4.points[:,1], color='blue')

#plt.scatter(obj1.center[0], obj1.center[1], color='purple')
#plt.scatter(obj2.center[0], obj2.center[1], color='purple')
#plt.scatter(obj3.center[0], obj3.center[1], color='purple')
#plt.scatter(obj4.center[0], obj4.center[1], color='purple')

plt.plot(obj1.hullPts[:,0], obj1.hullPts[:,1], color='green', linestyle='--', label='Convex Hull')
plt.plot(obj2.hullPts[:,0], obj2.hullPts[:,1], color='green', linestyle='--')
plt.plot(obj3.hullPts[:,0], obj3.hullPts[:,1], color='green', linestyle='--')
plt.plot(obj4.hullPts[:,0], obj4.hullPts[:,1], color='green', linestyle='--')

plt.scatter(startPt[0],startPt[1], color='red', label='Start')
plt.scatter(finishPt[0], finishPt[1], color='orange', label='Finish')

plt.plot(pathPts[:,0], pathPts[:,1], label='Path')

plt.xlim(-1,12)
plt.ylim(-1,10)
plt.legend(loc='lower right')
plt.show()