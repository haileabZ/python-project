

import random
import time

class quiz:

    def __init__(self,num_questions):
         self.num_questions=num_questions

    def prompt(self,result):
        user_input = int(input("enter your result\n"))
        if result == user_input:
            print("you got it!")
        else:
            print("you got wrong answer correct answer is", result)
    def generateQuestion(self):
        start_time=time.time()
        for question in range(self.num_questions):
            result=None
            operators = ["+", "/", "*", "-", "%"]
            rand_operator = random.choice(operators)
            operand1=random.randrange(1,50)
            operand2=random.randrange(1,50)
            print(operand1,rand_operator, operand2)
            match rand_operator:
                  case "+":
                    result = operand1 + operand2
                  case "-":
                    result = operand1 - operand2
                  case  "*":
                    result = operand1 * operand2
                  case  "/":
                    result = operand1 / operand2
                  case  "%":
                    result = operand1 % operand2
                  case _:
                      print("unknown operand")
            self.prompt(result)
        end_time=time.time()
        print("you use {:.3f}".format(end_time-start_time),"seconds")


quiz1=quiz(int(input("enter number of question you want to?")))
quiz1.generateQuestion()
