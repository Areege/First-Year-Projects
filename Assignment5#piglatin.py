#This program encrypts english to pig latin and decrypts pig latin to english

def Encrypt(string_input2): #function encrypts text from english to pig latin
    digits = ['0','1','2','3','4','5','6','7','8','9']
    latin = ""
    if_digits = False
    for word in string_input2: #for each word in the string
        #check to see if the "word" is a numerical value
        for ch in word:
            if ch in digits:
                if_digits = True
        #if the "word" is numerical, do the following:               
        if if_digits == True:
            latin += str((int(word)*4)+10)+" "
        #if the word is a string, do the following:
        else: 
            latin += word[1:]+word[0]+"ay"+" "
    return latin
        
def Decrypt(string_input2): #function decrypts text from pig latin to english
    digits=['0','1','2','3','4','5','6','7','8','9']
    english = ""
    if_digits = False
    for word in string_input2:#for each word in the string
        #check to see if the "word" is a numerical value
        for ch in word:
            if ch in digits:
                if_digits = True
        #if the "word" is numerical, do the following:               
        if (if_digits == True):
            english += str(int((int(word)-10)/4))+" "
        #if the word is a string, do the following:
        else:
            english += word[(len(word)-3)]+word[0:-3]+" "
    return english
        
def Read_script():
    inputOK = False
    while not inputOK:
        fileName = input("Please enter the name of the file you want to translate. Make sure you include the extension. ") #ask user to input file name
        try:
            inputFile = open(fileName, 'r') #open the text file
            string_input = inputFile.read() #convert the text file into a string
            inputOK = True
        except FileNotFoundError:
            print("That's not a valid file name. Try again!")
            
    string_input1 = string_input.casefold() #make all letters in the string lowercase
    string_input2 = string_input1.split(" ") #turn string into a list, elements seperated by word
    return string_input2

def Write_script(outputString): #function that writes the output string into a new text file
    file = open("chaudhary.txt", "w")
    file.write(outputString)
    file.close()
    print("Your translated text has been written into a new file.")
    quit()
        
def main():
    print("Welcome! Are you ready to translate some Pig Latin?!")
    new_string = Read_script() #call function that opens the file
    input_type = None
    while (input_type == None):
        check = False
        #ask user if they want to encrypt or decrypt the text
        input_type=input("Enter 'e' if  you want to translate to Pig Latin or 'd' if you want to translate to English: ")
        if (input_type == 'e'):
            latin_string = Encrypt(new_string) #call function that encrypts
            Write_script(latin_string) #call function that writes output string to file
            check = True
        if (input_type == 'd'):
            english_string = Decrypt(new_string) #call function that decrypts
            Write_script(english_string) #call function that writes output string to file
            check = True
        if (check == False): #input error checking
            print("Please enter either 'e' or 'd'.")
            input_type = None
        
main()                 
