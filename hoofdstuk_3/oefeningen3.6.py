BASISPRIJS = 5
HUIDIG_JAAR = 2022

jaar = int(input("Jaar = "))
rating = int(input("Rating = "))

if rating == 4 or rating == 5:
    BASISPRIJS += 2
elif HUIDIG_JAAR - jaar <= 2 or rating == 3 or rating == 2:
    BASISPRIJS += 1

print(BASISPRIJS)
