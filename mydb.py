import json
# this function is use to add the data in the json file  and this function take 3 argument(parameter)
class database:
    def add_data(self,name,email,password):

# in this is we open our file in read mode and check the load this file data in the database variable and check it if data is present in the file or not
        with open('db.json','r') as rf:
            database = json.load(rf)
 # if data is present in the database variable so we give the error
        if email in database:
            return 0
# if data is not present in the databse variable then we create new user key value and load this data in the our db json file
        else:
            database[email] = [name,password]
            with open('db.json','w') as wf:
                json.dump(database,wf)
            return 1

    def search(self,email,assword):
        with open('db.json',"r") as rf:
            database = json.load(rf)
            if email in database:
                 if database[email][1]==assword:
                     return 1
                 else:
                     return 0
            else:
                return 0
