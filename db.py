import json

class database:

    def inser_data(self,name,email,password):
        with open('users.json','r') as f:
            users=json.load(f)
            
            if email in users:
                return 0
            else:
                users[email]=[name,password]
        
        with open('users.json','w') as wf:
            json.dump(users,wf)
            return 1
        
    def search(self,email,password):
        with open('users.json','r') as f:
            users=json.load(f)
            if email in users:
                if users[email][1]==password:
                    return 1
                else:
                    return 0
            return 0