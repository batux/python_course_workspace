
class Person:
    # yer tutucudur, kod yazmasan da hata vermez
    pass

     #class attributes
    address = ""

    # constructor method
    def __init__(self, name, surname, year):
        # object attributes
        self.name = name
        self.surname = surname
        self.year = year
        print("Constructor method was run!")

    # class methods
    def getFullName(self):
        return self.name + " " + self.surname
    
    def calculateAge(self):
        return 2020 - self.year

p1 = Person("Batuhan", "Düzgün", 1988)
p1.address = "Akhisar"

p2 = Person("Ali", "Ahmet", 1986)
p2.address = "İstanbul"

print(p1.getFullName())
print(p1.address)
print(p1.calculateAge())

print(p2.getFullName())
print(p2.address)
print(p2.calculateAge())

class Circle:

    PI = 3.14

    def __init__(self, yariCap = 0):
        self.yariCap = yariCap
    
    def cevreHesapla(self):
        return 2 * self.PI * self.yariCap
    
    def alanHesapla(self):
        return self.PI * (self.yariCap ** 2)
    
c1 = Circle(5)
print(f"Alan: {c1.alanHesapla()}")
print(f"Çevre: {c1.cevreHesapla()}")