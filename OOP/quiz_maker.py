
class Question:

    def __init__(self, questionText, options, answer, score):
        self.questionText = questionText
        self.options = options
        self.answer = answer
        self.score = score
    

class QuestionDisplayer:

    @staticmethod
    def displayQuestion(id, question):
        
        print(f"{id}-) {question.questionText}\n")

        for option in question.options:
            print(str(option) + "\n")
        

class AnswerCollector:

    @staticmethod
    def typeAnswer():
        answer = input("Cevap: ").strip()
        return answer

class Quiz:

    score = 0
    rightAnswerCount = 0
    wrongAnswerCount = 0
    questionsMap = {}

    def __init__(self, questions):
        self.questions = questions
        self.indexQuestions(self.questions)


    def indexQuestions(self, questions):
        id = 1
        for question in questions:
            self.questionsMap[id] = question
            id += 1

    def start(self):

        for id, question in self.questionsMap.items():

            QuestionDisplayer.displayQuestion(id, question)
            answer = AnswerCollector.typeAnswer()

            if str(question.answer).lower() == str(answer).lower():
                self. score += question.score
                self.rightAnswerCount += 1
            else:
                self.wrongAnswerCount += 1

        print("Quiz bitti!")
        print(f"Toplam doğru sayısı: {self.rightAnswerCount}")
        print(f"Toplam yanlış sayısı: {self.wrongAnswerCount}")
        print(f"Toplam puan: {self.score}")


q1 = Question("Java kaç yılında ortaya çıkmıştır?", [1995, 1996, 1997, 1998], 1995, 20)
q2 = Question("Java çoklu kalıtımı destekler?", ["Evet", "Hayır", "Duruma göre değişir", "Bilinemez"], "Hayır", 20)
q3 = Question("Python çoklu kalıtımı destekler?", ["Evet", "Hayır", "Duruma göre değişir", "Bilinemez"], "Evet", 10)
q4 = Question("Python lambda ifadelerini içerir?", ["Evet", "Hayır"], "Evet", 5)
q5 = Question("Swing, Java'nın GUI kütüphanesidir?", ["Evet", "Hayır"], "Evet", 5)
q6 = Question("Python yorumlanan bir dildir?", ["Evet", "Hayır"], "Evet", 5)
q7 = Question("Java hem yorumlanan hem derlenen bir dildir?", ["Evet", "Hayır"], "Evet", 5)
q8 = Question("Spring Framework'ün en büyük faydası nedir?", ["Dependency Injection", "IoC", "Java ile yazılması", "OOP"], "IoC", 30)

questions = [ q1, q2, q3, q4, q5, q6, q7, q8  ]

quiz = Quiz(questions)
quiz.start()