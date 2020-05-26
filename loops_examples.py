
productLimit = int(input("Kaç ürün gireceksiniz?"))

productCounter = 0

products = {}

while productCounter < productLimit:

    name = input("ürün ismi?").strip()
    price = float(input("ürün fiyatı?").strip())

    products[name] = (name, price)
    productCounter += 1

for key, value in products.items():
    print(f"Key: {key}, Value: {value}")


