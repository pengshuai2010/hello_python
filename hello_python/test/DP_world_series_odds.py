'''
Created on Oct 15, 2015

@author: shuaipeng
'''
from test.DP_problem import print_2D_array
def solve_DP(n, p):
    P = [[0 for _ in range(n+1)] for _ in range(n+1)]
    for i in range(n+1):
        P[i][0] = 0
    for j in range(n+1):
        P[0][j] = 1
    for i in range(1, n+1):
        for j in range(1, n+1):
            P[i][j] = p*P[i - 1][j] + (1 - p)*P[i][j-1]
    return P

if __name__ == '__main__':
    print_2D_array(solve_DP(n = 7, p = 0.4))