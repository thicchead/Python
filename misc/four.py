# for letter in "banaan":
#     print(letter)

# for i in "metehan karakoruk":
#     print(i, end="")
#
# print()

# for i in "python":
#     print(i)
#     print(i, end="")

# fruit = "banaan"
# for letter in fruit:
#     print(letter)
# print("Klaar")

# fruit = "banaan"
# for letter in fruit:
#     print(letter)
#     if letter == "n":
#         fruit = "mango"
# print("Klaar")  --> laat zien dat in een for loop uw variabele niet gewijzigd kan worden

# for x in (10, 100, 1000, 10000):
#     print(x)
#
# for x in (2, " appels", " en ", 1, " peer "):
#     print(x, end="")

# a = 2
# while a < 5:
#     print(a)
#     a += 1
#     --> while True  = voer uit

for i in range(1, 6):
    for j in range(1, i + 1):
        print("x", end=" ")
    print(" ")
