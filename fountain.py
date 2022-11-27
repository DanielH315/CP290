import sys

def main():
    
    NM = sys.stdin.readline().split(" ")
    N = int(NM[0])
    M = int(NM[1])
    
    S = [['.' for x in range(M)] for y in range(N)]
    
    #building the initial fountain
    for row in range(N):
        line = sys.stdin.readline().strip()
        for col in range(M):
            S[row][col] = line[col]
    
    col = 0
    
    for row in range(N):
        while col < M:
            #print(row, col)
            if S[row][col] == 'V' and (row + 1) < N: #out of bounds
                if S[row+1][col] == '#':
                    if col + 1 < M and S[row][col+1] == '.':
                        S[row][col + 1] = 'V'
                    if col - 1 >= 0 and S[row][col-1] == '.':
                        S[row][col - 1] = 'V'
                        col -= 2
                else:
                    S[row+1][col] = 'V'
                    
            col += 1
        col = 0
        
    for x in range(N):
        print("".join(S[x]))

if __name__ == "__main__":
    main()
