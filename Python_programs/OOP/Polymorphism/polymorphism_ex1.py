class Cat(object):
    def makesound(self):
        print("Meawo")

class Dog(object):
    def makesound(self):
        print("Bow Bow")

class Cow(object):
    def makesound(self):
        print("Ambaa")

def makesound(animalType):
    animalType.makesound()

cat =Cat()
makesound(cat)

dog = Dog()
makesound(dog)

cow = Cow()
makesound(cow)