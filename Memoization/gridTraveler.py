"""
Supposed that you are travelling on a 2D grid. Your goal is to move from the top-left corner to the bottom-right
You must only move down and right. How many ways to move if you travelled in
a 2D grid whose dimensions m*n?
"""
import numpy as np
def gridTravel(m, n):
    if m == 1 and n == 1:
        return 1
    memoi = [[0 for i in range(n)] for j in range(m)]
    for i1 in range(1, m):
        memoi[i1][0] = 1
    for i2 in range(1, n):
        memoi[0][i2] = 1
    
    for i in range(1, m):
        for j in range(1, n):
            memoi[i][j] = memoi[i-1][j] + memoi[i][j-1]
    print(np.array(memoi))
    return memoi[m-1][n-1]
    

print(gridTravel(1, 1))
print(gridTravel(2, 3))
print(gridTravel(3, 2))
print(gridTravel(3, 3))
print(gridTravel(3, 7))