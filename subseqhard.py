import sys

def counting(sequence, length):
    
    freq = {} #dictionary to hold each value and its frequency
    total = 0
    result = 0
    empty = 0
    interesting = 47
    inc = 0
    
    while (inc < length):
        freq[total] = freq.get(total, empty) + 1
        total += sequence[inc]
        #print(freq)
        #subtract sum by interesting (47) to see if we hit a key in our freq
        diff = total - interesting
        if diff in freq:
            #print("total", total - interesting)
            check = total - interesting
            result += freq[check]
        
        inc += 1
    
    
    return result

def main():
    cases = sys.stdin.readline().strip()
    cases = int(cases)
    
    for x in range(cases):
        blank = sys.stdin.readline()
        
        length = sys.stdin.readline().strip()
        length = int(length)
        
        sequence = sys.stdin.readline().strip().split(" ")
        final_seq = list(map(int, sequence))
        
        result = counting(final_seq, length)
    
        print(result)

if __name__ == "__main__":
    main()
