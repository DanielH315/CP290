#Author: Daniel Hong
#It is okay to post my anonymized solution
#The following code was done by referencing Favtutor and GeeksforGeeks BFS algorithm/lectures

#https://purdue.kattis.com/courses/CS290-CP1/2022-Fall/assignments/qvmspa/problems/buttonbashing
import sys

def BFS_helper(time, buttons): #BFS function 
    
    if time == 0: #preliminary checker to make sure when time is 0, we print "0 0"
        return 0,0
    
    max_seconds = 3601 #var used for cases above 3600 secs
    button_presses = 0 #button presses counter
    queue = [(0,0)] #queue to keep track 
    visited = [] #visited list to keep track
    
    while queue: #loop to visit each node
        node, counter = queue.pop(0) #setting our curr node and counter to the first elem in queue

        for neighbor in buttons: 
            n = min(3600, max(0, neighbor + node)) #checking between 3600 and the combination of the neighbor nodes to see which is smaller
            
            if n == time: #if n equals our desired time, then we can return our results
                return counter + 1, 0
            
            if n not in visited: #making sure we're not double checking nodes
                visited.append(n) #if not, then we add it to visited list so we dont double check n in the next iteration
                queue.append((n, counter + 1)) #queuing 
                
                if n > time and n < max_seconds: #checking the case of it going over the desired time
                    max_seconds = n #we just set our max to the bigger result
                    button_presses = counter + 1 #incrementing button press counter
    
    return button_presses, (max_seconds - time) #when we return, we can subtract to find the difference and print the result

def main():
    test_case = sys.stdin.readline() #reading the num of test cases
    test_case = int(test_case) #converting into integer

    for x in range(test_case): #for loop running for how ever many test cases
        first = sys.stdin.readline().split(" ") 
        num = int(first[0]) #storing num of buttons
        time = int(first[1]) #storing desired time
        
        second = sys.stdin.readline().split(" ")
        buttons = list(map(int, second)) #converting my list of str buttons into ints

        minimum, extra = BFS_helper(time, buttons) #calling BFS function
        print(minimum, extra) #printing the output
    
if __name__ == "__main__":
    main()

