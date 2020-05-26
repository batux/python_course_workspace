
# set mükerrer kayıt içermez
# indeks ile erişemezsin
name_set = { "batuhan", "batuhan", "sevil", "zeynep" }
print(name_set)

numbers = [1,2,3,3,5,5,6,7,7,7,9,9,1]
set_numbers = set(numbers)
print()

for item in set_numbers:
    print(item)

## eleman çıkarmak için her ikis de kullanılır.
set_numbers.discard(1)
set_numbers.remove(3)

set_numbers.update([5, 8, 9, 10, 11])
print(set_numbers)

name_set.add("balkanska")
print(name_set)


# listeler referans tiplerdir.
numbers1 = [1,3,4,5]
numbers2 = [6,7,8,9]

# = ifadesiyle numbers1 değişkeni artık numbers2'nin bellek adresini gösterir
numbers1 = numbers2

numbers2.remove(9)

print(numbers1, numbers2)