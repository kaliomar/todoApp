import checking_user
from add_and_show import add_todo, show_missions


def choosing(): # to ask if user want to add or check date and mission
    print("          **** type (a) for adding new mission or (s) to show missions on specific date **** ")
    choice = input("Type your selection: ")
    if choice == 'a': # if user choose to add
        times_to_do = int(input("How many times do you need to try: "))
        for i in range(times_to_do):
            add_todo()
    elif choice == 's': # if user choose to check
        times_to_do = int(input("How many times do you need to try: "))
        for i in range(times_to_do):
            show_missions()
    else: # if user is a stupid asshole 
        print("not allowed choice")



choosing()