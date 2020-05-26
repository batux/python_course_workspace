from random import random, uniform, randint, choice, shuffle, sample
from mymodule import *

# 0-1 arasında random sayı üretiyor
print(random())

# düzgün dağılma uygun 0-10 arasında float sayı
print(uniform(0,100))

# 0-100 arasında rastgele tam sayı üretir
print(randint(0,100))


numbers = [ 1, 3, 5, 2, 6, 6, 8, 9, 1 ]
# listeden bir eleman seçiyor
print(choice(numbers))

# listeyi karıştırıyor
shuffle(numbers)
print(numbers)

# numbers listesinden bana 2 tane örnek seçip veriyor.
print(sample(numbers, 2))

sayHello()