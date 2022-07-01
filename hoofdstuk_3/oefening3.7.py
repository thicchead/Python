eerste_resultaat = int(input("Res 1 = "))
tweede_resultaat = int(input("Res 2 = "))
derde_resultaat = int(input("Res 3 = "))

gemiddelde = (eerste_resultaat + tweede_resultaat + derde_resultaat) * 1.6666666666
print(gemiddelde)

if gemiddelde < 60:
    print("Onvoldoende")
elif gemiddelde < 70:
    print("Voldoende")
elif gemiddelde < 80:
    print("Onderscheiding")
elif gemiddelde < 90:
    print("Grote onderscheiding")
else:
    print("Grootste onderscheiding")

