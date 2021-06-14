import sys
import time

a = 3.2
b = 0.2
c = 0.08
d = 4
e = 5

def intro() :
    print()
    print('"When you do something beautiful and nobody notices, do not be sad."')
    time.sleep(e)
    print('"For the sun every morning is a beautiful spectacle and yet most of the audience still sleeps."')
    time.sleep(e)
    print('-John Lennon')
    time.sleep(e)
    print()
    print('>>Harvey<< ( ͡❛ ͜ʖ ͡❛): "Rise and shine buttercup"')
    time.sleep(a)
    print('"My name is Harvey. Im that little voice in your head that tells you to wake up in the morning when your alarm goes off"')
    print()
    time.sleep(d)
    print('.....BEEP BEEP BEEP!!!')
    time.sleep(a)
    print()
    time.sleep(a)
    print('>>Harvey<<: ( ͡❛ ͜ʖ ͡❛) "Oh would you look at that"')
    time.sleep(a)

    print('"There goes your alarm now!"')
    time.sleep(a)

    print('"Now I know what you are thinking"')
    time.sleep(a)

    print('"You want to hit the snooze button for 5 more minutes of sleep heaven "')
    time.sleep(a)

    print('"But, we know you will make the right decision"')
    time.sleep(a)

    print('"So what will it be?"')
    time.sleep(a)

    print()

    startGame = input("Do you want to hit the snooze button? Y/N?:  ")
    if startGame == 'y' or startGame == 'Y' or startGame == 'Yep':
        print(
            "Not all of us can seize the day I suppose. You hit the snooze button and miss your meeting. You are Fired")
        print("Your boss is angry and fires you. ")
        print("GAME OVER, YOUR MORNING SIMULATION HAS COME TO AN END")
    elif startGame == 'n' or startGame == 'N' or 'nope':
        time.sleep(d)
        print("Now the real fun begins...Welcome to Wake Up! The Early Morning Simulator. Lets get the day started!")
        path1()



def path1() :
    time.sleep(a)
    print("You roll out of bed and you stumble into the bathroom")
    time.sleep(a)
    print("You turn on the shower and step inside")
    time.sleep(a)
    print("You realize there is no hot water")
    print()
    time.sleep(a)
    print('>>Harvey<<:( ͡❛ ͜ʖ ͡❛) "That water seems pretty cold. Your water heater must be busted."')
    time.sleep(a)
    print('"No time to get it fixed. You have to get to work pronto! What should you do?"')
    time.sleep(a)
    print()
    pathone = input("Do you continue with the ice cold shower? y/n?")
    if pathone == 'n' or pathone == "N" or pathone == 'nope' :
        path1_2()
    elif pathone == 'y' or pathone == "Y" or pathone == 'yep' :
        path2()
    else:
        print()
        print('"Ummm, Come again?"')
        path1()


def path1_2() :
    print("You turn off the shower head. Horrible way to start the day.")
    time.sleep(a)
    print("You decide to call into work sick")
    time.sleep(a)
    print("You pick up the phone and call your boss to tell him you have covid-19 and come come into work")
    time.sleep(a)
    print("Your boss cusses you out and complains on how you cost the company a crucial sales transaction")
    time.sleep(a)
    print("You go back to lay in bed like a big bum")
    print()

    print("GAME OVER, YOUR EARLY MORNING SIMULATION HAS ENDED")
    print()
def path2() :
    print("You continue taking your ice cold shower")
    time.sleep(a)

    print("You think to yourself that this is a horrible way to start the day")
    print()
    time.sleep(a)

    print('>>Harvey<< ( ͡❛ ͜ʖ ͡❛): "Hey! Hey! Hey!!, you only got 45 minutes to get to work!"')
    time.sleep(a)

    print('"Finish up this little polar bear shower and go make some coffee"')
    time.sleep(a)

    print('"Better yet! Swing on by Cup-Uh-Joe Coffee Shop on the way to work"')
    time.sleep(a)
    print('"I hear the Super Double Mocha Expresso is to die for"')
    print()
    time.sleep(a)
    pathtwo = input("Do you go to Cup-Uh-Joe Coffee Shop or Go straight to work Joe/Work?")
    if pathtwo == 'joe' or pathtwo == "Joe" or pathtwo == 'J':
        path2_1()
    elif pathtwo == 'work' or pathtwo == "Work" or pathtwo == 'W':
        path3()
    else:
        print()
        print('"We have a long commute to work, I do not understand your answer. Joe or Work?"')
        path2()

def path2_1() :
    print()
    print("You finish up in the bathroom, get dressed, grab your breifcase, car keys and run out the door")
    time.sleep(e)

    print("You speed out of your driveway and find the nearest Cup-Uh-Joe Coffee Shop")
    time.sleep(e)

    print("When you pull into the parking lot you see the place is swamped with other early morning monsters like yourself")
    time.sleep(e)

    print("You wait and get your coffee and realize you have 15 minutes to get to work. Your only option is to drive 90 mph")
    time.sleep(e)

    print("This is 15 mph over the legal limit, but you must get to work on time")
    print()
    time.sleep(a)
    print('>>Harvey<< ( ͡❛ ͜ʖ ͡❛): "Hey its me again! Driving fast is pretty dangerous. You should think again on this one"')
    print()
    time.sleep(a)
    pathtwoone = input("Do you go 90mph or go the speed limit? 90/speed limit")
    if pathtwoone == '90' or pathtwoone == "nintey" or pathtwoone == 'fast':
        pathWIN()
    elif pathtwoone == 'speed limit' or pathtwoone == "Speed Limit" or pathtwoone == 'Speed limit':
        path4()
    else:
        print()
        print('"You have 15 minutes to get to work. Stop messing around! Make a decision Try Again"')
        path2_1()

def path3() :
    print("You finish up in the bathroom, get dressed, grab your breifcase, car keys and run out the door")
    time.sleep(a)

    print("You are so tired from not having any coffee that you run into a tree")
    time.sleep(a)

    print("Your car is totalled and your boss is mad you missed work.")
    print()
    time.sleep(a)

    print("GAME OVER, YOUR EARLY MORNING SIMULATION HAS ENDED")


#THIS SEQUENCE IS THE WINNING PATH AND TAKES YOU INTO THE OFFICE AND INTO THE MORNING MEETING SEQUENCE
def pathWIN() :
    print("You put the pedal to the metal")
    time.sleep(a)

    print("You are cruising at 90 mph and you look in the rear view mirror")
    time.sleep(d)

    print()

    print('>>Harvey<< ( ͡❛ ͜ʖ ͡❛): "Hey buddy! Its me again, I know those lights anywhere. THATS THE FUZZ!!!!"')
    time.sleep(e)
    print()

    print('You decide to floor it and get off the freeway. You take a few turns to try and lose the cops')
    time.sleep(e)

    print('You see your job and pull into the parking lot')
    print()
    time.sleep(a)
    print('>>Harvey<< ( ͡❛ ͜ʖ ͡❛) :"I think you lost them man, looks like you made it to work on time. Looks like that coffee did the trick"')
    print()
    time.sleep(e)
    print('You give yourself one last sigh of relief')
    time.sleep(e)
    print('You take your coffee, and briefcase and walk into the building')
    time.sleep(e)
    print('You see Chris, your best buddy in the company. Both of you graduated together from the University of Southern California together.')
    time.sleep(e)
    print()
    print('>>Chris<< (❛̃ ͜ʖ❛̃) "Whats up man? Jeez, you look like hell."')
    time.sleep(a)
    print('"Did you shower with iscicles or something? HAHAHA!"')
    time.sleep(e)
    print('"Anyways man, I got to print these visuals off before the morning meeting"')
    print()
    print('>>Harvey<< ( ͡❛ ͜ʖ ͡❛) : "Uh Oh! Looks like you forgot to prepare your visuals for the meeting"')
    time.sleep(e)
    print('"You just can not seem to win today can you?"')
    time.sleep(e)
    print('"Chris is right. Did you shower with iscicles this morning?"')
    time.sleep(e)
    print('"Haha! That is a joke. Lighten up! You can take the visuals from last week"')
    time.sleep(e)
    print('"....or you can wing it"')
    print()

    pathvisual = input("Do you use the visuals from last week or wing it?: Visuals/Wing it")
    if pathvisual == "visuals" or pathvisual == "Visuals" or pathvisual == 'visual':
        pathgoodending()
    elif pathvisual == 'wing it' or pathvisual == "Wing it" or pathvisual == 'wing it':
        pathwingit()
    else:
        print()
        print('"You have a meeting to get to!. Try again!"')
        pathWIN()

    time.sleep(a)


def pathgoodending() :
    print()
    print('>>Harvey<< ( ͡❛ ͜ʖ ͡❛) : "Last weeks visuals huh? Hopefully the boss will not notice"')
    time.sleep(a)
    print()
    print("You run to your office and grab last weeks visuals")
    time.sleep(a)

    print("You run into the conference room and grab a seat next to Chris")
    time.sleep(d)

    print("Chris peeks at your paper and chuckles")
    time.sleep(d)

    print('>>Chris<< (❛̃ ͜ʖ❛̃)' "Are those last weeks visuals? HaHa! ")
    time.sleep(d)

    print("You look at Chris and tell him you will be fine")
    time.sleep(d)

    print("The meeting starts and everyone briefs the boss on their latest visuals")
    time.sleep(d)

    print('When it is your turn, you look down at your paper and begin to speak')
    time.sleep(d)

    print('You rattle off last weeks numbers and reports')
    time.sleep(d)

    print('Your boss is amazed at your "work" and promotes you to a major project')
    time.sleep(d)

    print('Even Chris is amazed at your Emmy-award winning performance')
    time.sleep(d)

    print('Chris gives you a nod and raises a peace sign at you')
    time.sleep(d)

    print("The good ol' USC hand gesture...fight on Trojans, fight on")
    time.sleep(d)

    print()
    print("CONGRATULATIONS: YOUR EARLY MORNING SIMULATION WAS A SUCCESS")
    time.sleep(d)

    print("UPCOMING RELEASES: NIGHT LIFE SIMULATOR")

def pathwingit():
    print()
    print("You throw your empty coffee cup into the trash")
    time.sleep(d)

    print("You run into the conference room and grab a seat next to Chris")
    time.sleep(d)

    print("Chris peeks at you and chuckles")
    time.sleep(d)

    print('>>Chris<< (❛̃ ͜ʖ❛̃)' "Where are your visuals? Holy smokes! Are you gonna wing it? ")
    time.sleep(d)

    print("You look at Chris and tell him you will be fine")
    time.sleep(d)

    print("The meeting starts and everyone briefs the boss on their latest visuals")
    time.sleep(d)

    print('When it is your turn, you look at a blank peice of paper and start speaking')
    time.sleep(d)

    print('You rattle off bogus numbers and reports')
    time.sleep(d)

    print('Your boss looks confused, as well as everyone in the room')
    time.sleep(d)

    print('Except for Chris who is trying his hardest not to laugh')
    time.sleep(d)

    print('When you are done your boss gives an awkward smile and thanks you for your brief')
    time.sleep(d)

    print("Your boss says he had no idea Cup-Uh-Joe Coffee Shop needed Data Analyst consultations")
    time.sleep(d)

    print("Everyone busts out laughing and you crack a small smile knowing you just got through the morning")
    time.sleep(d)

    print()
    print("CONGRATULATIONS: YOUR EARLY MORNING SIMULATION WAS A SUCCESS")
    time.sleep(a)

    print("UPCOMING RELEASES: NIGHT LIFE SIMULATOR")

#HARVEY NEEDS TO SPEAK HERE AND GIVE PLAYER A CHOICE  ABOUT THE MEETING


def path4() :
    print("You go the speed limit. You pull into work 10 minutes late")
    time.sleep(a)

    print("You walk into the office and your boss gives you a mean glance")
    print()
    time.sleep(a)

    print('Boss:"IN MY OFFICE NOW!!!!!"')
    time.sleep(a)

    print('You hang your head in sorrow as you walk into your bosses office to face the music')
    print()


    print("GAME OVER, YOUR EARLY MORNING SIMULATION HAS ENDED")


#THIS IS THE INTRO
print("")
print("|--------------------------------------|")
print("|                  /\                  |")
print("|                WAKE UP!              |")
print("|      THE EARLY MORNING SIMULATOR     |")
print("|                  \/                  |")
print("|--------------------------------------|")

time.sleep(a)
print("A Code Culture Program")
time.sleep(a)

playerStart = input("Are you ready to start the day? Y/N?:")
if playerStart == 'n' or playerStart == 'N' or playerStart == 'Nope':
    print("Not all of us can seize the day. You stay in bed and miss work. Your boss fires you")
    print("GAME OVER, YOUR EARLY MORNING SIMULATION HAS ENDED")
elif playerStart == 'y' or playerStart == 'Y' or playerStart == 'Yep' :

    intro()

