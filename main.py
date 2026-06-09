import time
_original_print = print

def print(*args, **kwargs):
    _original_print(*args, **kwargs)
    time.sleep(0.75)

battery = 70
health = 100
current_room = "Lab"
game_running = True

inventory = []

rooms = {
    "Lab": {
        "north": "Control Room",
        "east": "Storage",
        "item": "Battery Pack"
    },

    "Storage": {
        "west": "Lab",
        "south": "Generator Room",
        "item": ""
    },

    "Control Room": {
        "south": "Lab"
    }

}

def main():
    run_game()

        
#-----------------------------------------------------------

def run_game():

    global card_ControlRoom 

    card_ControlRoom = False

    print("BOOTING SYSTEM...")
    time.sleep(1)

    print("...")
    time.sleep(1)

    print("...")
    time.sleep(1)

    print("SYSTEM ONLINE")
    time.sleep(1)

    print("")
    print("WARNING:")
    time.sleep(0.5)

    print("Primary reactor unstable.")
    time.sleep(1)

    print("Emergency power active.")
    time.sleep(1)

    print("")
    print("R-7 (YOU) are activated.")
    time.sleep(1)

    show_status()

    print("")
    print("Objective:")
    time.sleep(0.5)

    print("Restore critical systems.")

    movement()


# Player Information
def show_status():
    global battery
    global health
    global current_room

    print("Player Status:")
    print("Battery: ", str(battery) + "%")
    print("Health: ", str(health) + "%")
    print("Current room:", current_room)

def show_room():
    global current_room

    print("Current room:", current_room)

#-----------------------------------------------------------------

# Player actions
def pick_item():
    item = rooms[current_room]["item"]
    inventory.append(item)
    print("Now you have", item)

def use_battery_pack():
    global battery
    battery = 90
    print("your battery recharge itself")
    show_status()
        
def movement():
    global current_room

    print("")
    while current_room not in ["1", "2", "3"]:  
        for i, room in enumerate(rooms, start=1):
            print(f"{i} - {room}")
        current_room = str(input("Type the number of your next room: "))


    if current_room == "1":

        current_room = "Lab"
        print("You are at Lab")

        # main puzzle
        lab_puzzle()
        
    elif current_room == "2":

        current_room = "Storage"

        # main puzzle
        storage_puzzle()
        
    elif current_room == "3":

        current_room = "Control Room"

        # puzzle principal
        controlRoom_puzzle()
        


# Rooms logic

def lab_puzzle():

    global lab_finished
    lab_finished = False

    global battery
    battery -= 20

    global health

    pick_battery = ""

    print("[ LAB ]")
    print("Emergency lights flicker across the laboratory walls.")
    print("Broken monitors illuminate the room with a weak blue glow.")
    print("You hear the distant sound of metal creaking somewhere in the facility.")
    print("")
    print("As long as you entered the room, you lost 20% of your total battery")

    while lab_finished == False:
        if current_room == "Lab":
            print()
            while True:
                pick_battery = str(input("Wow! You found a battery pack, do you want pick and use It? (Type 'yes' or 'no') "))
                if pick_battery == "yes":
                    pick_item()
                    use_battery_pack()
                    print("")
                    print("You insert the Battery Pack into your energy compartment.")
                    print("Your internal systems stabilize.")
                    print("")
                    print("As power returns to nearby systems,")
                    print("a damaged computer terminal suddenly turns on.")
                    print("")
                    print("--- TERMINAL ONLINE ---")
                    print("")
                    print("RESEARCH LOG #04")
                    print('"Reactor instability continues to spread through Sector 3."')
                    print('"Security protocols have locked the Control Room."')
                    print('"Emergency Access Cards were moved to the Storage Room."')
                    print("")
                    print("NEW OBJECTIVE:")
                    print("Find the Access Card in the Storage Room.")
                    print("")
                    print("A nearby door emits a weak mechanical sound.")
                    print("The facility seems to be slowly waking up again.")
                    print("")
                    print("You get out of Lab Room")
                    print("")
                    print("Choose another room: ")
                    movement()
                    break
                elif pick_battery == "no":
                    print("")
                    print("You leave the Battery Pack on the floor.")
                    print("Your systems remain unstable.")
                    print("Your battery is low.")
                    print("You lost 50% of your health")
                    health -= 50
                    print("")
                    show_status()
                    print("the laboratory stays dark and silent.")
                    print("")
                    print("You get out of Lab Room")
                    print("")
                    print("Choose another room: ")
                    movement()
                    break
                else: 
                    print("Type 'yes' or 'no'")
                    print("")   
            lab_finished = True

        
def storage_puzzle():
    global health

    if current_room == "Storage":
        if battery >= 90:
            print("You are at Storage")
            print("[STORAGE]")
            print("")
            print("Many boxes are around you")
            print("One of them fall in front of you!")
            while True:
                open_box = str(input("Do you want to open the box? (if yes, type 'yes') "))

                if open_box == "yes":
                    print("WHAAAAT????")
                    print("A cat jumped out of the box and spilled the water that was nearby on you")
                    print("You've lost 40% of health")
                    health -= 40
                    show_status()
                    lever_storage_puzzle()
                    movement()
                    break
                else:
                    lever_storage_puzzle()
                    movement()
                    break
        else:
            print("You just can enter in this room if your battery is at least 90%")
            show_status()
            print("Seems like your battery is lower than 90%")
            print("Maybe would be good explore Lab Room")
            movement()

def controlRoom_puzzle():
    global card_ControlRoom
    if current_room == "Control Room":
        if card_ControlRoom == True:
            print("You are at Control Room")
            print("[Control Room]")
            print("")
            print("The room is silent.")
            print("Rows of monitors flicker in the darkness.")
            print("A large red warning message fills the main screen.")
            print("REACTOR MELTDOWN IN PROGRESS")
            final_puzzle()
        else:
            print("You need to find the Access Card to enter in Control Room, choose another room")
            movement()
            
#------------------------------------------------

def final_puzzle():
    print("AUTHORIZATION REQUIRED")
    print("")
    while True:
        name = str(input("What is the name of the robot unit? (your name): "))
        if name == "R-7" or name == "R7":
            print("Congratulations! You are R-7: the maintenance robot")
            print("")
            while True:
                sector = str(input("What sector was mentioned in Research Log #04 at Lab Room?: "))
                if sector == "Sector 3" or sector == "3":
                    print("Reactor stabilization sequence started...")
                    print("10%")
                    print("30%")
                    print("50%")
                    print("70%")
                    print("90%")
                    print("99%")
                    print("...")
                    print("100%")
                    print("")
                    print("REACTOR STABLE")
                    print("Emergency mode disabled.")
                    print("Facility power restored.")
                    print("Mission Complete.")
                    print("Thank you, Unit R-7.")
                    print("The End.")
                    return
                else:
                    print("Try again. Tip: There are just 3 sectors")
        else:
            print("Try again. Tip: You are the seventh version of the type R robots")


def lever_storage_puzzle():
    global card_ControlRoom

    words = {
        "nhtoyp": "python",
        "edco": "code",
        "lppae": "apple"
    }

    print("")
    print("The wall in front of you starts to open!!")
    print("You see a lot of letters and words.")
    print("Maybe they are scrambled words...")
    print("It is a puzzle!!")
    print("")

    for scrambled_word, correct_word in words.items():

        while True:

            print(f"Unscramble this word: {scrambled_word}")

            answer = input("Type your answer: ")

            if answer == correct_word:
                print("You are correct!!")
                print("")
                break
            else:
                print("Wrong answer. Try again.")
                print("")
                print("A little tip: Snakes does not eat fruits, but you can code it!")
                print("")
    print("All the words were discovered by you! Congratulations!")
    print("WOW! Seems like you found the card to enter in Control Room!")
    print("You got Control Room Card.")
    card_ControlRoom = True

if __name__ == "__main__":
    main()