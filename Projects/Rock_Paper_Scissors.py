import random 

x = ("rock","paper","scissor")

computer = random.choice(x)
player = None
while player not in x :
  player = input("Enter a choice (rock,paper,scissor) : ") 


print(f"player :{player}")
print(f"computer :{computer}")

if player == computer:
  print("OOps its a tie")
elif player == "rock" and computer == "scissor":
  print("You Won :)")
elif player == "scissor" and computer == "paper":
  print("You Won :)")
elif player == "paper" and computer == "rock":
  print("You Won :)")
else:
  print("Sorry but you lose :(")

# Output
'''
Enter a choice (rock,paper,scissor) : rock
player :rock
computer :paper
Sorry but you lose :(
'''
