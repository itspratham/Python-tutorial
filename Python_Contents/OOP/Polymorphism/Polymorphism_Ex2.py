class Documnet(object):

    def __init__(self, name):
        self.name =  name

    def show(self):
        """ Abstract method
        We are raising the NotImplementedError in case anyone tries to use the menthod"""
        raise NotImplementedError("Subclass must implment the abstract method")

class PDF(Documnet):
    def show(self):
        print("File Name:{}\tShow PDF content".format(self.name))

class Word(Documnet):
    def show(self):
        print("File Name:{}\tShow Word content".format(self.name))


class Image(Documnet):
    def show(self):
        print("File Name:{}\tShow Image content".format(self.name))


doc = [PDF("MyPDFDoc1"), PDF("MyPDFDoc2"), Word("MyWordDoc1"), \
       PDF("MyPDFDoc3"),Word("MyWordDoc2"), Image("MyImage1")]
for d in doc:
    d.show()

