#Author: Daniel Hong
#It is okay to post my anonymized solution

import sys

def binary_search(temp_list, x): #helper function that performs binary search - citing G4G for helping me
    #Goal:
    #use the # in the first list as the target x need to find
    #return index of x in the sorted temp_list
    
    left = 0 #low bound
    mid = 0 #mid point
    right = len(temp_list) - 1 #high bound
    
    while right >= left: #while loop to perform binary searcj
        
        mid = (right + left) // 2 

        # If x is smaller, ignore left half
        if temp_list[mid] < x:
            left = mid + 1 #then we iterate and go right/higher
 
        # If x is smaller, ignore right half
        elif temp_list[mid] > x:
            right = mid - 1 #then we iterate and go left/lower
 
        # means x is present at mid
        else:
            return mid #returning 0 (index of 10 in sorted list)
 

def main():
    
    while True: #while loop to take in multiple cases
        n = int(sys.stdin.readline().strip()) #getting the input n
       
        if n == 0: #once n=0, then we know to stop the program
            return
       
        first_list = [] #list for the first list
        second_list = [] #list for the second list
        
        for x in range(n):
            first_list.append(int(sys.stdin.readline().strip())) #appending the first list from the inputs we
        
        for y in range(n):
            second_list.append(int(sys.stdin.readline().strip())) #appending the second list from the inputs we got
        
        temp_list = first_list #we want to create a temp list that is a sorted first list
        temp_list = sorted(first_list) #we sort our temp list
        second_list.sort() #sorting the second list
        
        index = 0 #index variable

        for i in range(len(temp_list)): #for loop for our binary search
            index = binary_search(temp_list, first_list[i]) #we call the binary search with our (sorted first list, value of first list at index i)
            print(second_list[index])
            
        print()
            
if __name__ == "__main__":
    main()