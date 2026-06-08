import random
choices = ('r','s','p')

user_choice = input("Rock, paper, or scissors? (r/p/s): ").lower()
while True:
    if user_choice not in  choices:
        print("Invalid choice !")
        continue
    computer_choice = random.choice(choices)
    # break
    print('your choce', user_choice)
    print('computer choice' ,computer_choice)
    break
file = open("shopping.txt")
contents = file.read()
# file.close()
print(contents)