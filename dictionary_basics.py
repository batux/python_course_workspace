

plateNumbers = {
    1: "Adana",
    6: "Ankara",
    8: "Artvin",
    34: "İstanbul",
    45: "Manisa",
    54: "Sakarya"
}

print(plateNumbers)

print(plateNumbers[8])

plateNumbers[77] = "Yalova"

print(plateNumbers)

users = {
    1: {
        "name": "Batuhan",
        "surname": "Düzgün",
        "age": 32,
        "email": "batux@gmail.com",
        "roles": ["super", "admin", "customer"]
    },
    2: {
        "name": "Sevil",
        "surname": "Düzgün",
        "age": 30,
        "email": "sevo@gmail.com",
        "roles": ["super", "customer"]
    }
}

print(users[1]["roles"])
print(users[2]["roles"])


def insertStudent(students):

    studentNo = int(input("Öğrenci No giriniz:\n"))

    studentName = input("Öğrenci Adı giriniz:\n")

    studentSurname = input("Öğrenci Soyadı giriniz:\n")

    studentTelephone = input("Öğrenci Telefon giriniz:\n")

    students[studentNo] = {
        "name": studentName,
        "surname": studentSurname,
        "telephone": studentTelephone
    }

def getStudent(students):

    id = int(input("Öğrenci no giriniz:\n"))
    return students[id]   


flag = True
students = {}

while flag:

    print("1- Öğrenci ekle")
    print("2- Öğrenci ara")
    print("3-Çıkış")
    choice = int(input())

    if choice == 1:
        insertStudent(students)
    elif choice == 2:
        student = getStudent(students)
        if student != None:
            print(student)
        else:
            print("Aradığınız kayıt buluanamadı!")
    elif choice == 3:
        break