import time
import random
import enum


#  replace while statements
def valid_input(prompt, option1, option2, option3):
    while True:
        response = input(prompt)
        if option1 in response:
            break
        elif option2 in response:
            break
        else:
            print_pause("Sorry, I don't understand.")
    return response


class Color(enum.Enum):
    red = '\033[91m'
    purple = '\033[95m'
    blue = '\033[94m'
    cyan = '\033[96m'
    green = '\033[92m'

    @classmethod
    def get_color(cls):
        return random.choice([color.value for color in cls])


def print_pause(message, delay=0):
    print(Color.get_color() + message)
    time.sleep(delay)


def intro():
    print_pause("The bell above the door rings as you walk into the diner.")
    print_pause("You hear a voice from behind the counter tell you to pick"
                " a table.")
    print_pause("As you sit down a menu is brought out to you.\n")


def menu_choice():
    print_pause("Today's specials includes:"
                "\n1. Biscuits and Gravy\n2. Pancakes")
    while True:
        response = valid_input("Which would you like? Type: 1 or 2\n",
                               "1", "2")
        if response == '1':
            print("That's a great choice!")
            break
        elif response == '2':
            print("The pancakes here are excellent!")
            break
        else:
            print("invalid response please try again")
#  Next in sequence


def soda():
    soda = valid_input("What would you like to drink?"
                       "\n1. 7up\n2. CocaCola\n", '1', '2')
    while True:
        if soda == '1':
            print("7up it is.\n")
            break
        elif soda == '2':
            print("Coca-Cola it is.\n")
            break
        else:
            print("invalid response please try again")
    waiting()
#  Next in sequence


def waiting():
    print_pause("Your food will be out soon.")
    waiting = valid_input("Would you like to look at your phone"
                          " while you wait or read a book?\n1. Phone\n"
                          "2. Book\n", '1', '2')
    while True:
        if waiting == '1':
            print("Your phone is out of batteries."
                  "You reach into your bag and grab your book.")
            break
        elif waiting == '2':
            print("Good choice, your phone is out of batteries anyways.")
            break
        else:
            print("invalid response please try again")
    your_soda()
#  Next in sequence


def your_soda():
    print_pause("Your waiter brings you your beverage.")
    print_pause('"Your food will be out very soon." says the waiter.')
    meal()
#  Next in sequence


def meal():
    print_pause('"Here is your meal, be careful it is hot."')
    print_pause("As you take a bite of your food you "
                "hear the waiter make an announcement...")
    print_pause('"Attention all diners! We will be having a random drawing. '
                'Winners will have the chance of a free meal!"')
    random_choice()
#  Next in sequence


def random_choice():
    print_pause('"Attention all diners. A random drawing is about to take'
                ' place. Pick a number 1 or 2 and you could win!"')
    while True:
        choice = valid_input("Pick a number 1 or 2\n", '1', '2')
        a = 1
        b = 2
        if choice == random.randint(a, b):
            print("Congratulations! You have won a free meal"
                  "and won the game!")
            break
        elif random_choice != random.randint(a, b):
            print("Sorry, you didn't win the free meal.")
            print_pause("You take out your wallet and with"
                        " dissapointment you pay your bill.")
            break
        else:
            print("invalid response please try again")
    again()
#  Next in sequence


def again():
    again = valid_input("Would you like to play again?"
                        " (Yes/No)\n", 'yes', 'no').lower()
    while True:
        if again == "yes":
            restaraunt()
            break
        if again == "no":
            print("Thank you for playing.")
            exit(0)
        else:
            print("invalid response please try again")


def restaraunt():
    intro()
    menu_choice()
    soda()
    waiting()
    your_soda()
    meal()
    random_choice()
    again()


restaraunt()

