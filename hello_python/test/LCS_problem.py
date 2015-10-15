'''
Created on Oct 15, 2015

@author: shuaipeng
'''
from test.DP_problem import print_2D_array
def solve_LCS(x, y):
    m = len(x) - 1
    n = len(y) - 1
#     b = [[0 for _ in range(n+1)] for _ in range(m+1)]
    c = [[0 for _ in range(n+1)] for _ in range(m+1)]
    for i in range(1, m+1):
        c[i][0] = 0
    for j in range(n+1):
        c[0][j] = 0
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if x[i] == y[j]:
                c[i][j] = c[i - 1][j - 1] + 1
            elif c[i - 1][j] > c[i][j - 1]:
                c[i][j] = c[i - 1][j]
            else:
                c[i][j] = c[i][j - 1]
    return c

def construct_LCS(c, m, n, x ,y):
    i, j = m, n
    LCS = []
    while c[i][j] != 0:
        if x[i] == y[j]:
            LCS.append(x[i])
            i, j = i - 1, j - 1
        elif c[i - 1][j] == c[i][j]:
            i = i - 1
        else:
            j = j - 1
    LCS.reverse()
    return LCS

if __name__ == '__main__':
    x = [None, 1, 0, 0, 1, 0, 1, 0, 1]
    y = [None, 0, 1, 0, 1, 1, 0, 1, 1, 0]
    c = solve_LCS(x, y)
    print_2D_array(c)
    print construct_LCS(c, len(x) - 1, len(y) - 1, x ,y)