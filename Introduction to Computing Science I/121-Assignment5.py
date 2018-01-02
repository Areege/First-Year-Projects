import urllib.request #imports library to be used in readHtml() function

#-----------------------------------------------------------------------------------
# This function takes data from an online resource and creates a list of strings.
# It then calls the manipulateList(aList) function.
#-----------------------------------------------------------------------------------
def readHtml():
    response = urllib.request.urlopen("http://www.cs.queensu.ca/home/cords2/data121.txt")
    html = response.read()
    data = html.decode('utf-8').split()
    return manipulateList(data)

#-----------------------------------------------------------------------------------
# This function takes a list as a parameter. It converts the string elements of
# the list to floats and then creates sub-lists of three elements each (to group
# together each item's data).
#-----------------------------------------------------------------------------------
def manipulateList(aList):
    tempList = [] #temp. list
    finalList = [] #final list
    initialList = list(map(float, aList)) #strings to floats
    while len(initialList) > 0: 
        for value in range(0,3):
            tempList.append(initialList[value]) #append 1st 3 elements in the initial list 
        del initialList[0:3]                    #to temp. list and deletes them from initial
        finalList.append(tempList) #append elements in temp. list to final
        tempList = [] #clear contents of temp. list
    return finalList

#-----------------------------------------------------------------------------------
# This function creates an empty binary search tree.
#-----------------------------------------------------------------------------------
def createEmptyTree():
    return None

#-----------------------------------------------------------------------------------
# This function takes data from a list and adds a node to the binary search tree.
# Its parameters include a binary search tree, an item ID, a price and a value for
# how many of those items are still in stock.
#-----------------------------------------------------------------------------------
def add(tree, partID, price, stock): 
    if tree == None:
        #'data' node holds a list rather than a single value
        return {'data':[partID, price, stock], 'left':None, 'right':None} 
    elif partID < tree['data'][0]:
        tree['left'] = add(tree['left'],partID, price, stock)
        return tree
    elif partID > tree['data'][0]:
        tree['right'] = add(tree['right'],partID, price, stock)
        return tree
    else:
        return tree
    
#-----------------------------------------------------------------------------------
# This function creates a list of all the items in the binary search tree in sorted order.
# *Taken from the binary search tree python file posted on the CISC121 moodle page.*
#-----------------------------------------------------------------------------------
def toList(tree):
    if tree == None:
        return []
    else:
        return toList(tree['left']) + [tree['data']] + toList(tree['right'])

#-----------------------------------------------------------------------------------
# This function takes a binary search tree as a parameter and prints out all it's
# contents. In this case, it prints out the item ID, how much that item costs and
# how many of those items are left.
#-----------------------------------------------------------------------------------
def printItems(tree):
    #create a list of all items using data from the binary search tree
    items = toList(tree['left']) + [tree['data']] + toList(tree['right']) 
    if len(items) == 0:
        print("There are no items left in stock. Sorry!")
    else:
        #use a for loop to print each item in the list created
        for item in range(0,len(items)): 
            #print each item in the list on a new line
            print("Item #"+str(int(items[item][0]))+": $"+str(format(float(items[item][1]),'.2f'))
                  +" each and "+str(int(items[item][2]))+" in stock.")

#-----------------------------------------------------------------------------------
# This function uses the toList function to create a list of all data elements of the
# binary search tree and then iterates through the list to count the number of items
# in stock that cost under $50.00. It takes a BST as a parameter.
#-----------------------------------------------------------------------------------
def fifty(tree):
    count = 0
    #creates a list using the toList function
    items = toList(tree['left']) + [tree['data']] + toList(tree['right'])
    if len(items) == 0: #if BST is empty
        print("There are currently no products in stock that cost under $50.00. Sorry! :(")
    else:
        #iterates through list
        for item in range(0, len(items)):
            if items[item][1] < 50:
                count = count + items[item][2] #include stock values
    print("There are currently "+str(int(count))+" items that cost less than $50.00.")

#-----------------------------------------------------------------------------------
# This function searches the tree and prints out a price for an item ID that a
# user enters. It takes a binary search tree and an item ID as a value to search for
# as parameters.
#-----------------------------------------------------------------------------------
def price(tree, value): 
    if tree == None:
        return "Hmm... Can't seem to find anything. Are you sure you entered the right item ID?"
    #if ID entered is the ID in the data node searched return ...
    elif value == tree['data'][0]: 
        return "The price of item "+ str(value) + " is $" + str(format(float(tree['data'][1]),'.2f')) + "."
    #if ID entered is less than ID in data node searched, search left tree
    elif value < tree['data'][0]: 
        return price(tree['left'],value)
    #if ID entered is less than ID in data node searched, search right tree
    elif value > tree['data'][0]: 
        return price(tree['right'],value)

#-----------------------------------------------------------------------------------
# This function increases the prices of all items that don't end in ".97" by 10%.
# It then prints all of the items onto the screen. It takes a binary search tree
# as a parameter.
#-----------------------------------------------------------------------------------            
def increase(tree):
    #create list using toList function
    items = toList(tree['left']) + [tree['data']] + toList(tree['right'])
    if len(items) == 0:
        print("Sorry...There doesn't seem to be any data in our system.")
    else:
        #iterate through list to find prices that end in .97
        for item in range(0, len(items)):
            #format price values to round them before checking
            if str(format(items[item][1],'.2f'))[-2:] != '97':
                #increase price by 10%
                items[item][1] = ((items[item][1])*(1+0.10))
    printItems(tree)

#-----------------------------------------------------------------------------------
# This function creates a menu for the user. The user inputs a, b, c or d and the
# function calls the corresponding function. It takes a binary search tree as a
# parameter.
#-----------------------------------------------------------------------------------
def menu(tree): 
    print("Welcome to the menu! Choose one of the following options.")
    print("Enter 'A' to see all of the items currently in stock:")
    print("Enter 'B' to find out how many items sell for under $50.00:")
    print("Enter 'C' to check the price of an item:")
    print("Enter 'D' to increase item prices by 10%:")
    getInput = False
    while getInput == False:
        userInput = input().lower()
        if userInput == 'a':
            printItems(tree) 
            getInput = True
            menu(tree)
        if userInput == 'b':
            fifty(tree)
            getInput = True
            menu(tree)
        if userInput == 'c':
            print("Please enter the ID of an item to see it's price:")
            value = int(input())
            print(price(tree,value)) 
            getInput = True
            menu(tree)
        if userInput == 'd':
            increase(tree)
            getInput = True
            menu(tree)
        else:
            print("Sorry! That is not a valid input. Please try again!")

#-----------------------------------------------------------------------------------
# This function creates the binary search tree using the provided data and then
# launches the menu function.
#-----------------------------------------------------------------------------------    
def main():
    productTree = createEmptyTree()
    for item in range(0, len(info)):
        productTree = add(productTree, info[item][0], info[item][1], info[item][2])
    menu(productTree)

info = readHtml() #setting data as global variable 'info' for easy access

main()
