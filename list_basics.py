
def changeElement(brandList, currentElement, willChangeElement):

    for index in range(0, len(brandList)):
        brand = brandList[index]
        if currentElement == brand:
            brandList[index] = willChangeElement
            break

    return brandList



numbers1 = [1, 2, 3, 4, 5]
numbers2 = [6, 7, 8, 9, 10]
# + operatorü her iki lsiteyi birleştirir.
joinedNumbers = numbers1 + numbers2
print(joinedNumbers)

students = [ "Batuhan Düzgün", "Fuat Düzgün", "Barkın Düzgün", "Zeynep Düzgün" ]
teachers = [ "Sevil Düzgün", "Mustafa Akyel" ]

users = [ students, teachers ]

print(users)


vehicles = ["Mazda", "Toyota", "Mercedes", "BMW", "Honda", "Subaru", "Fiat"]

lengthOfVehicles = len(vehicles)
print(f"Length of array is {lengthOfVehicles}")
print(f"First element of array is : {vehicles[0]}")
print(f"Last element of array is : {vehicles[lengthOfVehicles - 1]}")

vehicles = changeElement(vehicles, "Mercedes", "Porche")
print(vehicles)

# liste içinde eleman var mı yok mu ?
print(vehicles.index("Toyota"))
result = "Toyota" in vehicles
print(result)

print(vehicles[-2])
print(vehicles[::-1])

# ilk 3 elemanı alırsın
print(vehicles[:3])
# son 3 elemanı alırsın
print(vehicles[3:])

vehicles.append("Nissan")
vehicles.append("Audi")
print(vehicles)

# veya direkt sub array ekleyebilirsin
vehicles = vehicles + ["Nissan", "Audi"]
print(vehicles)

vehicles.remove(vehicles[len(vehicles) - 1])
print(vehicles)


# son 2 elemanı değiştirmek
vehicles[-2:] = ["Mustang", "Ferrari"]
print(vehicles)



minValueOfVehicles = min(vehicles)
print(minValueOfVehicles)
maxValueOfVehicles = max(vehicles)
print(maxValueOfVehicles)

minValueOfNumbers = min(numbers1)
print(minValueOfNumbers)
maxValueOfNumbers = max(numbers1)
print(maxValueOfNumbers)

numbers1.append(34)
print(numbers1)

numbers1.remove(numbers1[2])
print(numbers1)

numbers1.insert(2, 45)
print(numbers1)

# listeden son elemanı alır ve çıkarır
print(numbers1.pop())

numbers1.sort()
print(numbers1)

numbers1.reverse()
print(numbers1)


names = ["Ali", "Yağmur", "Hakan", "Deniz"]
years = [1988, 1989, 1991, 1995]

names.append("Cenk")
print(names)

names.insert(0, "Sena")
print(names)

print(names.index("Deniz"))

names.remove(names[len(names) - 1])
print(names)

print("Ali" in names)

print(names.reverse())

print(names.sort())

print(years.sort())

str = "Chevrolet, Fiat"

brands = str.split()
print(brands)

print(min(years))

print(max(years))

print(years.count(1998))

print(years.clear())

mybrands = []
brand = input("Araç markası giriniz\n")
mybrands.append(brand)

brand = input("Araç markası giriniz\n")
mybrands.append(brand)

brand = input("Araç markası giriniz\n")
mybrands.append(brand)

print(mybrands)