class fav_animal:
    def __init__(self):
        self.arms = float(5)
        self.legs = float(7)
        self.eyes = int(2)
        self.tail = True
        self.furry = False

    def attributes(self):
        print("Length of the arms is: ", self.arms)
        print("Length of the legs is: ", self.legs)
        print("Number of eyes there are: ", self.eyes)
        print("Does it have a tail? ", self.tail)
        print("Is it a furry: ", self.furry)



def main():
    animal = fav_animal()
    animal.attributes()
    
    

if __name__=="__main__":
    main()

    