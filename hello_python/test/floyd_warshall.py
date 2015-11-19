'''
Created on Nov 18, 2015

@author: shuaipeng
'''
from test.DP_problem import print_2D_array
def floyd_warshall(W):
    n = len(W)
    D = W
    PI = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i == j or W[i][j] == float("inf"):
                PI[i][j] = None
            else:
                PI[i][j] = i 
    for k in range(n):
        print "k = {}".format(k+1)
        D_new = [[0 for _ in range(n)] for _ in range(n)]
        PI_new = [[0 for _ in range(n)] for _ in range(n)]
        #calculate D
        for i in range(n):
            for j in range(n):
                D_new[i][j] = min(D[i][j], D[i][k] + D[k][j])
                print "D({k})[{i}, {j}] = min(D({k_1})[{i}, {j}], D({k_1})[{i}, {j}] + D({k_1})[{i}, {j}])".format(k = k+1, k_1 = k, i = i+1, j = j+1)
                print "{} = min({}, {} + {})".format(D_new[i][j], D[i][j], D[i][k], D[k][j])
                print ""
        #calculate PI
        for i in range(n):
            for j in range(n):
                if D[i][j] <= D[i][k] + D[k][j]:
                    PI_new[i][j] = PI[i][j]
                else:
                    PI_new[i][j] = PI[k][j]
        #update D
        D = D_new
        print "D({}) = ".format(k + 1)
        print_2D_array(D_new)
        print ""
        #update PI
        PI = PI_new
        print "PI({k}) = ".format(k = k+1)
        display_mat = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if PI[i][j] is not None:
                    display_mat[i][j] = PI[i][j] + 1
                else:
                    display_mat[i][j] = PI[i][j]
        print_2D_array(display_mat)# display index from 1
    return D_new

if __name__ == '__main__':
    W = [[0,    -4, 3,  float("inf"),   float("inf")],
     [float("inf"), 0, 2, 1, float("inf")],
     [float("inf"), -1, 0, 7, 5],
     [float("inf"), float("inf"), float("inf"), 0, 10],
     [float("inf"), float("inf"), float("inf"), -8, 0]]
    res = floyd_warshall(W)
    print_2D_array(res)