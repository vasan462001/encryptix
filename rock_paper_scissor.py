import random
def g_computer_choice():
    return random.choice(['rock','paper','scissors'])

def determine_winner(user_choice,computer_choice):
    if user_choice== computer_choice:
        return "it is a tie"
    elif (user_choice=="rock" and computer_choice=='scissors') or (user_choice=='scissors' and computer_choice=='paper') or (user_choice=='paper' and computer_choice=='rock'):
        return 'you win!'
    else:
        return 'oops! you lose'
    

def main():
        user_score=0
        computer_score=0
        rounds=1

        print("welcome to rock paper scisors game")
        print("choose rock , paper , scissors and type 'exit' to quite")

        while True:
            user_choice=input(f"Round {rounds}: your choice:").lower()
             
            if user_choice=='exit':
                print("thank you for your play")
                break

            if user_choice not in ['rock','paper','scissors']:
                print("give only game rules")
                continue

            computer_choice=g_computer_choice()
            print(f"computer choice",{computer_choice})
            result=determine_winner(user_choice,computer_choice)
            print(result)

            if "win" in result:
                user_score+=1
            elif "lose" in result:
                computer_score+=1
            print(f"score - you:{user_score},computer_score:{computer_score}")
            rounds+=1

            play_again=input("do you wnat to play again? (yes / no):").lower()
            if play_again=="no":
                print("thank you for playing")
                break

if __name__=="__main__":
    main()




