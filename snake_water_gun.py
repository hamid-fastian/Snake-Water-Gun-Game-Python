import random

player_Score=0
computer_Score=0
round=0

choices = {
        1:"Snake",
        2:"Water",
        3:"Gun"
    }

while True:
    input("Press Enter to play\n")
    print("1.Snake 🐍")
    print("2.Water 💧")
    print("3.Gun 🔫")
    print("4.Exit")
    
    ## We make a dictionary to choose one element 
    
    ch = int(input("Enter your choice:"))

    if(ch==1):
        us=choices[1]
    elif(ch==2):
        us=choices[2]
    elif(ch==3):
        us=choices[3]
    elif(ch==4):
        break
    else:
        print("====> Invalid !! user input <====")
        continue
    comp =random.choice(["Snake","Water","Gun"])  ## this will randomaly choose one element from list

    round+=1

    print(f"\nRound {round}")
    print(f"Player choice:{us}")
    print(f"Computer choice:{comp}")

    if((us =="Snake" and comp == "Water") or (us == "Water" and comp == "Gun") or (us == "Gun" and comp == "Snake")):
        print("Result: Player wins 🏆 🎉 ✅\n")
        player_Score+=10
    elif((us =="Water" and comp == "Snake") or (us == "Gun" and comp == "Water") or (us == "Snake" and comp == "Gun")):
        print("Result: Player lose ❌ 😞 💔\n")
        computer_Score+=10
    elif((us =="Snake" and comp == "Snake") or (us == "Water" and comp == "Water") or (us == "Gun" and comp == "Gun")):
        print("Result: Draw 🤝\n")
    else:
        print("Invalid Case")

print("=======><=======")
print("Scoreboard")
print(f"Player      : {player_Score}")
print(f"computer    : {computer_Score}")
if(player_Score>computer_Score):
    print("Final Result: Player Wins")
elif(player_Score<computer_Score):
    print("Final Result: Computer Wins")
else:
    print("Final Result: Draw")
print("=====> Game End <=====")