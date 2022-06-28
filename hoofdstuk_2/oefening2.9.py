bedrag = int(input("Aantal centen = "))

twee_euro = bedrag // 200
bedrag %= 200

een_euro = bedrag // 100
bedrag %= 100

vijftig_cent = bedrag // 50
bedrag %= 50

twintig_cent = bedrag // 20
bedrag %= 20

tien_cent = bedrag // 10
bedrag %= 10

vijf_cent = bedrag // 5
bedrag %= 5

twee_cent = bedrag // 2
bedrag %= 2

een_cent = bedrag // 1

print(twee_euro)
print(een_euro)
print(vijftig_cent)
print(twintig_cent)
print(tien_cent)
print(vijf_cent)
print(twee_cent)
print(een_cent)
