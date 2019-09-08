class Human(object):
    # Constructor
    def __init__(self, name, hand, legs, mouth=1):

        self.name = name
        self.legs = legs
        self.hands = hand
        self.mouth = mouth
        print("{} is born".format(self.name))

    # Destructor
    def __del__(self):
        print("{} is dead".format(self.name))
        del self.name
        del self.hands
        del self.mouth
        del self.legs

    def disply_human(self):
        print("Name is : {}".format(self.name))
        print("Legs {}".format(self.legs))
        print("Hands {}".format(self.hands))
        print("Mouth {}".format(self.mouth))

    def walk(self):
        print ("{} is walking".format(self.name))

    def talk(self):
        print("{} is talking".format(self.name))

    def clap(self):
        print("{} is clapping".format(self.name))


jhon_o = Human("Jhon",2,2,2)   # Initilization is called implicite
jhon_o.disply_human()
jhon_o.walk()
jhon_o.talk()
jhon_o.clap()
jhon_o.walk()

print("=======================")
joe = Human("Joe",2,2)
joe.disply_human()
joe.walk()
joe.talk()
joe.clap()

