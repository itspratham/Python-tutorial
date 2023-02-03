import abc
from abc import ABC


class A(ABC):
    def __init__(self):
        pass

    @abc.abstractmethod
    def play(self):
        print("Play")


class B(A):
    def __init__(self):
        super().__init__()

    def play(self):
        print("play")

    def pll(self):
        print()


b = B()
b.play()
