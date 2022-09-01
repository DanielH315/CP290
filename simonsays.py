import sys

#comments based on Sample Input 1
N = int(sys.stdin.readline()) #N = 1

for _ in range(N):
    command = sys.stdin.readline().strip() #reads "Simon says smile."
    if command[0:10] == "Simon says": #substring 0:10 is "Simon says"
        print(command[10:]) #print everything after 'Simon says'
