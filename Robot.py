
print("Robo_Pocalypse")

print("")

print("     By       ")

print("")

print("Jacob Lorenzo")

print("")

print("To play, you will be given 2 options per choice, to pick one, you press 0 for the first one, and 1 for the second one.")

print("In a world where an AI has taken over, you are one of the last humans left on"+
"this desolate world with nothing but robots patrolling the streets."+
"Your goal is to take down the AI and save what is remaining of humanity.")

print("")

fName = input("What is your first name?")

print("")

lName = input("What is your last name?")

print("")

print("Hello" + " "+ fName + " " + lName)

print("")

turnCounter = 0

gameChoice = []

storyInit = ["While you are sleeping, you wake up hearing a knocking at the door, it might be humans, but it could also be the robots."+" "+
"Then you hear them say"+" " +fName+" "+lName+" "+"are you there?"+" You have a crowbar, but if it is a human, you might injure them, but if its a robot, they will most likely kill you before you damage their machinery."]

Choices1 = ["Escape / Fight"]
Story0 = ["You escape through the window of your house, but you soon realize that either way, the robots would have captured you. Surrounding your house were twenty Assaultron units. You are then grabbed by an Assaultron unit and dragged across the floor."]
Story1 = ["You open the door with a crowbar in your hand and are greeted by an Assaultron arm locked around your wrist, you are being dragged along the floor as they take you to some unknown location."]

Choices2 = [ "Play Dead/Negotiate" ]

Story00 = ["You attempt to play dead, but one of the units is kicking you as you go along to keep you awake while one attached a feeding tube and oxygen tube to your face. You are brought into a testing room with a set of scary tools on the table beside you. You are restrained on a table and they say the surgeon will be here shortly."]
Story11 = ["You try to talk to them but you are then shocked by one of the unit's prods and tells you to be quiet. You are eventually brought to a prison they made out of fabricated materials in their factories, without tools, you have no chance of escape. Coincidentally this is the same prison that the AI lives."]

print(storyInit)
print("")
print(Choices1)
print("")

choiceGen = input("What would you like to do?")

if choiceGen == "0":

    gameChoice.append(0)

elif choiceGen == "1":

        gameChoice.append(1)
            
else:
            print("Unrecognized selection, Game Over")
            quit()

while (turnCounter < 2):

    turnCounter =  turnCounter +1

    if choiceGen == "0" and gameChoice == [0]:#Escape

        gameChoice.append(0)

        print(gameChoice)

        print("")

        print(Story0)

        print("")

        print(Choices2)

        print("")

        choiceGen = input("What would you like to do?")

        print("")

    elif choiceGen == "1" and gameChoice == [1]:#Fight

        gameChoice.append(1)

        print(gameChoice)
        
        print(Story1)

        print("")

        print(Choices2)

        print

        choiceGen = input("What would you like to do?")

        print("")

    elif choiceGen == "0" and gameChoice == [1,1] or gameChoice == [1,0]:

        gameChoice.append(0)

        print(Story00)

        print("")

    elif choiceGen == "1" and gameChoice == [0,0] or gameChoice == [0,1]:

        gameChoice.append(1)

        print(Story11)

        print("")


#storyA = Story("you go to the mall")
#storyB = Story("everything is awful")

#storyA.addChoice(Choice("go to hot topic", storyB), Choice("Kill time", storyA))



#while(True):
   # currentStory.printText()
   # choice = input("?")
   # newStory = currentStory.pickChoice(choice)
   # currentStory = newStory
