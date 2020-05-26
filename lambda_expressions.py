

def square(n): return n*n

numbers = [3, 5, 8, 10, 2]

# fonksiyonu ve listeyi map'e gönder. her item için tek tek bu fonksiyonu işletir.
print(list(map(square, numbers)))

# lambda ifadesiyle fonkiyon yaratabilirsin.
kup = lambda number: number**3

print(list(map(kup, numbers)))


oddNumbersCollector = lambda number: number % 2 > 0
evenNumbersCollector = lambda number: number % 2 == 0

evenNumbers = list(filter(evenNumbersCollector, numbers))
print(evenNumbers)

oddNumbers = list(filter(oddNumbersCollector, numbers))
print(oddNumbers)


# global değişken
sayi = 10

def karesi(sayi):
    # sayi lokal değişken
    sayi = sayi ** 2

    def topla(sayi):
        # nested lokal değişken
        sayi = sayi + 100
        return sayi
    
    return topla(sayi)

print(karesi(sayi))
print(sayi)

# eğer hep global değişkeni kullanmak istiyorsam "global" anahtar kelimesini kullanabilirim.
def karesiGlobal():
    global sayi
    sayi = sayi ** 2

    def toplaGlobal():
        global sayi
        sayi = sayi + 100
        return sayi
    
    return toplaGlobal()

print(karesiGlobal())
print(sayi)