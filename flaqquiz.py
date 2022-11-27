#Author: Daniel Hong
#It is ok to post my anonymized solution

import sys

Question = sys.stdin.readline() # reads the question (honestly don't need question var but had it for clarity)
N = int(sys.stdin.readline()) # reads the number of choices 

#initializing lists for future use
choices = [] #initializing a list of answer choices
elements = [] #creating a list for the elements in an answer choice
temp_choice = [] #creating a temp list that will be unaltered that holds the answer choices (for future use)


for x in range(N): #for loop that runs N times
    temp = sys.stdin.readline().strip() #reading the answer choices
    temp_choice.insert(x,temp) #storing the list with answer choices

    elements = temp.split(', ') #returns a list of an answer choice
    
    choices.insert(x, elements) #choices list becomes a list of list by inserting the elements list

max_list = [0] * N #initialize a list solely for holding the "max diff" values
diff = [ [0]* N for i in range(N)] #initalizing a list of list depending on N

for k in range(N): #k is our variable for FLAGS
    for j in range((k+1), N): #j is the pair we are comparing with
        for i in range(len(elements)): #i is the color
            if choices[k][i] != choices[j][i]: #here we start comparing the elements of the answer choices (AKA colors)
                diff[k][j] += 1 #fill upper triangle of our list with the diff values
        diff[j][k] = diff[k][j] #fill lower triangle of our list with the diff values
        if max_list[k] < diff[k][j]:
            max_list[k] = diff[k][j] #if our curr is greater than replace
        if max_list[j] < diff[k][j]:
            max_list[j] = diff[k][j] #this traverses the last answer choice 

#Now we print our output here after knowing the diff values:
temp = 10000 #temp var with an arbitrary number that is very big
for x in range(N): 
    if max_list[x] < temp:
        temp = max_list[x] #now we are sifting through the list and finding the minimum of the max diff values

#after we know the minimum, we now start printing the choices that have the same minimum (could be multiple answers)
for y in range(N): #for loop 
    if max_list[y] == temp: #finding the indices that have same minimum values
        print(temp_choice[y]) #prints the answer output