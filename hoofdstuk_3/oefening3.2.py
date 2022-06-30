brutoloon = float(input("Brutoloon = "))

vakantiegeld = brutoloon * 0.05
jaarlijkse_bijdrage = 0

if vakantiegeld > 350:
    jaarlijkse_bijdrage = 0.08 * 350
else:
    jaarlijkse_bijdrage = 0.08 * vakantiegeld

print("Brutoloon = " + str(brutoloon))
print("Vakantiegeld = " + str(vakantiegeld))
print("Jaarlijkse bijdrage = " + str(jaarlijkse_bijdrage))
