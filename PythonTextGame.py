from random import randint
import operator

print("This is an educational game where you will answer simple math questions.")
print("How many questions would you like to answer?")

questionInput = input()

def MathQuestion(questionInput):
    questionLoop = 0
    score = 0
    try:
        while questionLoop < int(questionInput):
            value1 = randint(1, 20)
            value2 = randint(1, 20)
            operationVariable = randint(0, 3)
            if operationVariable == 0:
                correctMathAnswer = operator.add(value1, value2)
                operation = "+"
            elif operationVariable == 1:
                correctMathAnswer = operator.sub(value1, value2)
                operation = "-"
            elif operationVariable == 2:
                correctMathAnswer = operator.mul(value1, value2)
                operation = "*"
            elif operationVariable == 3:
                while value1 % value2 != 0:
                    value1 = randint(1, 20)
                    value2 = randint(1, 20)
                correctMathAnswer = operator.truediv(value1, value2)
                operation = "/"
            print()
            print("What is " + str(value1) + operation + str(value2) + "?")
            userInput = input()
            try:
                if float(userInput) == correctMathAnswer:
                    print("Yes! That is the correct answer!")
                    score += 1
                    print("Your score is: " + str(score))
                else:
                    print("That is not the correct answer.")
                    print("Your score is: " + str(score))
            except ValueError:
                print("Please enter a numerical answer.")
            questionLoop += 1
    except ValueError:
        print("Please enter a number!")
        questionInput = input()
        MathQuestion(questionInput)

MathQuestion(questionInput)
