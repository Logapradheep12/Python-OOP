from Main_file_I import *

user1 = user()                    #  Parent class

user1.register()
user1.login()

stu1 = students()                 #  child class
stu1.greek_student()

fac1 = faculty()                  #  Child class
fac1.greek_faculty()

temp1 = tempfaculty()             # Multilevel Inheritance
temp1.register()

temp_stu1 = temp_students_faculty()
temp_stu1.greek_temp_student_faculty()