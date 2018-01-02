#This program asks user to input names and outputs back the names that include their first letter in the rest of the name

def Check_valid_name(listCheck): #function checks to see if the name passes all conditions for being valid (no spaces or digits)
    listCheck = list(listCheck)
    invalid = [' ','1','2','3','4','5','6','7','8','9']
    for index in range(0,len(listCheck)):
        for index1 in range(0,len(invalid)):
            if (listCheck[index] in invalid[index1]):
                return False
    return True

def Check_name(checkName): #function checks to see if the first letter in the name is also in the rest of the name
    checkName = checkName.lower() #makes letters lowercase
    for index in range(1,len(checkName)):
        if (checkName[0] == checkName[index]):
            return True

def Print_checked_names(finalNames):
    #checks to make sure that duplicate names aren't printed
    noDuplicates = len(finalNames)
    for i1 in range(0,noDuplicates-1):
        check = 0
        i2 = 0
        while (i2 < noDuplicates-1):
            if (finalNames[i1] == finalNames[i2]):
                check += 1
            if (check > 1):
                del finalNames[i1]
                noDuplicates -= 1
                check -= 1
            i2 += 1
    #print the names that pass the Check_name function
    answer1 = ("The "+str(len(finalNames))+" name(s) that pass 'my check' are:")
    print(answer1)
    answer2 = ''
    for index in range(0,len(finalNames)):
        if (index == 0):
            answer2 = ''.join(finalNames[index])
        if (index > 0):
            answer2 = answer2 + ', ' + ''.join(finalNames[index])
    print(answer2)

def main():
    name = []
    finalNames = []
    count = 1
    userInput = None
    userInput1 = None
    while (userInput1 != "quit"):
        userInput = input('Please input name '+str(count)+': ') #ask user to input a name
        userInput1 = userInput.casefold() #lowercase
        if (Check_valid_name(userInput) == False): #check to see if the input is invalid
            print('Sorry! Invalid name. It cannon contain numbers nor spaces, try again!')
        if (Check_valid_name(userInput) == True):
            name.append(userInput)
            count += 1
    for index in range(0,len(name)):
        validity = Check_name(name[index]) 
        if (validity == True):
            finalNames.append(name[index])
    Print_checked_names(finalNames) #call print function

main()
