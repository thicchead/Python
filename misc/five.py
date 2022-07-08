# def machtverheffing(grondtal, exponent):
#     if exponent == 0:
#         resultaat = 1
#     else:
#         resultaat = grondtal ** exponent
#
#     return resultaat
#
#
# print(machtverheffing(5, 3))

# print(5.2 % 1)


# import math
#
#
# def main():
#     x = math.pow(5, 3)
#     y = math.sqrt(64)
#     print(x, y)
#
#
# if __name__ == '__main__':
#     main()

# from math import sqrt, pow
#
#
# def main():
#     x = sqrt(169)
#     y = pow(9, 4)
#     print(x, y)
#
#
# if __name__ == '__main__':
#     main()

# Random --> getal tussen 0 en 1
# Randint --> getal tussen bovengrens en ondergrens


# miljoenen = (3892754 // 1000000) * 1000000
# nodige = 3892754 - miljoenen
# print(nodige // 100000)

# nummer = 892754
# duizenden = nummer // 10000 * 10000
# print(duizenden)
# nummer -= duizenden
# print(nummer // 1000)

# nummer = 3892754
# miljoenen = (nummer // 1000000) * 1000000
# nummer -= miljoenen
# tweede_getal = nummer // 100000
#
# duizenden = (nummer // 10000) * 10000
# nummer -= duizenden
# vierde_getal = nummer // 1000
#
# # print(tweede_getal, vierde_getal)
# # print(nummer)
#
# honderden = nummer // 100 * 100
# # print(honderden)
# nummer -= honderden
# laatste_twee = nummer
# # print(nummer)
#
# print(tweede_getal, vierde_getal, laatste_twee)
#
# check_een = str(tweede_getal) + str(vierde_getal)
# print(check_een)
# if check_een != laatste_twee:
#     print("Yay")

