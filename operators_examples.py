

x = int(input("sayi giriniz:"))
result = 0 < x < 100 # result > 0 and result < 100
print(f"0-100 arasında mı? ==> {result}")


x = int(input("sayi giriniz:"))
result = ((x > 0) and (x % 2 == 0))
print(f"pozitif çift sayı {result}")

email = "batux@gmail.com"
password = "12345"

userEmail = input("Kullanıcı email adresi:\n")
userPassword = input("Kullanıcı şifresi:\n")

result = (email == userEmail) and (password == userPassword)
print(f"giriş başarılı mı? {result}")

a = int(input("birinci sayıyı giriniz:"))
b = int(input("ikinci sayıyı giriniz:"))
c = int(input("üçüncü sayıyı giriniz:"))

result = a > b and a > c
print(f" a en büyük sayıdır: {result}")

result = b > a and b > c
print(f" b en büyük sayıdır: {result}")

result = c > a and c > b
print(f" c en büyük sayıdır: {result}")


vize1 = float(input("Vize1 notunu giriniz:"))
vize2 = float(input("Vize2 notunu giriniz:"))
final = float(input("Final notunu giriniz:"))

ortalama = (vize1 * 0.6) + (vize2 * 0.6) + (final * 0.4)

if final > 70:
    print("Dersten geçtiniz")
elif ortalama > 50 and final > 50:
    print("Dersten geçtiniz")
else:
    print("Dersten kaldınız")

