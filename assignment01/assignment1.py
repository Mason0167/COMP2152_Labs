# Author: Cheng-Yeh Tsai
# Assignment: #1

# Question b
gym_member = "Alex Alliton" # String
preferred_weight_kg = 20.5 # float
highest_reps = 25 # int
membership_active = True # Boolean

# Question c
# Dictionary: key = string (name), value = tuple of 3 integers (workout stats)
workout_stats = {
    "Alex": (30, 45, 20),
    "Jamie": (20, 30, 35),
    "Taylor": (55, 40, 50)
}

# Question d
workout_stats_total = {f"{k}_total": sum(v) for k, v in workout_stats.items()}

# Question e
row = 0
workout_list = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

# 2D List: the columns represent activities, the rows represent friends
for v in workout_stats.values():
    col = 0
    for i in v:
        workout_list[row][col] = i
        col += 1
    row += 1

# Question f
print("Yoga and Running:")
for v in workout_list:
    print(v[0:2])

print("\nWeight Lifting:")
for v in workout_list:
    print(v[2:3])

# Question g
for k, v in workout_stats.items():
    if (sum(v) >= 120):
        print(f"\nGreat job staying active, {k}!")

workout_stats = {
    "Alex": (30, 45, 20),
    "Jamie": (20, 30, 35),
    "Taylor": (55, 40, 50)
}


# Question h
name = input("\nEnter your friend name: ")
properName = name.title()
if properName == "Alex":
    print(
        f"{properName}'s workout time for each activity: {workout_stats[properName]}\n{properName}'s Total workout minutes: {sum(workout_stats[properName])}")
elif properName == "Jamie":
    print(
        f"{properName}'s workout time for each activity: {workout_stats[properName]}\n{properName}'s Total workout minutes: {sum(workout_stats[properName])}")
elif properName == "Taylor":
    print(
        f"{properName}'s workout time for each activity: {workout_stats[properName]}\n{properName}'s Total workout minutes: {sum(workout_stats[properName])}")
else:
    print(f"Friend <{properName}> not found in the records.")


# Question i
highestTotal = 0
value_lists = list(workout_stats_total.values())
lowestTotal = value_lists[0]
for k, v in workout_stats_total.items():
    if v > 0:
        highestTotalName = k
        highestTotal = v

    if v < lowestTotal:
        lowestTotalName = k
        lowestTotal = v

print(f"\n{highestTotalName.replace("_total", "")} has highest total workout minutes: {highestTotal}")
print(f"{lowestTotalName.replace("_total", "")} has lowest total workout minutes: {lowestTotal}")
