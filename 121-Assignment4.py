#----------------------------------------------------------------------------------
# This script is for Assignment 4 of the winter term of CISC121.
# Script written by: Areege Chaudhary (Student number: 10197607)
# Last modified on March 26, 2016
#----------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------
# This script opens a text file that includes a maze-like grid that includes a starting
# position, an end position, obstacles and open spaces. It then converts the grid into
# a list of lists where each element in each sublist is a position on the grid
# called by (x,y). The program traverses through all the positions and finds a path
# to the ending position that avoids all obstacles (marked by the character '|').It
# then prints out the modified grid clearly showing the correct path from the start
# to the finish of the maze.
#-----------------------------------------------------------------------------------
def main():
    freeMouse(0,0)
    showPath()

#-----------------------------------------------------------------------------------
# This function opens the text file containing the grid maze and converts it to a
# list of lists that can be accessed and modified by other functions in the script.
# This function is called later on to declare the grid as a global variable so that
# it can be accessed easily through all of the functions.
#-----------------------------------------------------------------------------------
def readFile():
    with open("/Users/areegechaudhary/Desktop/grid.txt", "r") as in_file:
        grid2 = [] #final list
        grid1 = [] #temp list
        grid = [] #initial list
        for line in in_file:            #goes through each line in text file
            grid.append(line.strip())   #and appends it to initial list
    for string in range(0,len(grid)): 
        for char in range(0,len(grid[string])): #appends each character in each
            grid1.append(grid[string][char])    #string element in initial list   
        grid2.append(grid1)                     #to the final list then clears temp
        grid1 = []                              #list and repeats process with
    return grid2                                #all elements in initial list

#-----------------------------------------------------------------------------------
# This function prints out the grid. It modifies the list of lists created in the
# readFile function so that all characters are joined together and the final solution
# path is easy to see.
#-----------------------------------------------------------------------------------
def showPath():
    for index in range(0,len(grid2)): #iterates through each element in grid
        line = ''.join(grid2[index])  #and joins the characters together into
        print(line)                   #a string and prints it

#-----------------------------------------------------------------------------------
# This function takes a x,y postion as a parameter to use as a starting point. It
# then iterates through each position to the left, right, above and below the
# position it is currently in. As it goes through, it marks "X"s in positions that
# are part of the path to the end and "+"s in positions that are not part of the
# path and do not lead to the end position.
#-----------------------------------------------------------------------------------
def freeMouse(x,y):
    if grid2[y][x] == 'O': #if solution is reached, return true
        return True
    #if position is an obstacle or has already been visited, solution is not
    #reached and the statement returns false
    if (grid2[y][x] == '|') or (grid2[y][x] == '+') or (grid2[y][x] == 'X'):
        return False
    grid2[y][x] = 'X' #mark a potential position of the path to the outside
    a = False 
    b = False #setting variables to be used later
    c = False
    d = False
    if x > 0: #when x is greater than 0, check the position to the left
        a = freeMouse(x-1,y) 
    if x < len(grid2[0])-1: #when x is less than the last index number (in x direction), 
        b = freeMouse(x+1,y)#check the position to the right
    if y > 0: #when y is greater than 0, check the position above
        c = freeMouse(x,y-1)
    if y < len(grid2)-1: #when y is less than the last index number (in y direction), 
        d = freeMouse(x,y+1) #check the position below
    if (a != True) and (b != True) and (c != True) and (d != True): 
        grid2[y][x] = '+' #if position doesn't lead to outside, mark with a +
        return False
    else:
        return True
    
grid2 = readFile() #setting the grid as a global variable 

main()
