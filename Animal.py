class Animal:
    def __init__(self, name, species, gender, age, color, hp = 100):
        self.__name = name 
        self.__species = species
        self.__gender = gender
        self.__age = age
        self.__color = color
        self.__hp = hp
        print("hello, I am", self.__name)
    
    def age(self):
        print (f'Today i turn, {self.__age} years old')
        
    def color(self):
        print (f'I can camoflauge in areas that are dark since my color is, {self.__color}')

    def battle(self):
        self.__hp -=1
        print ("ROAR")
        print (f'You have {self.__hp}, hp left in the tank (-1 hp)')

    def rest(self):
        print ("HUFF")
        print (f'You have {self.__hp}, hp left in the tank (+1 hp)')

    def walk(self, walk):
        self.__walk = walk
        print("I hate to", self.__walk)
    
    def lift(self,lift):
        self.__lift = lift
        print("I can lift more than", self.__lift)

    def talk(self):
        print(self.__name)

    def print_species(self):
        print("I am a",self.__species)

    def print_gender(self):
        print("I am a",self.__gender)

    def excrete_waste(self):
        print("I have excreted my waste")
    

    def eat(self):
        print(self.__name, "is eating.")

    def sleep(self):
        print(self.__name, "is sleeping.")

    def cry(self):
        print(self.__name, "is crying.")

    def running(self):
        print(self.__name, "is running")