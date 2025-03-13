class user:
    def __init__(self,user_name,pwd):
        self.user_name=user_name
        self.pwd=pwd
        
    def register(self):
        print("Registering     ")
        
    def login(self):
        print("Logging in     ")
        


class students(user):  
    
    def __init__(self, user_name, pwd, course, fee):
        # Call Super Function variables
        super().__init__(user_name, pwd) 
        self.course = course
        self.fee = fee
                      
    def student(self):                                 # OverRide To parent Class
        print("Hiii details are ...............",self.user_name, self.pwd, self.course, self.fee)

class faculty(user):                    
    def teacher(self):
        print("Hiii...............Teachers")
    
class tempfaculty(faculty):                             # OverRide To parent Class
    def temp_teacher(self):
        print("Hello Guys............ Nice to meet You")