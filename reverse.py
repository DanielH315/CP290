import sys

def reverse_valid():
    

def check_valid():


def main():
    
    first_l= sys.stdin.readline().strip()
    output = 1 #print cases
    
    while (first_l != None):
        list_input = first_l.split(" ")
        m = int(list_input[0]) #num of location
        n = int(list_input[1]) #num of roads connecting
        adj = [[] for j in range(m)] #adjacent list, 
        #index 0 should store 1, index 1 should store 2
        
        for x in range(n):
            ab = sys.stdin.readline().split()
            a = int(ab[0])
            b = int(ab[1])
            adj[a].append(b) #[[1], [2], []]
        
        #check if the graph is SCC
        #if it is, then VALID
        #but if it's not, then I try to reverse each edge (one at a time)
        #check SCC
        
        #everything doesn't work then invalid
        
        print("Case {}:".format(output)) #printing cases
        
        output += 1 #updating each case number

if __name__ == "__main__":
    main()

