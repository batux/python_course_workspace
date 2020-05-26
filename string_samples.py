
def extract(word, text):

    firstCharacter = word[0]
    firstIndex = text.index(firstCharacter)
    return text[firstIndex : firstIndex + len(word)]


website = "http://www.batuhanduzgun.com"
course = "Python Kursu: From Zero to Hero Course"

courseLength = len(course)
print(f"Course word length is {courseLength}")

lastOccurenceIndexOfL = website.rindex("/")
print(f"Last occurence index is : {lastOccurenceIndexOfL}")

firstOccurenceIndexOfL = website.index("/")
print(f"First occurence index is : {firstOccurenceIndexOfL}")


protocolPrefix = website[lastOccurenceIndexOfL + 1 : lastOccurenceIndexOfL + 4]
print(protocolPrefix)

print( extract("www", website) )

print( extract("com", website) )

first15CharacterOfCourse = course[:15]
print(first15CharacterOfCourse)

last15CharacterOfCourse = course[-15:]
print(last15CharacterOfCourse)

# reverse of string is so basic :)
print(course[::-1])



## String Methods

#1
sampleMessage = "  Hello word   "
print(sampleMessage)
print(sampleMessage.strip())

# sadece sağdan veya soldan boşlukları temizliyor
print(sampleMessage.rstrip())
print(sampleMessage.lstrip())


#2
# index metodu bulamazsa hata fırlatır.
# find metodu ise bulamazsan hata döndürmez, -1 değer döner.
lastIndexOfDot = website.rindex(".")
firstIndexOfDot = website.index(".")
print(website[firstIndexOfDot + 1 : lastIndexOfDot])

# yada
# silinmesini istediğin karakterleri verebiliyorsun.
print( website.strip("w.moc/pht:") )

#3
print(website.lower())

#4
# a harfinden kaç tane olduğunu sayıyor.
print(website.count("a"))

#5
print(website.find(".com"))
print(website.startswith(".com"))
print(website.endswith(".com"))


#6
#karakterlerin hepsi alfanumeric mi kontrol ediyor.
print(website.isalpha())
#karakterlerin hepsi numeric mi kontrol ediyor.
print(website.isdigit())

#7
print(website.center(50, "*"))

#8
print(course.replace(" ", "-"))

print(course.replace("Zero", "Hero"))

print(course.split())
