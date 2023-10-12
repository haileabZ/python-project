flag=True
while flag:
    name=input("enter your name\n")
    print("well come",name)
    answer=input("you are on the dirt it has to come end and you can go left or right, which do you choose(left,right)\n")
    while answer not in ["left","right"]:
        answer = input(
            "you are on the dirt it has to come end and you can go left or right, which do you choose(left,right)\n")
    if answer=="left":
        answer = input(
            "you come to a river, you walk around it or swim across? what do you choose(walk,swim)\n")
        while answer not in ["walk","swim"]:
            answer = input(
                "you come to a river, you walk around it or swim across? what do you choose(walk,swim)")
        if answer=="walk":
            print("you walked for many miles, ran out oxygen then you will loss")
        else:
            print("you swam across and were eaten by alligator.")
    if answer=="right":
        answer=input("you come to a bridge,it looks wobby, do you want cross or back (cross,back)\n ")
        while answer not in ["cross", "back"]:
            answer = input("you come to a bridge,it looks wobby, do you want cross or back (cross,back) \n")
        if answer=="back":
            print("you go back and loss")
        else:
            print("you got follow the correct path")
