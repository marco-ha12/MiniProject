import random

# Exercise lists by difficulty
easy = [
    "5 Push-ups",
    "10 Sit-ups",
    "10 Squats",
    "20-second Plank"
]

medium = [
    "10 Push-ups",
    "15 Sit-ups",
    "20 Squats",
    "30-second Plank",
    "15 Jumping Jacks"
]

hard = [
    "20 Push-ups",
    "25 Sit-ups",
    "30 Squats",
    "1-minute Plank",
    "20 Burpees",
    "20 Lunges (each leg)"
]

print("=== Quick Workout Generator ===")

while True:
    # Get valid difficulty input
    while True:
        level = input("\nChoose difficulty (easy / medium / hard): ").lower()
        
        if level == "easy":
            chosen_list = easy
            break
        elif level == "medium":
            chosen_list = medium
            break
        elif level == "hard":
            chosen_list = hard
            break
        else:
            print("Invalid choice. Please enter easy, medium, or hard.")

    # Generate workout
    workout = random.sample(chosen_list, 3)

    print("\nYour workout:")
    for exercise in workout:
        print("-", exercise)


# Ask to repeat
    while True:
        again = input("\nGenerate another workout? (yes/no): ").lower()
    
        if again == "yes":
            break   # go back to main loop (generate again)
        elif again == "no":
            print("Good job! Stay active 💪")
            exit()  # end program
        else:
            print("Invalid input, please type yes or no.")
