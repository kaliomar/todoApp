import json

def add_todo(): # this function for adding mission to json file
    from rwfunc import wr_file
    wr_file()


def show_missions(): # to print out mission of specific date
    date = input("select date: ")
    from rwfunc import re_file
    current_missions = re_file()

    if date not in current_missions.keys(): # user date isn't in our dict
        print("not existance")
    
    else: # user date is in our list
        if type(current_missions[date]) == list: # but date has many mission on it
            for i in current_missions[date]:
                print(i)
        else: # date has one mission on it 
            print(current_missions[date])


def choosing(): # to ask if user want to add or check date and mission
    print("          **** type (a) for adding new mission or (s) to show missions on specific date **** ")
    add_or_show = input("Type your selection: ")
    times_to_do = int(input("How many times do you need to try: "))
    if add_or_show == 'a': # if user choose to add
        for i in range(times_to_do):
            add_todo()
    elif add_or_show == 's': # if user choose to check
        for i in range(times_to_do):
            show_missions()
    else: # if user is a stupid asshole 
        print("not allowed choice")



choosing()