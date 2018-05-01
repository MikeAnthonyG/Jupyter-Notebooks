import random as r
import math

def plums(n=3, trials=10000):
    total=0
    for i in range(trials):
        points = [0 for x in range(0, n)]
        for j in range(0,n):
            flag = True
            while flag:
                x = -1.0 + 2 * r.random()
                y = -1.0 + 2 * r.random()
                z = -1.0 + 2 * r.random()
                d = x**2 + y**2 + z**2
                if d < 1.0:
                    flag = not flag
            points[j] = math.sqrt(d)
        total += max(points)
    print(1-(total/trials))