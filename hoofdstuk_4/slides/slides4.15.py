user_input = int(input("Getal = "))

while user_input % 5 != 0:
    user_input = int(input("Getal = "))
    if user_input % 2 == 0:
        print(user_input)

print("Einde")
