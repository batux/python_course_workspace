import math

while True:

    number = int(input("sayi gir:\n"))
    midOfNumber = int(math.ceil(number / 2.0))

    tamBolenler = []
    for n in range(1, midOfNumber + 1):
        if number % n == 0:
            tamBolenler.append(n)
        
    if len(tamBolenler) == 1:
        print(f"{number} asal sayıdır.")
    else:
        tamBolenler.append(number)
        print(f"{number} sayısının {len(tamBolenler)} tam böleni vardır. Asal sayı değildir!")
        print(f"Tam bölenler listesi {tamBolenler}")
    
    choice = input("Devam etmek için herhangi bir tuşa basınız, çıkmak için Q'ya basınız!")

    if choice.lower() == "q":
        break

