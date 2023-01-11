player_action = input("Enter a choice(rock, paper, scissors): ")
possible_actions = ["rock", "paper", "scissors"]
computer_action = random.choice(possible_actions)

if player_action == computer_action:
    print("Her iki oyuncuda {player_action} seçti. Berabere")
elif player_action == "rock":
    if computer_action == "scissors":
        print("Taş makası kırar! Kazandın!")
    else:
        print("Kağıt taşı  kaplar! Kaybettin")
elif player_action == "paper":
    if computer_action == "rock":
        print("Kağıt taşı kaplar! Kazandın!")
    else:
        print("Makas kağıdı keser! Kaybettin!")
elif player_action == "scissors":
    if computer_action == "rock":
        print("Taş makası kırar! Kaybettin")
    else: 
        print("Makas kağdı keser! Kazandın!") 

    play_again = input("Tekrar oynamak ister misiniz? (y/n): ")
    if play_again.lower() != "y":
        close 





