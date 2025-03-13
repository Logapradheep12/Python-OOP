class father:
    hair_colour = "white"
    
    def music(self):
        print("Kutthu songs")

class mother:
    hair_colour = "white"
    eye_color = "black"
    
    def music(self):
        print("Melody Songs")
        
class child(father, mother):
    no_of_legs = 2
    

child1 = child()

child1.music()