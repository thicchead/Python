def main():
    keuze = int(input("Uw stemcode = "))
    student_1_aantal = 0
    student_2_aantal = 0
    student_3_aantal = 0
    student_4_aantal = 0
    student_1 = []
    student_2 = []
    student_3 = []
    student_4 = []

    while keuze != 0:
        if keuze == 1:
            student_1.append(keuze)
        elif keuze == 2:
            student_2.append(keuze)
        elif keuze == 3:
            student_3.append(keuze)
        else:
            student_4.append(keuze)

        student_1_aantal = student_1.count(2)
        student_2_aantal = student_2.count(2)
        student_3_aantal = student_3.count(3)
        student_4_aantal = student_4.count(4)

        keuze = int(input("Uw stemcode = "))

    # print(student_1)

    print(student_1_aantal)
    print(student_2_aantal)
    print(student_3_aantal)
    print(student_4_aantal)


if __name__ == '__main__':
    main()
