#Author: Daniel Hong
#It is okay to post my anonymized solution
#I tried to go through the bisection route by using helper functions but was struggling too much with it
#With the TA's suggestions, I decided working backwards was efficient enough and that I could break my program the instant I knew certain citations weren't fit for the H-index

import sys

def main():
    N = int(sys.stdin.readline()) #reading 
    
    citations = [] #creating a list for the citations

    while True: #while loop to traverse through the citations
        c = sys.stdin.readline() #read the line and store in c
            
        if c == None or c == '' or c == '\n': #conditional statement to break the while loop
            break
        
        citations.append(c) #appending each citation to my list
    
    final_list = [int(i) for i in citations] #converting list of strings to list of integers
    final_list.sort(reverse=True) #sorting the list in reverse order because I want to go via monotonic approach (keep track of what works until it doesn't work then we break!)
    
    H = 0 #H-index variable counter
    for x in range(0, N): #for loop where we're going through the # of papers
        if final_list[x] >= (x+1): #we compare the num of citations with (x+1) papers  
            H += 1 #we increment by 1
        elif final_list[x] < (x+1): #if less, we break
            break
        else: #just in case, in any other case that I didn't account for, we break
            break
    
    print(H)
    
if __name__ == '__main__':
    main()
