#----------------------------------------------------------------------------------
# This script is for Assignment 3 of the winter term of CISC121.
# Script written by: Areege Chaudhary (Student number: 10197607)
# Last modified on March 11, 2016
#----------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------
# This function reads two text files containing lists from two different Netflix
# profiles. It then builds a linked list using the lists from the two profiles
# and creates a menu for the user. Using the menu, the user can view the lists
# belonging to Profiles 1 and 2,  merge the lists together, remove duplicate items,
# add a new movie to the specified watch list in a specific location and delete an
# item from one of the watch lists.
#----------------------------------------------------------------------------------

def main():
    profile1 = readFile('D:/Queens/CISC121/profile1.txt')
    profile2 = readFile('D:/Queens/CISC121/profile2.txt')
    linkedProfile1 = buildList(profile1)
    linkedProfile2 = buildList(profile2)
    menu(linkedProfile1, linkedProfile2)

#----------------------------------------------------------------------------------
# This function takes a file path in string format as input, reads the .txt file
# and creates a list containing the titles written in that profile's text file.
#----------------------------------------------------------------------------------
def readFile(string):
    lis = []
    with open(string, "r") as in_file: #open file
        for line1 in in_file:
            lis.append(line1) #removes empty lines
        for index in range(0, len(lis)-1): #gets rid of extra characters at the end of each title                                     
            lis[index] = lis[index][:-1]   #(created when reading the file)
    in_file.close()
    return lis #the created list is appended to the toReturn list so it can be returned as a single list

#----------------------------------------------------------------------------------
# This function is used to prevent repetition in the rest of the code. It prints
# out the different options that the user has for the menu function.
#----------------------------------------------------------------------------------
def menuOptions():
    print("Welcome to the MENU :)")
    print("Enter '1' to view Profile 1's list:")
    print("Enter '2' to view Profile 2's list:")
    print("Enter '3' to merge the two profiles' lists:")
    print("Enter '4' to remove the duplicates:")
    print("Enter '5' to add a movie to a list:")
    print("Enter '6' to delete a movie from a list:")
    print("Type 'quit' to quit")


#----------------------------------------------------------------------------------
# This function takes two parameters: linkedProfile1 and linkedProfile2. These
# parameters are used as the inputs. It then shows the user the different options
# that they could choose to modify the profile lists.
#----------------------------------------------------------------------------------
def menu(linkedProfile1, linkedProfile2):
    menuOptions() #call the options function to list options availible to user
    continueOn = True #used to continue the function until user types 'quit'
    while (continueOn == True):
        print("Enter 'menu' to re-display the options:")
        userInput = input()
        # User can re-display options if desired. 
        if (userInput == 'menu'):
            menuOptions()
        if (userInput == 'quit'):
            continueOn = False
        # Print profile 1
        if (userInput == '1'):
            printTree(linkedProfile1)
        # Print profile 2
        if (userInput == '2'):
            printTree(linkedProfile2)
        # If user selects option 3, navigate to mergeList function
        if (userInput == '3'):
            linkedProfile1, linkedProfile2 = mergeList(linkedProfile1, linkedProfile2)
        # If user selects option 4, navigate to removeDupes function
        if (userInput == '4'):
            linkedProfile1 = removeDupes(linkedProfile1)
        # If user selects option 5, navigate to addMovies function
        if (userInput == '5'):
            linkedProfile1, linkedProfile2 = addMovies(linkedProfile1, linkedProfile2)
        # If user selects option 6, navigate to deleteMovies function
        if (userInput == '6'):
            linkedProfile1, linkedProfile2 = deleteMovies(linkedProfile1, linkedProfile2)
    quit()

#----------------------------------------------------------------------------------
# This function has two parameters: a linked list and a movie/TV show title. It
# adds the title to the end of the linked list.  
#----------------------------------------------------------------------------------
def addToEnd(linkedList, title):
    startNode = linkedList
    newNode = {'data':None,'next':None}
    #if the node/root of the tree is empty, this part of the code handles it
    if (linkedList == None):
        linkedList = {'data':title,'next':newNode}
        return linkedList
    #if the provided linkedList is not empty, it navigates to the last node in the list
    #and then adds the data, and the 'next' empty node to it
    elif (linkedList != None):
        while (linkedList['next'] != None):
            linkedList = linkedList['next']
        linkedList['data'] = title
        linkedList['next'] = newNode
    #return an indicator to the first node in the linked list
    return startNode

#----------------------------------------------------------------------------------
# This function has one parameter: a linked list. It takes that list as an input
# and creates a linked list using the addToEnd function. It also removes the empty
# nodes that are created by the addToEnd function. It then returns an indicator
# to the beginning of the built linked list
#----------------------------------------------------------------------------------
def buildList(lis):
    linkedList = None
    for index in range(0, len(lis)):
        linkedList = addToEnd(linkedList, lis[index])
    #cleans up the 'None' nodes 
    startNode = linkedList
    while ((linkedList['next']) != None):
        if ((linkedList['next']['data'] == None) and (linkedList['next']['next'] != None)):
            linkedList['next'] = linkedList['next']['next']
        if ((linkedList['next']['data'] == None) and (linkedList['next']['next'] == None)):
            linkedList['next'] = None
        if (linkedList['next'] != None):
            linkedList = linkedList['next']
    return startNode
    
#----------------------------------------------------------------------------------
# This function has one parameter: a linked list. It takes that linked list as input
# and then prints the data within that linked list using numbers that represent the
# index of the data. It then returns a count representing the length of the list
#----------------------------------------------------------------------------------
def printTree(linkedList):
    count = 1
    #if the profile is empty, this part of the code handles it
    if (linkedList['data'] == None):
        print ('This profile is empty.')
        return None
    #if only one element is to be printed
    if ((linkedList != None) and (linkedList['next']) == None):
        print (str(count) + ':' , str(linkedList['data']))
        return count
    #if the linked list contains more than one item
    while (linkedList['next'] != None):
        #if the items are not in the list
        if (linkedList['data'] != None):
            print (str(count) + ':' , str(linkedList['data']))
            count += 1
        #moving through the linked list
        if (linkedList['next'] != None):
            linkedList = linkedList['next']
        # Handles printing the last element in the linked list
        if (linkedList['next'] == None):
            print (str(count) + ':' , str(linkedList['data']))
            count += 1
            return count
    if (linkedList['next'] == None):
        return count
        
#----------------------------------------------------------------------------------
# This function has two parameters: two linked lists. It then merges them together
# at an index the user selects. It then returns the merged linked list and makes the
# other list empty.
#----------------------------------------------------------------------------------
def mergeList(lis1, lis2):
    #the first node in an empty linked list is defined so it can be returned when the
    #lists are merged
    clearList = {'data':None,'next':None}
    x = printTree(lis1) #signifies max index at which second list can be merged
    userInput = input('Enter an numerical value where you would like the list to merge:')
    firstNode = lis1
    #if merge into first index position
    if ((int(userInput) == 1)):
        firstNode = lis2
        while (lis2['next'] != None):
            lis2 = lis2['next']
        lis2['next'] = lis1
        return firstNode, clearList
    #if the merge index is greater than the first position but less than length of list
    if ((int(userInput) < x) and (int(userInput) > 1)):
        firstNode = lis1
        counter = int(userInput)
        count = 2
        while (count != counter):
            lis1 = lis1['next']
            count += 1
        temp = lis1['next']
        lis1['next'] = lis2
        while (lis1['next'] != None):
            lis1 = lis1['next']
        lis1['next'] = temp
        return firstNode, clearList
    #if neither cases above are met, prompt user to enter valid input
    else:
        print ('Please enter a valid input:')
        mergeList(lis1, lis2)

#----------------------------------------------------------------------------------
# This function has one parameter: a linked list. It then modifies the list so
# that it removes duplicate data elements and returns the list.
#----------------------------------------------------------------------------------
def removeDupes(lis):
    #if list is empty, return None
    if lis == None:
        return None
    startNode = lis
    iterate = lis
    while (iterate['next'] != None):
        current = iterate
        #if the duplicate element is not the last element
        while ((current != None) and (current['next'] != None)):
            if (iterate['data'] == current['next']['data']):
                current['next'] = current['next']['next']
            current = current['next']
        #if the duplicate element is the last element
        if (iterate['next'] != None):
            iterate = iterate['next']
    return startNode

#----------------------------------------------------------------------------------
# This function has two parameters: two linked lists. It then asks the user what
# list to add new titles to and where in the list they would like to add it to.
# It then returns both the modified and unmodified lists. 
#----------------------------------------------------------------------------------
def addMovies(lis1, lis2):
    profile = int(input("Enter '1' to add a title to Profile 1 and '2' to add a title to Profile 2:"))
    if ((profile != 1) and (profile != 2)):
        print("Please enter a valid profile:")
        addMovies(lis1, lis2)
    #Determines which list to modify
    if (profile == 1):
        lis = lis1
    if (profile == 2):
        lis = lis2
    x = printTree(lis)
    userInput = input("Enter a index value at which you would like to add the title:")
    movieToAdd = input("Enter the title you wish to add:")
    movieNode = {'data': movieToAdd, 'next': None}
    firstNode = lis
    #if the profile being added to is empty
    if (firstNode['data'] == None):
        if (profile == 1):
            return movieNode, lis2
        if (profile == 2):
            return lis1, movieNode
    #if new title is being added to index 1
    if ((int(userInput) == 1)):
        firstNode = movieNode
        movieNode['next'] = lis
        if (profile == 1):
            return firstNode, lis2
        if (profile == 2):
            return lis1, firstNode
    #if new title is being added to indexes other than 1
    if ((int(userInput) < x) and (int(userInput) > 1)):
        firstNode = lis
        counter = int(userInput)
        count = 2
        #moving through the linked list (up to index where inserting)
        while (count != counter):
            lis = lis['next']
            count += 1
        #re-arranges indicators for data insertion
        temp = lis['next']
        lis['next'] = movieNode
        lis = lis['next']
        lis['next'] = temp
        #returns the modified lists returning modified lists
        if (profile == 1):
            return firstNode, lis2
        if (profile == 2):
            return lis1, firstNode
    #error input check
    else:
        print ('Please enter a valid input:')
        mergeList(lis, lis2)

'''
Input:
    Takes two linked lists as inputs and lets the user delete data from the selected profile
Output:
    Returns modified linked lists
'''
#----------------------------------------------------------------------------------
# This function has two parameters: two linked lists. It then lets the user delete
# titles from the selected profile and returns the modified linked list
#----------------------------------------------------------------------------------
def deleteMovies(lis1, lis2):
    profile = int(input("Enter '1' to delete from Profile 1 and '2' to delete from Profile 2:"))
    #error input check
    if ((profile != 1) and (profile != 2)):
        print('Please enter a valid profile:')
        deleteMovies(lis1, lis2)
    if (profile == 1):
        lis = lis1
    if (profile == 2):
        lis = lis2
    movie = int(input("Enter the number of the title you would like to delete:"))
    startNode = lis
    #if title to be deleted is at index 1 
    if (movie == 1):
        lis = lis['next']
        if (profile == 1):
            return lis, lis2
        if (profile == 2):
            return lis1, lis
    #moving through the array up to index that will be deleted
    for i in range(0,movie-2):
        if (lis['next'] == None):
            print('There is no movie at that index.')
            return lis1, lis2
        lis = lis['next']
    #re-arranges indicators to remove undesired node
    if ((lis['next']['next']) != None):
        lis['next'] = lis['next']['next']
    elif ((lis['next']['next']) == None):
        lis['next'] = None
    #returns modified list
    if (profile == 1):
        return startNode, lis2
    if (profile == 2):
        return lis1, startNode
    


#calls main() function to begin executing script
main()
