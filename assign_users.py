import json

class users:
    
    def get_data(self):
        self.name = input("name: ")
        self.password = input("password: ")
        self.email = input("email: ")
    
    
    def creat_file(self):
        new_file = open(f"{self.name}'s_todos.json","w")
        user_data_dict = {}
        user_data_dict[f"{self.name}'s_data"] = [self.name,self.password,self.email]
        json.dump(user_data_dict,new_file)
    

