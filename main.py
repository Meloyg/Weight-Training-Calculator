import datetime
import math
import data

def calculate_total_weight(exercises):
    return sum(weight * sets * reps for weight, sets, reps in exercises.values())

def calculate_total_weight_for_exercise(exercise):
    weight, sets, reps = exercise
    return weight * sets * reps

user_input = input("Enter your exercise: (chest, back): ").lower()

exercises = None

if user_input == "chest":
    exercises = data.chestData.chest_exercises
elif user_input == "back":
    exercises = data.backData.back_exercises
else:
    print("Invalid input")
    exit()

print(f"Starting {user_input} workout plan\n")

today = datetime.datetime.now()

for week in range(10):
    print(f"Week {week + 1} - {today.strftime('%d/%m/%Y')}")

    total_weight = sum(calculate_total_weight_for_exercise(exercise) for exercise in exercises.values())
    print(f"Total weight: {total_weight}kg")

    for exercise, details in exercises.items():
        total_weight = calculate_total_weight_for_exercise(details)
        print(f"Total weight for {exercise}: {total_weight}kg")
        print(f"The weight you should lift is about {total_weight/4/10}kg")

    print()
    
    # Increase weights for next week
    exercises = {exercise: (math.ceil(weight * 1.03), sets, reps) for exercise, (weight, sets, reps) in exercises.items()}
    today += datetime.timedelta(days=7)
