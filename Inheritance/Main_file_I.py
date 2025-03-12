


class user:              #  Parent class
        
    def register(self):
        print("Registering     ")
        
    def login(self):
        print("Logging in     ")


class students(user):                   #  child class
    def greek_student(self):
        print("Hiii ............... Students")

class faculty(user):                    #  child class
    def greek_faculty(self):
        print("Hiii...............Teachers")
    
class tempfaculty(faculty):              # Multilevel Inheritance
    def greek_tempfact(self):
        print("Hello Guys............ Nice to meet You")
        
class temp_students_faculty(faculty,students):                   
    pass
