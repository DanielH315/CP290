#Daniel Hong
#It is ok to post my anonymized solution
#9/2/22

import sys

#comments based on own test cases
N = int(sys.stdin.readline()) #N = 5; takes in input

world = sys.stdin.readline().split(" ") #reads and splits (worlds)
count = 0 #counter variable for future use

checker = int(world[-1])

if (N == 1): #if only 1 planet
    print(checker) #prints pop
    exit() #done

if (checker + 2) <= N: #thanos suicide case
    print(1) #print 1 
    exit()

t = 1
for t in range(len(world) - 1): #another suicide case [0,0,0,4]
    if int(world[t]) < (t-1): #must be a minimum
        #print(world)
        print(1)
        exit()
        
#world = [8,8,7,5,9,7] count = 17
#         0 1 2 3 4 5

i = len(world) - 1 # making i the length of the lists of world - 1
while i >= 0:
    #print(world[i]) 
    x = int(world[i]) #x is a variable that holds pop value of a world
    
    if i != 0: #if it's not 0, then we can safely look at the index of the next world
        y = int(world[i-1]) #9; y is a temp variable to compare the next world
        if x <= y: #x = 7, y = 9
            count += (y - x + 1) #we calculate the count which is next world - prev world + 1
            y = x - 1 #update y value
            if y < 0: #however, if we notice that there is a value that's negative, we know there's no perfect universe
                print(1) #exit
                exit()
            world[i-1] = y #updating pop if everything goes well

    i -= 1 #next world iteration
    #print(world, count)
print(count)