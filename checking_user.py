import json

name = input("name: ")
usr_password = input("password: ")
def get_user_data():
    file_name = f"{name}'s_todos.json"
    key_name = f"{name}'s_data"
    all_data = (file_name, key_name, name)
    return all_data

def checking_user():
    tuple_data = get_user_data()
    usr_name,key_name,name = tuple_data
    final_name = name
    try:
        with open(usr_name,"r") as filex:
            new_dict = json.load(filex)

            if name == new_dict[key_name][0]:
                pass
                if usr_password == new_dict[key_name][1]:
                    print("you are log in ../..")
                    import add_and_show
                else:
                    print("wrong password")
                    checking_user()
            else:
                print("No data saved for this name")
                tf = input("If you want to sign up type y: ")
                if tf == "y":
                    import assign_users
                else:
                    print("good bye")
    except:
        print("user not found...")
        opinion = input("IF YOU WANT TO SIGN UP TYPE y: ")
        if opinion == "y":
            import assign_users
            user = assign_users.users()
            user.get_data()
            user.creat_file()
        else:
            print("good bye")
    return final_name
    
