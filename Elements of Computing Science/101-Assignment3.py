#Code developed by Areege Chaudhary (10197607): November 6, 2015

#This code asks the user to input their name and string and then determines whether or not that string is a palindrome,
#and if any letters in the string are letters of the user's name. If not, it prints out the number of characters in the
#string. If the user enters an empty string, it asks the user to re-enter it. If at any point the user types the word 'quit', the program terminates.


#ask user to input their name (Part 1)
name=str(input("What is your name?"))
name_case=name.casefold()

#if the user enters quit during this input point, end the script (Part 3)
if name_case=='quit':
    quit()

while len(name)>=0:
    
#ask user to input a string
    S=str(input("Enter a string: "))
    #alter the string so that it changes all the characters to lowercase 
    S=S.casefold()
    #remove the spaces in the string
    S=S.replace(" ","")
   
#if the user enters quit, quit the program (Part 3)
    if S=='quit':
        quit()

#if the user enters an empty string, return back to the top of the while loop (Part 2b)
    if S == "":
        print("You need to re-enter the string.")
        continue
    
#check to see if any of the letters in the name are in the string (Part 2b)
    if len(set(S) and set(name_case)) > 0:
        print("This string contains letters of your name.")

#Check to see if the string entered is a palindrome (Part 2a)
    if len(S)>1:
        #reverse the order of the characters in the string that was inputted by the user 
        rev_S=reversed(S)
        #if-else statment telling the user whether the inputted string is a palindrome
        if list(S)==list(rev_S):
            print("This string is a palindrome.")

#print length of string if it doesn't satisfy any of the above conditions (Part 2d)
    else:
        print("The number of characters in your string is: ",len(S))
