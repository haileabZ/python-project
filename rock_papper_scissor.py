import random
flag=True;
draw=loss=win=0;
while flag:
    game_list=["rock","papper","scissor"]
    index = random.randint(0,2);
    computer_move=game_list[index].lower()
    your_move=input("enter rock,papper or scissor\n").lower()
    while your_move not in game_list:
        your_move = input("enter rock,papper or scissor\n").lower()
    print("your move is",your_move)
    print("computer move is ",computer_move)
    if(computer_move==your_move):
        draw += 1
        print("you draw!")
    elif (your_move=="scissor" and computer_move =="rock"  ):
        loss += 1
        print("you loss!")

    elif (your_move == "scissor" and computer_move == "papper"):
        win += 1
        print("you win!")

    elif (your_move == "papper" and computer_move == "rock"):
        win += 1
        print("you win!")
    elif (your_move == "papper" and computer_move == "scissor"):
        draw += 1
        print("you draw!")
    elif (your_move == "rock" and computer_move == "papper"):
        loss += 1
        print("you loss!")
    else:
        win += 1
        print("you win!")
    response=input("wanna exit new game say y to exit and see the score")
    if(response.lower()=="y"):
        flag=False
        print("you win",win,"times\n","you loss",loss,"times\n","you draw",draw,"times")
