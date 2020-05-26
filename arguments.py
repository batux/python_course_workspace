import math

def changeName(name):
    name = "batuhan"

name = "Kılavuz Ahmet"

# pass by value
changeName(name)
print(name)

def changeList(brands):
    brands[0] = "BMW"

brands = ["Mercedes", "Ferrari", "Porche", "Audi"]

# pass by reference
changeList(brands)
print(brands)

# * ile parametrekelerin hepsinin bir tuple listesi olacağını belirtiyoruz.
def limitlessParameters(*numbers):
    print(numbers)
    print(type(numbers))
    return sum(numbers)

print(limitlessParameters(10, 45, 15, 30))
print(limitlessParameters(1, 4, 1, 3))

# ** ile parametrelerin hepsinin bir dictionary olacağını belirtiyoruz.
def showDictionary(**params):
    print(params)
    print(type(params))

    for key, value in params.items():
        print(f"Key: {key}, Value: {value}")

showDictionary(name="Fiat", price=19222, name1="BMW", price1=283232)


def displayOnConsole(message, limit=1):

    """
    DOCSTRING : my function :)
    """
    counter = 0

    while counter < limit:
        print(message)
        counter += 1
    
    # ya da 
    print(message * limit)

displayOnConsole("batuhan", 10)


def convertToList(*args):
    print(type(args))
    tmpList = []
    for arg in args:
        tmpList.append(arg)
    return tmpList

myList = convertToList(10, 45, 23, 54, 34 )
print(type(myList))

def findAsalSayi(firstNumber, lastNumber):

    asalSayilar = []
    for number in range(firstNumber, lastNumber + 1):

        midOfNumber = int(math.ceil(number / 2.0))

        tamBolenler = []
        for n in range(1, midOfNumber + 1):
            if number % n == 0:
                tamBolenler.append(n)
            
        if len(tamBolenler) == 1:
            asalSayilar.append(number)
    
    return asalSayilar


asalSayilar = findAsalSayi(1, 700)
print(asalSayilar)


def sayininTamBolenleri(number):

    midOfNumber = int(math.ceil(number / 2.0))
    tamBolenler = []
    
    for n in range(1, midOfNumber + 1):
        if number % n == 0:
            tamBolenler.append(n)
    
    tamBolenler.append(number)
    return tamBolenler


print(sayininTamBolenleri(100))