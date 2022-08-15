print("Tell me, how many chickens do you have on your farm?")
chickens = int(input())
print("Tell me, how many cows do you have on your farm?")
cows = int(input())
print("Tell me, how many pigs do you have on your farm?")
pigs = int(input())
if chickens >= 0 and cows >= 0 and pigs >= 0:
    print(f"The animals on your farm have {chickens * 2 + ((cows*4) + (pigs*4))} paws!")
else:
    print("Please, enter valid numbers")