#Author: Daniel Hong
#It is okay to post my anonymized solution

import sys

def main(): 
    num = int(sys.stdin.readline()) #getting the integer 
    array = sys.stdin.readline().strip().split() #reading the second line of integers and splitting each element into a list
    
    temp_greater = array[0] #temp variable that holds the first value of the array list
    temp_lesser = array[num - 1] #temp variable that holds the last value of the array list
    
    gr_table = [False] * num #table of numbers that holds Falses - to be changed to Trues for elements greater
    ls_table = [False] * num #table of numbers that holds Falses - to be changed to Trues for elements lesser
    
    for x in range(num):
        #traversing from the right side of array, we compare if the second right-most element is less than the right most-element
        if x == 0 or (int(array[num-x-1]) < int(temp_lesser)): 
            temp_lesser = array[num-x-1] #if condition is met, we update the temp variable for next comparison
            ls_table[num-x-1] = True #update index of boolean table to True for future count

        #traversing from the left side of array, we compare if the next element is less greater 
        if (int(array[x]) >= int(temp_greater)): 
            temp_greater = array[x] #if condition is met, we update the temp variable for next comparison
            gr_table[x] = True #update index of boolean table to True for future count
        
    final = 0 #final count 
    
    for i in range(num):
        if gr_table[i] == True and ls_table[i] == True:
            final += 1 #if there is True for both tables at i index, then we know that the element is a valid pivot so we increment count
    
    print(final)
    
if __name__ == "__main__":
    main()