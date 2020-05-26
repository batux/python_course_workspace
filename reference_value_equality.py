
x = y = [1, 4, 5, 11, 3, 9]
z = [1, 4, 5, 11, 3, 9]

# == operatorü bellek referanslarını değil, değerleri kıyaslar!
print(x == y)
print(z == x)

# bellek referansını kıyaslamak istersek "is" operatorü kullanmalıyız!
print(x is y)
print(x is z)

# membership operator is "in"
fruits = ["Apple", "Banana", "Orange"]

print("Kiwi" in fruits)
print("Orange" in fruits)