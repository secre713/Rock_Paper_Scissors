import random
print("-------------------------------------")
print("Rock Paper Scissors Big Bang addition")
print("-------------------------------------")
print("1) ✊")
print("2) 🖐️")
print("3) ✌️")
print("4) 🦎")
print("5) 🖖")
player=int(input("player enter your choice(1-5):"))
computer=random.randint(1,5)
choice=["rock","paper","scissors","lizard","spock"]
print("your choice:",choice[player-1])
print("computer choice:",choice[computer-1])
if player>5:
    print("invalid choice!!")
  
if computer==player:
    print("it's a tie")
elif(player==1 and (computer==3 or computer==4))or \
    (player==2 and (computer==1 or computer==5))or \
    (player==3 and (computer==1 or computer==4))or \
    (player==4 and (computer==2 or computer==5))or \
    (player==5 and (computer==1 or computer==3)):
    print("you win!")
else:
    print("you lose.")

