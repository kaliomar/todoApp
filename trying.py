import json

def re_file(): # to read todos from file
    with open("vault.json","r") as remember:
        todol = json.load(remember)
    return todol


def wr_file(): # to save todos to file
    with open("vault.txt","w") as wr_file:
    asking()
    text = (dict_to_text())
    memory.write(text)
    memory.close()
    print("all is well")
