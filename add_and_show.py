import json
def add_todo(): # this function for adding mission to json file
    from read_and_write import wr_file
    wr_file()


def show_missions(): # to print out mission of specific date
    date = input("select date: ")
    from read_and_write import re_file
    current_missions = re_file()

    if date not in current_missions.keys(): # user date isn't in our dict
        print("not existance")
    
    else: # user date is in our list
        if type(current_missions[date]) == list: # but date has many mission on it
            for i in current_missions[date]:
                print(i)
        else: # date has one mission on it 
            print(current_missions[date])

