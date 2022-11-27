#Author: Daniel Hong
#It is okay to post my anonymized solution

import sys

def binary_search(sequence, x): #binary search helper function - citing G4G for helping me 
    low = 0 #low bound
    mid = 0 #mid point
    high = len(sequence) - 1 #high bound
    
    while (low <= high): #while loop to start searching
        mid = (low + high) // 2
        
        #ignore left
        if sequence[mid] < x:
            low = mid + 1
        
        #ignore right
        if sequence[mid] > x:
            high = mid - 1
        
        #we want the exact
        if sequence[mid] == x:
            return mid
    
    return -1 #binary search could not find

def sequence(n, m, a, c, xo):
    xi = ((xo*a) + c) % m #sequence formula given 
    sequence_list = [] 
    sequence_list.append(xi) #appending the sequence we get into a list
    
    for x in range(n - 1): #appending the rest of the sequence of length n
        xi = ((xi*a) + c) % m #formula
        next_xi = xi
        sequence_list.append(next_xi) #appending the rest
    
    return sequence_list

def main():
    input_list = sys.stdin.readline().split(" ") #getting inputs and putting them into a list
    
    n = int(input_list[0]) #getting n
    m = int(input_list[1]) #getting m
    a = int(input_list[2]) #getting a
    c = int(input_list[3]) #getting c
    xo = int(input_list[4]) #getting xo
    
    result = sequence(n, m, a, c, xo) #calling my sequence helper function with the variables as parameters
    counter = 0 #counter to see how many we find in the binary search
    
    for i in range(len(result)):
        final = binary_search(result, result[i]) #calling binary search function
        
        if final != -1: #if we don't return -1 (a.k.a we are able to find the desired eleement)
            counter += 1 #then we add 1 to the counter
    
    print(counter) #print the result
    
if __name__ == "__main__":
    main()
