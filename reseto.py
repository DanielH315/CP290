#Daniel Hong
#It is ok to post my anonymized solution
#9/2/22
#some comments are based on sample input 1
import sys

line = sys.stdin.readline().split(" ") #reads input

N = int(line[0]) #N = 7 - takes in N
K = int(line[1]) #K = 3 - takes in K

#counter variable for future use
counter = 0 

bool_list = [True for t in range(N + 1)] #list of N ints
bool_list[0] = False #get rid of 0 (not considered)
bool_list[1] = False #get rid of 1 (not considered)

#true = prime; false = not prime

#sample input 1
#7 3
#2,3,4,5,6,7 
#cross 2,4, then 3

#sample input 2
#15 12
#2,3,4,5,6,7,8,9,10,11,12,13,14,15
#cross 2,4,6,8,10,12,14,3,6(DUP),9,12(DUP),15,5,7

x = 2 #2 - N range
for x in range(N + 1): #x=2 true

    if (bool_list[x] == False): #when the number isn't prime
        continue
    y = x #y = 2; making y = x because we're incrementing by its multiples
    while y <= N: #when number is prime, 2 < 15
        if (bool_list[y] == False): 
            y += x #increment
            continue #next iteration
        
        bool_list[y] = False #2 becomes false
        #print(y, bool_list[y]) 
        counter += 1 #track of K counter
        
        if (counter == K): #when counter hits K
            print(y) #print y
            exit()
        
        y += x #increment by 2
    #print(bool_list)
        