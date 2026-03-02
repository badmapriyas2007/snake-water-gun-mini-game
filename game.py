import random

# List of choices
choices = ["snake", "water", "gun"]

# Initialize scores
user_score = 0
computer_score = 0

print("Welcome to Snake Water Gun Game")
print("--------------------------------")

# Safe input for rounds
try:
    rounds = int(input())
    if rounds <= 0:
        rounds = 3
except:
    rounds = 3   # Default rounds if no input

for i in range(rounds):
    
    # Safe user input
    try:
        user_choice = input().lower().strip()
    except:
        user_choice = random.choice(choices)

    if user_choice not in choices:
        user_choice = random.choice(choices)

    computer_choice = random.choice(choices)

    # Game logic
    if user_choice == computer_choice:
        pass
    elif (user_choice == "snake" and computer_choice == "water") or \
         (user_choice == "water" and computer_choice == "gun") or \
         (user_choice == "gun" and computer_choice == "snake"):
        user_score += 1
    else:
        computer_score += 1

# Print final score
print(user_score, computer_score)

if user_score > computer_score:
    print("You won the game!")
elif computer_score > user_score:
    print("Computer won the game!")
else:
    print("The game is a Draw!")