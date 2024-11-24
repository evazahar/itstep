class ProgrammingLanguage:
    def  init (self, name):
self.name=name

    def display greeting(self):
         print (f"Hello! I am {self.name), one of the best programming languages!")

class Python(Programming Language):
    def   init   (self):
        super().init ("Python")

class Java(ProgrammingLanguage):
    def    init   (self) :
        super().init ("Java")
class CPlusPlus(Programming Language):
    def    init   (self):
        super(). init ("C++")
ifname== " main "=
   python =Python()
   java =Java()
   cpp=CPlusPlus()

python.display_greeting()
java.display greeting()
cpp.display_greeting()
