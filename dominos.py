import sys
import collections
from collections import deque

#referred G4G DFS functions
global adj
global L

num = 1

int_list = [0 for i in range(N)] #list of 0's

#assign function
def assign(x):

    if int_list[x] == 0:
        num += 1
        int_list[x] = num
        for i in adj[v][1]:
            assign(i)


#DFS helper function
def helper(v):

    # Mark the current node as visited and print it
    #visited[v] = True

    if not visited[v]:
        visited[v] = True
        for child in adj[v][0]:
            helper(child)
        L.appendleft(v)

    #Traverses through the forward array
    #for i in adj[v][0]:
    #    if visited[i] == False:
    #        helper(adj ,i, visited)


    #Traverses through the backward array
    #for i in adj[v][1]:
    #    if visited[i] == False:
    #        helper(adj, i, visited)


#DFS function
# def DFS(adj):
#     V = len(adj)  #total vertices

#     # Mark all the vertices as not visited
#     visited =[False for x in range(V)]

#     # Call the recursive helper function to print
#     # DFS traversal starting from all vertices one
#     # by one

#     minimum = float('inf')

#     for k in range(V):
#         count = 0
#         curr_node = k
#         for i in range(V):
#             if curr_node >= V:
#                 curr_node = 0
#             if visited[curr_node] == False:
#                 helper(adj, i, visited)
#                 count += 1
#             curr_node += 1

#         if (count < minimum):
#             minimum = count
               
#         visited = [False for p in range(V)]

#     return count

def main():
    
    test = int(sys.stdin.readline().strip()) #test case

    for j in range(test):
        nm = sys.stdin.readline().split(" ")
        N = int(nm[0]) #num of dom
        M = int(nm[1]) #num of lines
        
        #[[[FORWARD], [BACKWARD]], [[F], [B]], [[F], [B]]]
        #[[[2], []], [[3], [1]], [[], [2]]] (I added 1)
        #    D:1         D:2        D:3
        adj = [[[] for j in range(2)] for i in range(N)]
        L = deque([])
        
        for i in range(M):
            xy = sys.stdin.readline().split(" ")
            x = int(xy[0]) - 1 #
            y = int(xy[1]) - 1
            
            adj[x][0].append(y)
            adj[y][1].append(x)

        for v in range(N):
            helper(v)

        for x in L:
            groups = assign(x)
        
        #count = DFS(adj)

        print(groups)
        

if __name__ == "__main__":
    main()
