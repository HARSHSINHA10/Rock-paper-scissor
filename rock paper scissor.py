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
elements = [rock, paper, scissors]
#Write your code below this line 👇
import random
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
comp_choice = random.randint(0,2)
if user_choice > 2:
    print("You typed an invalid number, you lose!")
    
else:
 print ("You chose:\n " + elements[user_choice])
 print ("Computer chose:\n "+ elements[comp_choice]) 
if user_choice == comp_choice:
    print("Game draw")
if user_choice == 0 and comp_choice == 1:
    print("You lose")
if user_choice == 0 and comp_choice == 2:
    print("You win")
if user_choice == 1 and comp_choice == 0:
    print("You win")
if user_choice == 1 and comp_choice == 2:
    print("You lose")
if user_choice == 2 and comp_choice == 0:
    print("You lose")
if user_choice == 2 and comp_choice == 1:
    print("You win")