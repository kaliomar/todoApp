import json
import add_and_show
from json.decoder import JSONDecodeError
from checking_user import get_user_data

usr_name,key_name,name = get_user_data()
file_name = f"{name}'s_todos.json"

def re_file(): # to read todos from file
    with open(file_name,"r") as ref:
        try:
            json_dict = json.load(ref)
            return json_dict
        except JSONDecodeError:
            json_dict = {}
            return json_dict

def wr_file(): # to save todos to file
    todos = re_file()
    date = input("date: ")
    mission = input("mission: ")

    if date not in todos.keys(): # key isn't in file 
        todos[date] = mission
    
    elif type(todos[date]) == list: # there are many todos on this date
        li = []
        for i in todos[date]:
            li.append(i)
        li.append(mission)
        todos[date] = li
        
    else: # there is one mission on this date
        li = [todos[date],mission]
        todos[date] = li

    with open(file_name,mode="w") as wrf:
        json.dump(todos, wrf)
    wrf.close()

