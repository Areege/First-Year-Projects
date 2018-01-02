#----------------------------------------------------------------------------------
# This script is an adventure game (assignment one) for the winter term of CISC121.
# Script written by: Areege Chaudhary (Student number: 10197607)
# Last modified on January 26, 2016
#----------------------------------------------------------------------------------
import time #imports the time library, this allows the program to pause for a
            #set amount of time before moving on to the next statement in the code

import random #imports the random library

#----------------------------------------------------------------------------------
# This function starts off the program. It prints the general instructions of the
# game to the user and creates the data structure that will hold the player stat-
# istics. It then calls the startingRoom function, which starts off the game's
# storyline.
#----------------------------------------------------------------------------------
def welcome():
    stats={'lives': 9, 'items': [], 'money': 0, 'visits': 0}
    print("Welcome to the game that involves talking cats!")
    print("If at any point you want to quit the game, enter 'Quit'.")
    print("Enter 'N' to go north, 'S' to go south, 'E' to go east, 'W' to go west, 'T' to talk to a character, 'L' to look for items, and 'I' to check your stats.") 
    print("Anyways, have fun! Your game will start shortly.")
    time.sleep(10)
    startingRoom(stats)

#----------------------------------------------------------------------------------
# This function handles all of the player's input. It sets a select few letters as
# the "valid input" and does not allow the user to input anything else. It also lets
# the user quit the game and show player stats. This function's role is to essentially
# check the input of any errors before returning the input back into the function
# where it was called. The stats parameter is used to include the data structure.
#----------------------------------------------------------------------------------
def playerInput(stats):
    valid_input = ['s', 'n', 'e', 'w', 't', 'l', 'p', 'z', 'i']
    user_input = input('Enter a letter: ').lower()
    if user_input == 'quit':
        quit()
    if user_input == 'i':
        showPlayerStats(stats)
        user_input = input('Enter a letter: ')
    for index in range(0,len(valid_input)): #if the user does not input the "valid input",
        if user_input == valid_input[index]:#the for loop helps to check for that and
            return user_input               #prints an error statement/asks user to 
    print("Sorry! That's not a valid input. Please try again!") #re-enter the input
    return user_input                       #if it isn't "valid"

#----------------------------------------------------------------------------------
# This function prints the player's statistics when they enter "i" as input. The stats
# parameter is used to include the data structure.
#----------------------------------------------------------------------------------
def showPlayerStats(stats):
    print('You currently have $' + str(stats['money']) + ', ' + str(stats['lives']) + ' lives and ' + str(stats['visits']) + ' room visits.')
    itemCount(stats)
    
#----------------------------------------------------------------------------------
# This function is used whenever the player enters a room. It prints out instructions
# for that room and adds a visit to the room visit counter in the roomVisits function.
# The charName parameter changes for each room depending on the name of the character
# in that room. The roomEnter parameter checks to see if the player is actually
# re-entering the room or just returning from a dialogue with a character (so the
# roomVisits function doesn't run twice).The stats parameter is used to include
# the data structure.
#----------------------------------------------------------------------------------
def enterRoom(charName, roomEnter, stats):
    randomMoney(stats)
    if charName == 'none': #if there is no character in that room, it doesn't prompt
                           #the user to enter "t
        print("Enter 'I' to view your stats.")
        print("Enter 'L' to look for items here.")
    else:
        print("Enter 'I' to view your stats.")
        print("Enter 'T' to talk to " + charName + ".")
        print("Enter 'L' to look for items here.")
    if roomEnter == True:
        stats = roomVisits(stats)

#----------------------------------------------------------------------------------
# This function adds a visit to the number of room visits. It then adds that new
# number back into the stats dictionary. The stats parameter is used to include the
# data structure.
#----------------------------------------------------------------------------------
def roomVisits(stats):
    stats['visits'] = stats['visits'] + 1
    return stats

#----------------------------------------------------------------------------------
# This function adds a set amount of money (depending on the roomAmount parameter)
# to the money count in the stats dictionary. The stats parameter is used to include
# the data structure.
#----------------------------------------------------------------------------------
def money(roomAmount, stats): 
    stats['money'] = stats['money'] + int(roomAmount)
    return stats

#----------------------------------------------------------------------------------
# This function is called when the user enters "L" and looks for items in a room.
# It allows the user to pick up an item depending on what the item is (which
# depends on what room the player is in). It then adds that item to the items list
# in the stats dictionary. The stats parameter is used to include the data structure. 
#----------------------------------------------------------------------------------
def itemPickup(roomItem, stats):
    print("You found a " + roomItem + "!")
    print("Enter 'P' to pick it up.")
    user_input = playerInput(stats)
    if user_input == 'p':
        if roomItem == 'red earring':
            addItems(stats, 'red earring')
        if roomItem == 'blue earring':
            addItems(stats, 'blue earring')
        if roomItem == 'purple earring':
            addItems(stats, 'purple earring')
        if roomItem == 'teddy bear':
            addItems(stats, 'teddy bear')
        if roomItem == 'hairbrush':
            addItems(stats, 'hairbrush')
        if roomItem == 'cookie':
            addItems(stats, 'cookie')
        print("You have successfully picked up a " + roomItem + "!")
        return stats    

#----------------------------------------------------------------------------------
# This function adds an item to the items list in the stats dictionary depending on
# what that item is (roomItem parameter). The stats parameter is used to include
# the data structure. 
#----------------------------------------------------------------------------------
def addItems(stats, roomItem):
    if roomItem == 'red earring':
        stats['items'].append('red earring') #append is used to add the string to a list.
    if roomItem == 'blue earring':
        stats['items'].append('blue earring')
    if roomItem == 'purple earring':
        stats['items'].append('purple earring')
    if roomItem == 'teddy bear':
        stats['items'].append('teddy bear')
    if roomItem == 'hairbrush':
        stats['items'].append('hairbrush')
    if roomItem == 'cookie':
        stats['items'].append('cookie')
    return stats

#----------------------------------------------------------------------------------
# This function removes an item from the items list in the stats dictionary depending
# on what that item is (roomItem parameter). The stats parameter is used to include the
# data structure.
#----------------------------------------------------------------------------------
def removeItems(stats, roomItem):
    if roomItem == 'red earring':
        stats['items'].remove('red earring') #remove is used to remove the string from
    if roomItem == 'blue earring':           #the list.
        stats['items'].remove('blue earring')
    if roomItem == 'teddy bear':
        stats['items'].remove('teddy bear')
    if roomItem == 'hairbrush':
        stats['items'].remove('hairbrush')
    if roomItem == 'cookie':
        stats['items'].remove('cookie')
    return stats

#----------------------------------------------------------------------------------
# This function counts how many of an item is in the items list in the stats dictionary.
# It then tells the player how many of what items they have. The stats parameter is
# used to include the data structure.
#----------------------------------------------------------------------------------
def itemCount(stats): 
    redEarring = 0
    blueEarring = 0
    purpleEarring = 0
    teddyBear = 0
    hairbrush = 0
    cookie = 0
    for item in stats['items']:  #checks to see if there is an item in the list 
        if item == 'red earring':#and then counts it to form an integer value.
            redEarring = redEarring + 1
        if item == 'blue earring':
            blueEarring = blueEarring + 1
        if item == 'purple earring':
            purpleEarring = purpleEarring + 1
        if item == 'teddy bear':
            teddyBear = teddyBear + 1
        if item == 'hairbrush':
            hairbrush = hairbrush + 1
        if item == 'cookie':
            cookie = cookie + 1
    if redEarring > 0:
        print('You have ' + str(redEarring) + ' red earring(s).')
    if blueEarring > 0:
        print('You have ' + str(blueEarring) + ' blue earring(s).')
    if purpleEarring > 0:
        print('You have ' + str(purpleEarring) + ' purple earring(s).')
    if teddyBear > 0:
        print('You have ' + str(teddyBear) + ' teddy bear(s).')
    if hairbrush > 0:
        print('You have ' + str(hairbrush) + ' hairbrush(es).')
    if cookie > 0:
        print('You have ' + str(cookie) + ' cookie(s)')

#----------------------------------------------------------------------------------
# This function randomly makes the player lose money upon entering a room (it is
# called in the enterroom function. The stats parameter is used to include the
# data structure.
#----------------------------------------------------------------------------------
def randomMoney(stats):
    randomMoney = random.randint(1,10)
    if randomMoney == 1:
        roomAmount = random.randint(1,5)
        print("You weren't paying attention and dropped $" + str(roomAmount) + ".")
        money(-roomAmount, stats)

#----------------------------------------------------------------------------------
# This function randomly makes the player lose a life and decreases the value of 
# lives in the stats dictionary. The stats parameter is used to include the
# data structure.
#----------------------------------------------------------------------------------
def lives(stats):
    randomLifeLoss = random.randint(1,18)
    if randomLifeLoss == 1:
        stats['lives'] = stats['lives'] - 1
        print("Idk what happened... but you lost a life. :) ")
    if stats['lives'] == 0:
        print("You have died completely. I must now reset the game for you.")
        start()
    else:
        return stats
    
#----------------------------------------------------------------------------------
# This room starts the game's storyline. It prints out narrative and then gives
# the user instructions on what possible moves they can make. It then calls the foyer
# function to continue the story.The stats parameter is used to include the data structure.
#----------------------------------------------------------------------------------
def startingRoom(stats):
    readNote = False
    goSouth = False #the goSouth and readNote variable helps to make sure the player
                    #goes south and reads the noteso that they can continue the game
    print("You awaken alone in what looks like a bedroom for someone obsessed with the"
          " colour purple.'Not again!', you think to yourself. Things like this always"
          " seem to happen to you. You look around and notice a little note. Enter 'Z'" 
          " to pick up and read the note.")
    while readNote == False:
        user_input = playerInput(stats)
        if user_input != 'z':
            print("Look...this game isn't going to go anywhere if you don't read the note! "
                  "So you better READ IT!!! Enter 'Z'")
        if user_input == 'z':
            print("The note reads: 'Go opposite from the way of Kim and Kanye's first child.'")
            readNote = True
    time.sleep(3)
    print("Enter 'S' to go south.")
    print("Enter 'E' to go east.")
    print("Enter 'W' to go west.")
    while goSouth == False:
        user_input = playerInput(stats)
        if user_input == 'e':
            print("This door is locked! Try going elsewhere.")
        if user_input == 'w':
            print("This door is locked! Try going elsewhere.")
        if user_input == 's':
            print("The door opens...")
            time.sleep(3)
            goSouth = True
    foyer(stats)

#----------------------------------------------------------------------------------
# This function involves some dialogue with a character that explains the goal of the
# game to the player. It then redirects the user to another room. Stats parameter is used
# to include the data structure.
#----------------------------------------------------------------------------------
def foyer(stats):
    talkCat = False #this variable is used in the while look to
                    #makes sure the player talks to the cat in
                    #order to advance the game.
    print("You enter into a grand looking foyer. It looks like something straight out "
          "of a movie. Farther down, you see a door. It's pretty big and well decorated"
          "so you assume that it is your way out of this mysterious place (aka the front "
          "door). You approach the door and try to open it. It's locked. 'Of COURSE its "
          "locked! Couldn't these kinds of games for ONCE be easy for me?!', you exclaim "
          "in frustration. You try opening it again...")
    time.sleep(15)
    print("Random voice: 'If you want to leave, you're gonna have to do something for me "
          "first...'")
    time.sleep(2)
    print("A tiny little cat appears out of what seems like nowhere. Enter 'T' to reply.")
    while talkCat == False:
        user_input = playerInput(stats)
        if user_input != 't':
            print("(Psst...you HAVE to reply to the cat. You know... unless you want to "
                  "stay here forever!)")
        if user_input == 't':
            talkCat = True
    print("You: 'Okay...weird little talking cat... What can I do?'")
    time.sleep(2)
    print("By this point, you're so used to weird stuff like this happening to you, you "
          "don't question it at all.")
    time.sleep(4)
    print("Moochikins: 'Well BASICALLY, I need $100 so I can buy this really dope catnip toy.'")
    time.sleep(4)
    print("You: 'I don't have $100........'")
    time.sleep(4)
    print("Moochikins: 'Yeah... thats exactly why you're going to work for it! lol you "
          "wish it was that easy!'")
    time.sleep(4)
    print("You: 'Ok... but I don't even know where I am and apparently I can't leave "
          "this building so how do you expect me to work for it?'")
    time.sleep(4)
    print("Moochikins: 'OMG literally chill for a sec! I'll explain it to you. It's "
          "very simple.'")
    time.sleep(4)
    print("You: '...'")
    time.sleep(4)
    print("Moochikins: 'Okay so there's a total of 6 rooms in this house, including "
          "this foyer area. One of my siblings are in each room except the room you woke "
          "up in and this one. If you press 'T', you can talk to them and they will have "
          "a task for you. Usually, it involves finding them an item and bringing it back"
          "to them. In exchange for the item, they will give you some money. When you have"
          "$100, come back here and give it to me and I will let you out. See? Simple!'")
    time.sleep(10)
    print("You: 'Ahhh okay... See you later then!'")
    time.sleep(2)
    print("The cat waves at you with its little paw. And you turn around to figure out "
          "which way to go next.")
    time.sleep(3)
    print("Enter 'N' to go north (back to the room you came from).")
    print("Enter 'E' to go east.")
    print("Enter 'W' to go west.")
    user_input = playerInput(stats)
    if user_input == 'n': #redirects user to next room depending on direction
        roomOne(stats)
    if user_input == 'e':
        roomFive(stats)
    if user_input == 'w':
        roomThree(stats)
        
#----------------------------------------------------------------------------------
# This function allows the player to enter inputs that redirect to different functions
# and different outcomes. The stats function is used to include the data structure. 
#----------------------------------------------------------------------------------
def roomOne(stats):
    print("You enter back into the bedroom that you started in.")
    enterRoom('none', True, stats)
    user_input = playerInput(stats)
    if user_input == 'l':
        stats = itemPickup('red earring', stats)
    print("Enter 'S' to go south.")
    print("Enter 'E' to go east.")
    print("Enter 'W' to go west.")
    user_input = playerInput(stats)
    if user_input == 'l':
        stats = itemPickup('red earring', stats)
        user_input = playerInput(stats)
    if user_input == 's':
        roomSix(stats) 
    if user_input == 'e':
        roomFour(stats)
    if user_input == 'w':
        roomTwo(stats)    
        
#----------------------------------------------------------------------------------
# This function allows the player to enter inputs that redirect to different functions
# and different outcomes. The stats function is used to include the data structure. 
#----------------------------------------------------------------------------------
def roomTwo(stats):
    print("You enter into an office space.")
    enterRoom('Cece', True, stats)
    user_input = playerInput(stats)
    if user_input == 'l':
        stats = itemPickup('blue earring', stats)
    if user_input == 't':
        charTalk('two', stats)
    enterRoom('Cece', False, stats)
    print("Enter 'E' to go east.")
    print("Enter 'S' to go south.")
    user_input = playerInput(stats)
    if user_input == 'l':
        stats = itemPickup('blue earring', stats)
    if user_input == 't':
        charTalk('two', stats)
    if user_input == 'e':
        roomOne(stats)
    if user_input == 's':
        roomThree(stats)

#----------------------------------------------------------------------------------
# This function allows the player to enter inputs that redirect to different functions
# and different outcomes. The stats function is used to include the data structure. 
#----------------------------------------------------------------------------------
def roomThree(stats):
    print("You enter into a living room. Very well decorated. You know... for cats.")
    enterRoom('Mimi', True, stats)
    user_input = playerInput(stats)
    if user_input == 'l':
        stats = itemPickup('teddy bear', stats)
    if user_input == 't':
        charTalk('three', stats)
    enterRoom('Mimi', False, stats)
    print("Enter 'N' to go north.")
    print("Enter 'E' to go east.")
    user_input = playerInput(stats)
    if user_input == 'l':
        stats = itemPickup('teddy bear', stats)
    if user_input == 't':
        charTalk('three', stats)
    if user_input == 'n':
        leaveRoom = True
        roomTwo(stats)
    if user_input == 'e':
        leaveRoom = True
        roomSix(stats)

#----------------------------------------------------------------------------------
# This function allows the player to enter inputs that redirect to different functions
# and different outcomes. The stats function is used to include the data structure. 
#----------------------------------------------------------------------------------
def roomFour(stats):
    print("You enter into a bathroom")
    enterRoom('Lulu', True, stats)
    user_input = playerInput(stats)
    if user_input == 'l':
        stats = itemPickup('hairbrush', stats)
    if user_input == 't':
        charTalk('four', stats)
    enterRoom('Lulu', False, stats)
    print("Enter 'S' to go south.")
    print("Enter 'W' to go west.")
    user_input = playerInput(stats)
    if user_input == 'l':
        stats = itemPickup('hairbrush', stats)
    if user_input == 't':
        charTalk('four', stats)
    if user_input == 's':
        roomFive(stats)
    if user_input == 'w':
        roomOne(stats)

#----------------------------------------------------------------------------------
# This function allows the player to enter inputs that redirect to different functions
# and different outcomes. The stats function is used to include the data structure. 
#----------------------------------------------------------------------------------
def roomFive(stats):
    print("You enter into a kitchen. Smells delicious...")
    enterRoom('Nini', True, stats)
    user_input = playerInput(stats)
    if user_input == 'l':
        stats = itemPickup('cookie', stats)
    if user_input == 't':
        charTalk('five', stats)
    enterRoom('Nini', False, stats)
    print("Enter 'N' to go north.")
    print("Enter 'W' to go west.")
    user_input = playerInput(stats)
    if user_input == 'l':
        stats = itemPickup('cookie', stats)
    if user_input == 't':
        charTalk('five', stats)
    if user_input == 'n':
        roomFour(stats)
    if user_input == 'w':
        roomSix(stats)
    
#----------------------------------------------------------------------------------
# This function allows the player to enter inputs that redirect to different functions
# and different outcomes. The stats function is used to include the data structure. 
#----------------------------------------------------------------------------------
def roomSix(stats):
    print("You enter back into the foyer.")
    enterRoom('Moochikins', True, stats)
    user_input = playerInput(stats)
    if user_input == 't':
        charTalk('six', stats)
    enterRoom('Moochikins', False, stats)
    print("Enter 'N' to go north.")
    print("Enter 'W' to go west.")
    print("Enter 'E' to go east.")
    user_input = playerInput(stats)
    if user_input == 't':
        charTalk('six', stats)
    if user_input == 'n':
        roomOne(stats)
    if user_input == 'w':
        roomThree(stats)
    if user_input == 'e':
        roomFive(stats)

#----------------------------------------------------------------------------------
# This function includes all of the character dialogue after the intro scenes. The room
# parameter helps to determine what character is placed in which room and therefore
# prints the correct dialogue. The stats function is used to include the data structure.
# The dialogue that is printed depends on whether the player holds specific items. If they
# don't, then the character prompts them to obtain it. If they do, then the character in
# return gives the player money (that is added to the stats dictionary using the money
# function. After the dialogue is completed, the player is redirected back to the room
# they are currently in.
#----------------------------------------------------------------------------------
def charTalk(room, stats):
    if room == 'two':
        if 'hairbrush' in stats['items']:
            print("Cece: 'Thank you for finding my hairbrush! Here's your $20.'")
            removeItems(stats, 'hairbrush')
            money(20, stats)
        else:
            print("You: 'Hey Cece!'")
            print("Cece: 'Oh finally!! I can't pawwwwsibely get any work done "
                  "with my hair looking like this! Would you be a dear and bring"
                  "me my [hairbrush]? I'll give you $20.'")
            print("You: 'Yup! Be back soon!'")
        roomTwo(stats)
    if room == 'three':
        if 'cookie' in stats['items']:
            print("Mimi: 'Thank you for bringing me my cookie! Here's your $40.'")
            removeItems(stats, 'cookie')
            money(40, stats)
        else:
            print("You: 'Hey Mimi!'")
            print("Mimi: 'Hey! Can you help me?'")
            print("You: 'Yup! That's what I'm here for! What do you need?'")
            print("Mimi: 'So I've just been sitting here watching YouTube videos."
                  "Like, at first I was watching hilarious human videos right? "
                  "But then, I clicked onto a cooking video and now I'm starving! "
                  "Can you bring me a [cookie] please? I'll give you $40 in return.")
            print("You: 'Yes of course! I'll go bring you some right away.'")
        roomThree(stats)
    if room == 'four':
        if ('red earring' and 'blue earring') in stats['items']:
            print("Lulu: 'Thank you for finding my earrings! Here's your $50.'")
            removeItems(stats, 'red earring')
            removeItems(stats, 'blue earring')
            money(50, stats)
        else:
            print("You: 'Hey Lulu!'")
            print("Lulu: 'Finally! Some help! I have two hours to get to my friend's"
                  "party but I can't find my earrings anywhere! If I give you $50, "
                  "would you please help me look? I need one [blue earring] and one"
                  "[red earring].")
            print("You: 'I'll try!'")
        roomFour(stats)
    if room == 'five':
        if 'teddy bear' in stats['items']:
            print("Nini: 'Thank you for bringing me my teddy bear! Here's your $20.'")
            removeItems(stats, 'teddy bear')
            money(20, stats)
        else:
            print("You: 'Hey Nini!'")
            print("She seems very busy making dinner and doesn't even look over.")
            print("Nini: Shhh! I have no time! Can you please just bring me my [teddy "
                  "bear]? Mr. Cuddles always loves watching me cook. I think I left him"
                  "in the living room. You'll get $20!")
            print("You: Sure. Be back in a bit!")
        roomFive(stats)
    if room == 'six':
        if stats['money'] > 99:
            print("Moochikins: 'Nice! You brought back $100! You can leave now. Bye!'")
            print("Moochikins opens the front door, signaling your freedom.")
            money(-100, stats)
            win()
        else:
            print("You: 'Hey Moochikins!'")
            print("Moochikins: 'Do you have the $100 for me?'")
            print("You: Nope...not yet!")
            print("Nini: Well hurry!!!!!!!")
            print("You: I'm working on it!")
        roomSix(stats)

#----------------------------------------------------------------------------------
# This function prints the winning dialogue once the player completes the game.
# It then exits the program.
#----------------------------------------------------------------------------------
def win():
    print("Congratulations! You won the game!!!!!!!!!!!")
    print("You win absolutely nothing!!!! :)")
    print("Hope you had fun!")
    print("Goodbye!")
    quit()
    
welcome()
