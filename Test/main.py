print("How many cups of coffee would you like to buy?")
a = int(input())
if a >= 0:
    print(f"Ok! Also, you will get {a//6} cups of coffee as bonus")
else:
    print("Please, enter a valid number!!!")

