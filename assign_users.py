class users:
    counter = 0
    
    def get_data(self):
        self.name = input("name: ")
        self.password = input("password: ")
        self.email = input("email: ")
    
    
    def creat_file(self):
        self.counter+=1
        new_file = open(f"{self.name}'s_todos.json","w")
        user_data_dict = {}
        user_data_dict[self.name] = [self.counter,self.name,self.password,self.email]
        first_item_name = str(user_data_dict)
        new_file.write(first_item_name)
        
    

hamed = users()
hamed.get_data()
hamed.creat_file()