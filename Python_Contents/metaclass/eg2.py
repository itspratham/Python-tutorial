class Philosopher1:

    def the_answer(self, *args):
        return 42


class Philosopher2:
    def the_answer(self, *args):
        return 42


class Philosopher3:
    def the_answer(self, *args):
        return 42


plato = Philosopher1()
print(plato.the_answer())
kant = Philosopher2()
# let's see what Kant has to say :-)
print(kant.the_answer())