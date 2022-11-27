#Author: Daniel Hong
#It is okay to post my anonymized solution

import sys
sys.setrecursionlimit(1000000) #needed this line to set a recursion limit for Python

#taking in the inputs and initializing N and M
nm = sys.stdin.readline().split(" ")
n = int(nm[0]) 
m = int(nm[1]) 

if m <= 0: #a potential edge case where M is 0 or negative
    print(0) 
else:
    #creating a 2D array (list of lists) and creating a "border" around soteholm to be able to DFS
    soteholm = [] 
    border = ['0' for _ in range(m+2)] #array of 0's for top border
    end_border = ['0' for _ in range(m+2)] #array of 0's for bottom border

    soteholm.append(border) 

    for x in range(n):
        list1 = [] 
        coast = sys.stdin.readline().strip() #reading each line
        list1[:0] = coast 
        soteholm.append(['0'] + list1 + ['0']) #appending a '0' before and after the line to make the "border" of 0's

    soteholm.append(end_border)

    count = 0 #count variable for output

    def isOutOfBounds(i, j, soteholm): #out of bounds function to make sure everything is within bounds
        if (i < 0 or i >= len(soteholm) or j < 0 or j >= len(soteholm[i])):
            return True 

        return False

    def dfs(soteholm, i, j):
        global count

        soteholm[i][j] = 'X' #marking a place as visited with 'X'

        #Below four functions are just DFSing the whole soteholm 2D array. 

        #j + 1 route when not out of bounds/ and not previously visited, then we add to our count
        if (not isOutOfBounds(i, j+1, soteholm)) and (soteholm[i][j+1] != 'X'):
            if soteholm[i][j+1] == '1':
                count += 1
            else:
                dfs(soteholm, i, j+1)

        #j - 1 route when not out of bounds/ and not previously visited, then we add to our count
        if (not isOutOfBounds(i, j-1, soteholm)) and (soteholm[i][j-1] != 'X'):
            if soteholm[i][j-1] == '1':
                count += 1
            else:
                dfs(soteholm, i, j-1)

        #i + 1 route when not out of bounds/ and not previously visited, then we add to our count
        if (not isOutOfBounds(i+1, j, soteholm)) and (soteholm[i+1][j] != 'X'):
            if soteholm[i+1][j] == '1':
                count += 1
            else:
                dfs(soteholm, i+1, j)

        #i - 1 route - when not out of bounds/ and not previously visited, then we add to our count
        if (not isOutOfBounds(i-1, j, soteholm)) and (soteholm[i-1][j] != 'X'):
            if soteholm[i-1][j] == '1':
                count += 1
            else:
                dfs(soteholm, i-1, j)

    dfs(soteholm, 0, 0) #calling our DFS function 

    print(count) #printing the final output