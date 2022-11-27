#Author: Daniel Hong
#It is okay to post my anonymized solution

import sys

def delivery(incoming_list, capacity):
    #After sorting the negatives/positives, we now deliver:
    
    remaining = capacity #we have a remaining variable to keep track of how many letters remaining
    
    for i in reversed(range(len(incoming_list))): #we're reversing the incoming list so that we deliver to farthest location first
        
        if capacity < incoming_list[i][1]: #checking if capacity of truck is less than how many we need to deliver
            incoming_list[i][1] -= capacity #if so, we deliver however much we can then go back to the post office
            return #return so we go back to office for more letters
        
        #assuming capacity is greater than the number of letters we need to deliver:
        capacity -= incoming_list[i][1] #remaining letters after delivery
        incoming_list.remove(incoming_list[i]) #after we finish a delivery, we can remove the location from the delivery list
    

def main(): #main function
    input_list = sys.stdin.readline().split(" ") #read first line input
    
    N = int(input_list[0]) #N = number of delivery addresses
    K = int(input_list[1]) #K = carrying capacity of truck
    
    positive_list = [] #initializing a list for positive location values
    negative_list = [] #initializing a list for negative location values
    
    delivery_list = [] #initializing a list to list out the deliveries needed
    
    for x in range(N):
        info_list = sys.stdin.readline().split(" ") #reading the locations and letters needed to deliver
        delivery_list.append(info_list) #appending our locations and letters to our delivery list
    
    delivery_list = [[int(float(j)) for j in i] for i in delivery_list] #converts the list of lists strings to integers (source: Stackoverflow)
    
    for y in range(len(delivery_list)):
        if delivery_list[y][0] < 0:
            negative_list.append(delivery_list[y]) #if our location is negative, we append the negative list
        else:
            positive_list.append(delivery_list[y]) #if our location is positive, we append the positive list
    
    negative_list.sort(reverse=True) #we sort the negative list in descending order (i.e. -100 < -10 but -100 is farther in terms of location)

    total = 0 #total distance variable
    
    while negative_list: #going through the negative list
        total += (negative_list[len(negative_list) - 1][0] * 2) #calculating distance there/back
        delivery(negative_list, K) #updating our list by doing the delivery/calling delivery function
    
    total = abs(total) #make negative into positive number for total distance calculations
    
    while positive_list: #going through the positive_list
        total += (positive_list[len(positive_list) - 1][0] * 2) #calc distance there/back
        delivery(positive_list, K) #updating our list by doing the delivery/calling delivery function
    
    print(total) #print the final distance 
    
if __name__ == "__main__":
    main()