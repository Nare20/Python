# import random

# number_guess = random.randint(1,100)
# while True:
#     try:
#         guess = int(input("Guess the number between 1 and 100: "))

#         if guess < number_guess:
#             print("Too low")
#         elif guess > number_guess: 
#             print("Too high! ")
#         else: 
#             print("Congratulation you are guess!! ")
#             break
#     except ValueError:
#         print("please enter a valid number")

# #import random
# emojic = {'r':'🪨', 's':'✂️', 'p': '📄'}
# choices = ('r', 'p','s')
# while True:
#     choice = input("Rock, paper, or scissors? (r/p/s): ").lower()
#     if choice not in choices:
#         print('invalid choice!')
#         continue

#     computer_choice = random.choice(choices)

#     print(f' You chose {emojic[choice]} ')
#     print(f' Computer_choice {emojic[computer_choice]}')

#     if choice == computer_choice:
#         print('Tie!')
#     elif (
#         (choice == 'r' and computer_choice == 's') or 
#         (choice == 's' and computer_choice == 'p') or 
#         (choice == 'p' and computer_choice == 'r')):
#         print("you win" )
#      else:
#         print('you lose! ' )
#     ask_quetion = input('continue? (y/n):').lower()
#     if ask_quetion == 'n':
        

        

