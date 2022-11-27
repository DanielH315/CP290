import sys

#PREFIX SUM PROBLEM
#Saw this problem before

def helper(array, divisor):
    
    total = 0
    result = 0
    temp = []
    
    for x in range(divisor):
        temp.append(0)
    temp[0] = 1

    for element in array:
        total += element
        remainder = total % divisor
        result += temp[remainder]
        temp[remainder] += 1
    
    return result
    
    
def main():
    test_cases = sys.stdin.readline().strip()
    test_cases = int(test_cases)
    
    for cases in range(test_cases):
        first = sys.stdin.readline().strip().split(" ")
        divisor = int(first[0])
        length = int(first[1])
        
        array = sys.stdin.readline().strip().split(" ")
        array = list(map(int, array)) #elements of sequence
        
        result = helper(array, divisor)
        
        print(result)
    
    
if __name__ == "__main__":
    main()
