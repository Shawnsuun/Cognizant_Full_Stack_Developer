import time
import random
import string


def typewriter_simulator(message):
    for char in message:
        print(char, end='')
        if char in string.punctuation:
            time.sleep(0.2)
        time.sleep(0.01)
    print('')


def print_pause(message, delay=1):
    typewriter_simulator(message)
    time.sleep(delay)


def intro():
    print_pause("You find yourself standing in an open field, filled with"
                " grass and yellow wildflowers.")
    print_pause("Rumor has it that a wicked fairie is somewhere around here,"
                "and has been terrifying the nearby village.")
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause("In your hand you hold your trusty (but not very effective)"
                " dagger.")


def field(weapons):
    # Things that happen when the player runs back to the field
    print_pause("Enter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave.")
    print_pause("What would you like to do?")
    valid_input = True
    while valid_input:
        choice = input("(Please enter 1 or 2.)")
        if choice == "1":
            house(weapons)
            valid_input = False
        elif choice == "2":
            cave(weapons)
            valid_input = False


def cave(weapons):
    # Things that happen to the player goes in the cave
    if "long_claw" in weapons:
        print_pause("There is nothing to to explore...")
    else:
        print_pause("You peer into the cave.")
        print_pause("It seems dark and narrow.")
        print_pause("Suddenly you see a bling inside the cave.")
        print_pause("You feel a little scared.")
        print_pause("What could be inside?")
        print_pause("Enter 1 to explore deeper inside.")
        print_pause("Enter 2 to run away.")
        valid_input = True
        while valid_input:
            choice = input("(Please enter 1 or 2.)")
            if choice == "1":
                print_pause("You find the weapon long claw!")
                weapons.append("long_claw")
                valid_input = False
            elif choice == "2":
                valid_input = False
        print_pause("You walk back out to the field.")
    field(weapons)


def house(weapons):
    # Things that happen to the player in the house
    print_pause("The house looks weird, seems it is abandoned.")
    print_pause("You knock the door and no one answered.")
    print_pause("You push the door and it is opened")
    print_pause("You walk inside and suddenly the wicked fairie"
                " attacked you from the behind!")
    print_pause("Enter 1 to fight.")
    print_pause("Enter 2 to run away.")

    valid_input = True
    while valid_input:
        choice = input("fight or escape?")
        if choice == "1":
            print_pause("You run into the corner of the house.")
            print_pause("The wicked fairie waves her wand and ready"
                        " to give you the last attack!.")
            if 'long_claw' in weapons:
                print_pause("You guard yourself with your sword.")
                print_pause("The attack of enemy has been parryed"
                            " by the sword!")
                print_pause("It is time for you to counter attack!")
                print_pause("You use your sword to hit the wicked fairie")
                print_pause("The wicked fairie have been defeated!")
                print_pause("You won the game!", 5)
            else:
                print_pause("But you only have a little dagger")
                print_pause("You decide to throw the dagger to the"
                            " enemy desperately!")
                hit = random.randint(0, 5)
                if hit == 0:
                    print_pause("The dagger hits right into the wicked"
                                " fairie's face!")
                    print_pause("The wicked fairie have been defeated!")
                    print_pause("You won the game!")
                else:
                    print_pause("You miss the target!")
                    print_pause("Your have been defeated!")
                    print_pause("Game over!", 5)
            valid_input = False
        elif choice == "2":
            print_pause("You fail to escape, and be captured by the"
                        " wicked fairie.")
            print_pause("Game over!", 5)
            valid_input = False
    end()


def end():
    valid_input = True
    while valid_input:
        choice = input("Play again? (y/n)")
        if choice == "y":
            print_pause("\nGame restart.\n")
            play()
        elif choice == "n":
            print("\nQuit game.\n")
            exit(0)


def play():
    weapons = ['dagger']
    intro()
    field(weapons)


play()
