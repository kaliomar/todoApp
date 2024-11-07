import json
import todoapp 

def re_file(): # to read todos from file
    with open("vault.json","r") as remember:
        magic = json.load(remember)
    return magic

def wr_file(): # to save todos to file
    text = todoapp.todo()
    if text == "file is empty in ":
        print(text)
    else:
        with open("vault.json",mode="w",encoding = "utf-8") as wr_file:
            json.dump(text,wr_file)
        wr_file.close()
        
wr_file()