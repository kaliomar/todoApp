import json

todol = {}

def dict_to_text():
    text = json.dumps(todol)
    return text

def re_file(): # to read todos from file
    with open("vault.json","r") as remember:
        todol = json.load(remember)
    return todol

def todo(): #this function for adding mission to dict
    date = input("select date: ")
    mission = input("mission: ")
    re_file()
    if date not in todol.keys(): # add mission to new dates
        todol[date] = mission
        return todol
    
    else: # add mission to current existance date
        if type(todol[date]) == list: # there are many todos on this date
            li = []
            for i in todol[date]:
                li.append(i)
            li.append(mission)
            todol[date] = li
            return todol
        
        else: # there is one mission on this date
            li = [todol[date],mission]
            todol[date] = li
            return todol

def output(): # to print out mission of specific date
    date = input("select date: ")
    re_file()
    if date not in todol.keys(): # user date isn't in our dict
        print("not existance")
    
    else: # user date is in our list
        if type(todol[date]) == list: # but date has many mission on it
            for i in todol[date]:
                print(i)
        
        else: # date has one mission on it 
            print(todol[date])

def asking(): # to ask if user want to add or check date and mission
    which = input("Add new todo select 'i':\nCheck mission of date select 'o':\nType your selection: ")
    numof = int(input("How many times do you need to try: "))
    if which == 'i': # if user choose to add
        for i in range(numof):
            todo()
    elif which == 'o': # if user choose to check
        for i in range(numof):
            output()
    else: # if user is a stupid asshole 
        print("not allowed choice")

def wr_file(): # to save todos to file
    with open("vault.txt","w") as wr_file
    asking()
    text = (dict_to_text())
    memory.write(text)
    memory.close()
    print("all is well")

asking()