'''
Created on Oct 14, 2015

@author: speng
'''

class Tree_node(object):
    def __init__(self):
        self.data = None
        self.left = None
        self.right = None

def dp_programming(p, q, n):
    e = [[0 for _ in range(0, n+1)] for _ in range(0, n+1+1)]
    w = [[0 for _ in range(0, n+1)] for _ in range(0, n+1+1)]
    root = [[0 for _ in range(0, n+1)] for _ in range(0, n+1)]
    for i in range(1, n + 1+1):
        e[i][i - 1] = q[i - 1]
        w[i][i - 1] = q[i - 1]
    for l in range(1,n+1):
        for i in range(1,n - l + 1+1):
            j = i + l - 1
            e[i][j] = 1e6
            w[i][j] = w[i][j - 1] + p[j] + q[j]
            for r in range(i, j+1):
                t = e[i][r - 1] + e[r + 1][j] + w[i][j]
                if t < e[i][j]:
                    e[i][j] = t
                    root[i][j] = r
    return e, w, root

def print_2D_array(A):
    print ('\n'.join([','.join(['{:16}'.format(item) for item in row]) 
                  for row in A]))

def construct_BST(table, start, end):
    if start > end:
        return None
    root = table[start][end]
    root_node = Tree_node()
    root_node.data = root
    root_node.left = construct_BST(table, start, root - 1)
    root_node.right = construct_BST(table, root + 1, end)
    return root_node

def print_tree(root_node):
    if root_node == None:
        return
    print root_node.data
    print_tree(root_node.left)
    print_tree(root_node.right)

if __name__ == '__main__':
        p = [0, 0.04, 0.06, 0.08, 0.02, 0.10, 0.12, 0.14]
        q = [0.06 for _ in range(0, 3+1)] + [0.05 for _ in range(4, 7+1)]
        n = len(p)-1
        e, w, root = dp_programming(p, q, n)
        print "e = "
        print_2D_array(e)
        print "w = "
        print_2D_array(w)
        print "root ="
        print_2D_array(root)
        root_node = construct_BST(root, 1, n)
        print_tree(root_node)