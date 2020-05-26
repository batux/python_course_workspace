
class Person:
    def __init__(self):
        print("Person created!")
    
    def eat(self):
        print("I can eat something!")
    
    def whoAmI(self):
        print("I'm person")

class Student(Person):
    def __init__(self):

        # Java'daki super() gibi :)
        # Person.__init__(self)
        # ya da alternatif super() kullanmak olabilir.
        super().__init__()

        print("Student created!")
    
    # aynı isimle bir metot yazarsak üst sınıftakini ezer. (override)
    def whoAmI(self):
        print("I'm Student")

p1 = Person()
p1.whoAmI()

s1 = Student()
s1.eat()
s1.whoAmI()

