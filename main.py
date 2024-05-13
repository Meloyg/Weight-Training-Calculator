import datetime
import math

def calculate_total_weight(exercises):
    total_weight = sum([exercises[key][0] * exercises[key][1] * exercises[key][2] for key in exercises])
    return total_weight

def calculate_total_weight_for_exercise(exercises, exercise):
    weight, sets, reps = exercises[exercise]
    return weight * sets * reps


user_input = input("Enter your exercise: (chest, back): ").lower()

chest_exercises = {
    "bench press": (60, 4, 10),
    "chest fly": (50, 4, 12),
    "incline bench press": (60, 4, 10),
    "incline chest fly": (30, 4, 12),
    "lower chest press": (50, 4, 12),
    "tricep dips": (25, 4, 12),
}

back_exercises = {
    "wide grip pull": (55, 4, 10),
    "dumbbell rows": (46, 4, 12),
    "cable rows": (60, 4, 10),
    "close grip pull": (60, 4, 10),
    "pullovers": (30, 4, 12),
    "bicep curls": (25, 4, 10),
}

# Get today's date
today = datetime.datetime.now()


exercises = {}

if user_input == "chest":
    exercises = chest_exercises
elif user_input == "back":
    exercises = back_exercises
else:
    print("Invalid input")
    exit()

print(f"Starting {user_input} workout plan\n")

for week in range(10):
    print(f"Week {week + 1} - {today.strftime('%d/%m/%Y')}")
    
    for exercise, details in exercises.items():
        total_weight = calculate_total_weight_for_exercise(exercises, exercise)
        
        print(f"Total weight for {exercise}: {total_weight}kg")
    
    print(f"Total weight: {calculate_total_weight(exercises)}kg\n")
    
    # Increase weights for next week
    exercises = {exercise: (math.ceil(details[0] * 1.03), details[1], details[2]) for exercise, details in exercises.items()}
    today += datetime.timedelta(days=7)
