"""
Author: <Eseosa Eweka>
Assignment: #1
"""


# Step b: Create 4 variables
gym_member = "Alex Alliton"            # str
preferred_weight_kg = 20.5             # float
highest_reps = 25                      # int
membership_active = True               # bool


# Step c: Dictionary storing workout data (dict: str -> tuple[int, int, int])
workout_stats = {
    "Alex": (30, 45, 20),     # yoga, running, weightlifting
    "Jamie": (25, 35, 40),
    "Taylor": (20, 30, 50)
}


# Step d: Calculate total workout minutes and add new key-value pairs
for friend, workouts in list(workout_stats.items()):
    total_minutes = sum(workouts)
    workout_stats[f"{friend}_Total"] = total_minutes


# Step e: Create a 2D nested list (list[list[int]])
workout_list = [
    list(workout_stats["Alex"]),
    list(workout_stats["Jamie"]),
    list(workout_stats["Taylor"])
]


# Step f: Slice the workout_list

# Yoga and running for all friends
print("Yoga and Running minutes:")
for row in workout_list:
    print(row[:2])

# Weightlifting for the last two friends
print("\nWeightlifting minutes for last two friends:")
for row in workout_list[1:]:
    print(row[2])


# Step g: Check if any friend's total >= 120
for friend in ["Alex", "Jamie", "Taylor"]:
    if workout_stats[f"{friend}_Total"] >= 120:
        print(f"Great job staying active, {friend}!")


# Step h: User input lookup
name = input("\nEnter a friend's name: ").capitalize()

if name in workout_stats:
    yoga, running, lifting = workout_stats[name]
    total = workout_stats[f"{name}_Total"]
    print(f"\n{name}'s workout minutes:")
    print(f"Yoga: {yoga}")
    print(f"Running: {running}")
    print(f"Weightlifting: {lifting}")
    print(f"Total: {total}")
else:
    print(f"Friend {name} not found in the records.")


# Step i: Friend with highest and lowest total workout minutes
totals = {
    friend: workout_stats[f"{friend}_Total"]
    for friend in ["Alex", "Jamie", "Taylor"]
}

highest = max(totals, key=totals.get)
lowest = min(totals, key=totals.get)

print(f"\nHighest total workout minutes: {highest}")
print(f"Lowest total workout minutes: {lowest}")
