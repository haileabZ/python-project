import random

questions=[
           {"q":". what does RAM stand for?",
            "a":"A. random acess memory",
            "b":"B. read acess memory",
            "c":"C. rotate acess memory",
            "answer":"a"
            },
           {"q":". what does CPU stand for?",
            "a":"A. cemos processing unit",
            "b":"B. create processor unit",
            "c":"C. central processing unit",
            "answer":"c"
            },
           {"q":". what does ROM stand for?",
            "a":"A. random only memory",
            "b":"B. read only memory",
            "c":"C. rotate only memory",
            "answer":"b"
            }
           ]
random.shuffle(questions)
# print(questions)
count=0
index=0
for i in questions:
  index+=1
  print(index,i["q"])
  print("  ",i["a"])
  print("  ",i["b"])
  print("  ",i["c"])

  answer=input("enter your choice").lower()
  if(i["answer"]==answer):
    count+=1
    print("you got it!")
  else:
    print("correct answer is",i[i["answer"]])
print("you got ",count,"out of ",index,"questions")

