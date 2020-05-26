
# immutable list is tuple
tuple_example = ("Sevil", "Batuhan", "Berkehan")

print(type(tuple_example))


for item in tuple_example:
    print(item)

print(tuple_example.count("Sevil"))

subtuple = ("Fuat", "Zeynep")

tuptuple_example = tuple_example + subtuple

print(tuptuple_example)