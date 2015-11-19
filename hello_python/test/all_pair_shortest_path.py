'''
Created on Nov 18, 2015

@author: shuaipeng
'''
from test.DP_problem import print_2D_array
def extend_shortest_paths(L, W):
    n = len(L)
    L_prim = [[float("inf") for _ in range(0, n)] for _ in range(0, n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                L_prim[i][j] = min(L_prim[i][j], L[i][k] + W[k][j])
            print "L[{},{}] = {l_prim} is min of ".format(i+1, j+1, l_prim = L_prim[i][j])
            print ', '.join(['{} + {}'.format(L[i][k], W[k][j]) for k in range(n)])

    return L_prim

def faster_all_pairs_shorted_paths(W):
    n = len(W)
    L = W
    m = 1
    print 'L({}) = '.format(m)
    print_2D_array(L)
    while m < n-1:
        L = extend_shortest_paths(L, L)
        m = 2*m
        print 'L({}) = '.format(m)
        print_2D_array(L)
    return L

if __name__ == '__main__':
    W = [[0,    -4, 3,  float("inf"),   float("inf")],
         [float("inf"), 0, 2, 1, float("inf")],
         [float("inf"), -1, 0, 7, 5],
         [float("inf"), float("inf"), float("inf"), 0, 10],
         [float("inf"), float("inf"), float("inf"), -8, 0]]
    res = faster_all_pairs_shorted_paths(W)
    print_2D_array(res)