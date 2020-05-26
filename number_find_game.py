import random

total = 0
questionPoint = 20
choice = ""
usableRightCount = 0
userNumber = 0

while True:

    if usableRightCount == 0:
        randomNumber = int(1 + random.random() * 99)
        print(randomNumber)

        rightLimit = int(input("kaç adet can hakkı istiyorsun?"))
        usableRightCount = rightLimit
        
    userNumber = int(input("sayi gir:\n"))

    if userNumber > randomNumber:
        usableRightCount -= 1
        if usableRightCount == 0:
            print("Üzgünüm kaybettin bro!")
            choice = input("Çıkmak istersen Q'ya, devam için herhangi bir tuşa bas!")
            if(choice.lower() == "q"):
                break
        else:
            print(f"Kalan can hakkın: {usableRightCount} Aşağı yönde sayı gir!")
    elif userNumber < randomNumber:
        usableRightCount -= 1
       
        if usableRightCount == 0:
            print("Üzgünüm kaybettin bro!")
            choice = input("Çıkmak istersen Q'ya, devam için herhangi bir tuşa bas!")

            if(choice.lower() == "q"):
                break
        else:
            print(f"Kalan can hakkın: {usableRightCount} Yukarı yönde sayı gir!")
    else:
        currentPoint = int(questionPoint * (usableRightCount / float(rightLimit)))
        total = total + currentPoint
        print(f"Tebrikler Kazandın! Toplam Puan: {total}")
        usableRightCount = 0
        rightLimit = 0
        choice = input("Çıkmak istersen Q'ya, devam için herhangi bir tuşa bas!")

        if(choice.lower() == "q"):
            break


print("oyun bitti!")