
 Download file
import sys

#experiencing TLE so I use Binary Search to cut down
#referenced G4G Binary Search

def BEAT_TLE(investments, days, minimum):
    profit = 0
    
    for i in investments:
        specific = (i[0] * days) - i[1]

        if specific > 0:
            profit += specific
        if profit >= minimum:
            #print(days)
            return 1
    return 0
    

def main():
    
    options_min = sys.stdin.readline().strip().split(" ")
    
    options = int(options_min[0])
    minimum = int(options_min[1])
    
    investments = []
    
    for x in range(options):
        profit, cost = sys.stdin.readline().split(" ")
        profit = int(profit)
        cost = int(cost)
        investments.append([profit, cost])
    
    days = 0
    low = 0
    high = 2
    
    while BEAT_TLE(investments, high, minimum) == 0:
        low = high
        high *= 2
    
    while low < high : #BINARY SEARCH
        middle = (low + high) // 2

        if BEAT_TLE(investments, middle, minimum) > 0:
            high = middle
        else:
            low = middle + 1
    
    print(low)
    
if __name__ == "__main__":
    main()
