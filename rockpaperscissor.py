import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_images = [rock, paper, scissors]
user_choice=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n"))
print(game_images[user_choice])
random_choice=random.randint(0,2)
print("Computer chose:")
print(game_images[random_choice])
if user_choice== 0 and random_choice== 1:
 print("computer win ")
elif user_choice== 0 and random_choice== 2:
 print("user win ")
elif user_choice== 1 and random_choice== 2:
 print("computer win ")
elif(user_choice==1and random_choice==0):
 print("user win ")
elif(user_choice==2and random_choice==0):
 print("computer win ")
elif(user_choice==2and random_choice==1):
 print("user win ")
elif (user_choice==random_choice):
 print("Draw")
