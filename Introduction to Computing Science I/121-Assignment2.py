#----------------------------------------------------------------------------------
# This script is for Assignment 2 of the winter term of CISC121.
# Script written by: Areege Chaudhary (Student number: 10197607)
# Last modified on February 11, 2016
#----------------------------------------------------------------------------------

#----------------------------QUESTION #2------------------------------------------
# This function is a modification of the BinarySearch code (taken from the Sample
# Code section on the course Moodle). The parameters are a list of values and a
# "target" value (the value you want to find). It first counts how many times the target
# value appears in the collection and then finds the index value of the first
# appearance of the target value in the collection. It then returns that index number
# and the number of times the target value appears.
#----------------------------------------------------------------------------------
def modBinary(collection, target):
    low = 0
    high = len(collection) -1
    lowCount = 0 #low count and highcount are variables used in the counting
                 #section of the code
    highCount = len(collection) -1
    targetCount = 0 #number of times the target appears in the collection
    #counting how many times the target value appears 
    while highCount >= lowCount:
        if (target == collection[highCount]):
            targetCount = targetCount +1 #add 1 to targetCount value
            highCount = highCount -1 #get rid of the last value in the collection
        if (target != collection[highCount]):
            highCount = highCount -1 #get rid of the last value in the collection
    #figuring out the minimum index value that the target is found in
    while high >= low:
        mid = (high + low) // 2
        if (target == collection[mid]):
            return mid, targetCount #returns the items
        if (target < collection[mid]):
            high = mid - 1   #search left half
        else:
            low = mid + 1    #search right half
    return -1

#----------------------------QUESTION #3------------------------------------------
# This function takes one parameter which is the full file path of the text file
# you want to sort. It then opens that text file and converts each line into an
# element of a single list. The next part of the code is a modified version of
# the BubbleSort code found on the course Moodle. This arranges each string element
# based on how many characters there are in that string. Then, the final, sorted list
# is printed. 
#----------------------------------------------------------------------------------
def sortNames(filePath1):
    with open(filePath1) as in_file:
        queensHopefuls = in_file.read().splitlines() #converts text file into a list
    #we don't need to go to the end of the list with each iteration, so end will change over time.
    end = len(queensHopefuls) -1
    #switch keeps track of whether or not any swaps were made during an iteration
    switch = True 
    while (switch == True):
        #this starts a new iteration at the start of the list
        #switch begins as false and turns true if and only if a swap is made
        switch = False
        for i in range(0, end):
            if len(queensHopefuls[i]) > len(queensHopefuls[i+1]): #checks to see which element
                                                                  #has more characters
                #re-arranges the order
                queensHopefuls[i], queensHopefuls[i+1] = queensHopefuls[i+1], queensHopefuls[i]
                switch = True
        #the end point of our next iteration is one less than it was in the previous one
        end = end - 1
    print(queensHopefuls)

#----------------------------QUESTION #4.1------------------------------------------
# This function takes two parameters: a list of values and a target value. It is a
# modification of the BinarySearch code taken from the course Moodle. If the target
# value is not a value in the collection given, it returns the index value that is
# one value lower than what the index value would be if the target value was actu-
# ally part of the collection. 
#----------------------------------------------------------------------------------
def floor(collection, target):
    low = 0
    high = len(collection) -1
    while high >= low:
        mid = (high + low) //2
        if (target == collection[mid]):
            return mid    #found the item
        if (target < collection[mid]):
            if (target < collection[mid-1]):
                high = mid -1 #search left half
            if (target > collection[mid-1]):
                mid = mid -1 
                return mid #return the value one lower than the mid
        if (target > collection[mid]):
            if (target < collection[mid+1]):
                return mid 
            if (target > collection[mid+1]):
                low = mid + 1 #search right half
    return -1   #if not found

#----------------------------QUESTION #4.2------------------------------------------
# This function takes two parameters: a list of values and a target value. It is a
# modification of the BinarySearch code taken from the course Moodle. If the target
# value is not a value in the collection given, it returns the index value that is
# one value greater than what the index value would be if the target value was actu-
# ally part of the collection. 
#----------------------------------------------------------------------------------
def ceil(collection, target):
    low = 0
    high = len(collection) -1
    while high >= low:
        mid = (high + low) //2
        if (target == collection[mid]):
            return mid    #found the item
        if (target < collection[mid]):
            if (target < collection[mid-1]):
                high = mid -1 #search left half
            if (target > collection[mid-1]):
                return mid
        if (target > collection[mid]):
            if (target < collection[mid+1]):
                mid = mid +1
                return mid #return the value one higher than the mid
            if (target > collection[mid+1]):
                low = mid + 1 #search right half
    return -1   #if not found
