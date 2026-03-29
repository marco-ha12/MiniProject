import random

# List of exercises
exercises = [
    "10 Push-ups",
    "15 Sit-ups",
    "20 Squats",
    "30-second Plank",
    "15 Jumping Jacks",
    "10 Lunges (each leg)",
    "20 High Knees",
    "15 Burpees"
]

print("=== Quick Workout Generator ===")

while True:
    print("\nYour workout:")

    # Pick 3 random exercises
    workout = random.sample(exercises, 3)

    for exercise in workout:
        print("-", exercises)

    # Ask user if they want another workout
    again = input("\nGenerate another workout? (y/n): ").lower()

    if again != "y":
        print("Good job! Stay active 💪")
        break
