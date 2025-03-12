class user:
    def __init__(self,user_name,pwd):
        self.user_name=user_name
        self.pwd=pwd
        
    def register(self):
        print("Registering     " +self.user_name)
        
    def login(self):
        print("Logging in     " +self.pwd)