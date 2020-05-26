
name = input("isminizi giriniz:\n")
age = int(input("yaşınızı giriniz:\n"))
educationState = input("öğrenim durumunuzu giriniz:\n")

lowerCaseEducationState = educationState.lower()
if age > 18 and (lowerCaseEducationState == "lise" or lowerCaseEducationState == "üniversite"):
    print("ehliyet alabilirsin")
else:
    print("ehliyet alamazsın")


yazili1 = float(input("yazili1 notunuz:"))
yazili2 = float(input("yazili2 notunuz:"))
sozlu = float(input("sozlu notunuz:"))

ortalama = (yazili1 + yazili2 + sozlu) / 3.0

if 0 <= ortalama <= 24:
    print("0")
elif 25 <= ortalama <= 44:
    print("1")
elif 45 <= ortalama <= 54:
    print("2")
elif 55 <= ortalama <= 69:
    print("3")
elif 70 <= ortalama <= 84:
    print("4")
elif 85 <= ortalama <= 100:
    print("5")


name = input("isminiz?")
kg = float(input("kilonuz?"))
height = float(input("boy uzunluğunuz?"))

index = kg / (height ** 2)

if index >=0 and index <= 18.4:
    print("zayif")
elif index > 18.4 and index <= 24.9:
    print("normal")
elif index > 24.9 and index <= 29.9:
    print("kilolu")
elif index > 29.9 and index <= 34.9:
    print("obez")

