print("Enter value of minutes!")
minutes = int(input())

if 0 <= minutes <= 15:
    print(f"{minutes} lays in the first quarter!")
elif 16 <= minutes <= 30:
    print(f"{minutes} lays in the second quarter!")
elif 31 <= minutes <= 45:
    print(f"{minutes} lays in the third quarter!")
elif 46 <= minutes <= 60:
    print(f"{minutes} lays in the fourth quarter!")
elif minutes > 60:
    if 0 <= minutes % 60 <= 15:
        print(f"{minutes} lays in the first quarter!")
    elif 16 <= minutes % 60 <= 30:
        print(f"{minutes} lays in the second quarter!")
    elif 31 <= minutes % 60  <= 45:
        print(f"{minutes} lays in the third quarter!")
    elif 46 <= minutes % 60 <= 60:
        print(f"{minutes} lays in the fourth quarter!")
else:
    print("Warning! Enter a valid number!")

# 1 чверть це 0-15 хвилин, 61-75  хвилин, 121-135 хвилин
# 2 чверть це 16-30 хвилин, 76-90 хвилин, 136-150 хвилин
# 3 чверть це 31-45 хвилин, 91-105 хвилин, 151-165 хвилин
# 4 чверть це 46-60 хвилин, 106-120 хвилин, 166-180 хвилин
