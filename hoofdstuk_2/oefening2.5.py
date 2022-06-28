graden_fahrenheit = float(input("Graden Fahrenheit = "))

graden_celsius = (graden_fahrenheit - 32) / (9 / 5)
print("Graden Celsius = " + str(graden_celsius))

afgeronde_celsius = (graden_celsius * 10 + 0.5) // 1 / 10
print(afgeronde_celsius)
