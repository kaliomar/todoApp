import json
import add_and_show

def re_file(): # to read todos from file
    with open("vault.json","r") as ref:
        json_dict = json.load(ref)
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

    with open("vault.json",mode="w") as wrf:
        json.dump(todos, wrf)
    wrf.close()

