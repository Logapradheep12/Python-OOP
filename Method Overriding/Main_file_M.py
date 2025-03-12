class user:             
        
    def register(self):
        print("Registering...")
        
    def login(self):
        print("Logging in...")
        
    def greek(self):
        print("Hello User...")


class students(user):                   
    def greek(self):                                 # OverRide To parent Class
        print("Hiii ............... Students")

class faculty(user):                    
    def greek(self):
        print("Hiii...............Teachers")
    
class tempfaculty(faculty):                             # OverRide To parent Class
    def greek(self):
        print("Hello Guys............ Nice to meet You")