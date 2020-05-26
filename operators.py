
x, y, z = 1, 4, 5

print(x,y,z)

x += 1
y += 2
z += 3

print(x,y,z)

# creates auto tuple
values = 1, 2, 4, 6, 7

print(type(values))
print(values)

# a,b,c değerleri sırayla atanır, kalanlarla d değerine biz alt dizi oluşturulur.
a, b, c, *d = values

print(a, b, c, d)