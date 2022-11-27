import sys

#Referenced G4G Longest Common Subsequence

#def print2d(table, string):   
#    print("      a  b  c  d  e  f  g  h  i  j  k  l  m  n  o  p  q  r  s  t  u  v  w  x  y  z")
#    for x in range(len(dp)):
#        print(string[x - 1], table[x])
#    print()

def helper(alphabet, string, a_len, s_len, table):

    #print2d(table, string) - This called my commented out print function to help me better visualize the table
    
    #check to make sure we don't loop again
    if a_len == 0 or s_len == 0:
        return 0
    
    #making sure I'm not rechecking a cell
    if (table[s_len][a_len] == -1):

        #going backwards
        #start at bottom right of 2D array, work our way up to top left
        if (string[s_len - 1] == alphabet[a_len - 1]): #match? -> then...
            table[s_len][a_len] = helper(alphabet, string, a_len - 1, s_len - 1, table) + 1
            return table[s_len][a_len] 
        
        top = helper(alphabet, string, a_len, s_len - 1, table)
        left = helper(alphabet, string, a_len - 1, s_len, table)

        if top > left: #find out which one is bigger, then table at index is set it to that
            table[s_len][a_len] = top
        else:
            table[s_len][a_len] = left

    else:
        return table[s_len][a_len]
    
    return table[s_len][a_len]

def main():
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    string = sys.stdin.readline().strip() #read input
    
    table = [[-1 for x in range(len(alphabet) + 1)] for y in range(len(string) + 1)] #table of 0's based on lengths
    result = 26 - helper(alphabet, string, len(alphabet), len(string), table)
    
    print(result)
    
if __name__ == "__main__":
    main()
