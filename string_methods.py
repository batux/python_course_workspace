

message = "Merhaba, güzel dünya çok harikasın :)"

upperMessage = message.upper()
print(upperMessage)

lowerMessage = message.lower()
print(lowerMessage)

# kelimelerin ilk harflerini büyük yapar.
titleMessage = message.title()
print(titleMessage)

# sadece ilk harfi büyüük yapar.
capitalizeMessage = message.capitalize()
print(capitalizeMessage)

# boşlukları temizler
spaceMessage = "   " + message + "   "
print(spaceMessage)
print(spaceMessage.strip())

# kelimelere ayırır. (boşluk karakterine göre)
words = message.split()
print(words)

commaWords = message.split(",")
print(commaWords)

# join fonksiyonu içine dizi vermek lazım :) o dizidekileri birleştiriyor.
joinedMessage = " ".join(words)
print(joinedMessage)

# kelimeleri birleştirirken araya yıldız koyar.
joinedStarMessage = "*".join(words)
print(joinedStarMessage)

numbers = [ 1, 5, 34, 45, 54, 8]
# basit bir for loop ile stringe çevirip kullanabilirsin
print(" - ".join(str(number) for number in numbers))


firstIndexOfDunya = message.find("dünya")
print(firstIndexOfDunya)

print(message.startswith("Merhaba"))
print(message.endswith("Merhaba"))

messageWithoutTurkish = message.replace("ü", "u").replace("ö", "o").replace("ç", "c")
print(messageWithoutTurkish)

# sağına ve soluna 100 karakter ekliyor.
print(messageWithoutTurkish.center(100, "*"))