

numbers = [1, 3, 5, 10]

for n in numbers:
    print(n)


coordinates = [ (1,3), (4, 55), (87, 6), (99, 5) ]

for x,y in coordinates:
    print(x,y)

dicti = { 'k1': 1, 'k2': 2, 'k3': 3 }

for d in dicti:
    print(d, dicti[d])


for key, value in dicti.items():
    print(key, value)



counter = 0
total = 0

while counter <= 100:
    total += counter
    counter += 1

print(total)


name = ""

while not name.strip():
    name = input("isim giriniz:")
    name = name.strip()

print(f"Merhaba, {name}")


for item in range(10):
    print(item)

for item in range(50, 100, 2):
    print(item)



name = "Batuhan"
for item in enumerate(name):
    print(item)

for index, value in enumerate(name):
    print(index, value)


list1 = [ 1, 3, 4, 5, 6 ]
list2 = [ "Ali", "Efe", "Can", "Naz", "Ece" ]
mergedList = list(zip(list1, list2))

print( mergedList )


# Comprehensions
numbersList = [ n for n in range(10) ]
print(numbersList)

numbersList = [ n for n in range(10) if n % 2 == 0 ]
print(numbersList)

numbersList = [ n**2 for n in range(10) if n % 2 == 0 ]
print(numbersList)

numbersList = [ n if n % 2 == 0 else 'TEK' for n in range(10) ]
print(numbersList)

numbersList = [ (x, y, z) for x in range(3) for y in range(3) for z in range(3) ]
print(numbersList)