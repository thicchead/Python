def main():
    # print(len("Metehan"))
    # tekst = "metehan"
    # print(tekst * 3)

    # print("Sammy ate {0:.2f}% of a pizza".format(75.741258))

    # s1 = "metehan"
    # s2 = "batuhan"
    #
    # for letter in s1:
    #     if letter in s2:
    #         print(letter)

    # name = "metehan"
    #
    # print(name[0:3])
    # print(name[1:4])
    # print(name[1:6:2])
    # print(name[4:])
    # print(name[-1::-1])

    # fruit = "aaldbei"
    # fruit = fruit[:2] + "r" + fruit[3:]
    #
    # print(fruit)
    #
    # tekst = "***" + "metehan" + "abc*"
    # tekst = tekst.strip("*")
    # print(tekst)

    # tekst = "metehana"
    # midden = len(tekst) // 2
    # print(tekst[:midden])

    # tekst = "hallo ik ben ben metehan"
    # eerste_ben = tekst.find("ben")
    # print(eerste_ben)
    # print(tekst.find("ben", eerste_ben + 1))
    # print(tekst.find("ben", 10, 20))

    # lyric = "Let it be, let it be, let it be, let it be"
    #
    # # lyric = lyric.lower()
    #
    # replaced = lyric.replace("let", "don't let", 3)
    #
    # print(replaced)

    # print(ord("a"))
    # print(chr(69))
    # print("mango" > "mangaan")

    # tekst = "metehan"
    # print(tekst[0:4])
    #
    # prijs = 912.31
    # prijs = prijs // 1
    # prijs = int(prijs)
    # print(prijs)
    # # prijs = prijs[::-1]
    # prijs = str(prijs)
    # prijs = prijs[::-1]
    # print(prijs)

    # tekst = "tekst"
    #
    # for letter in range(0, len(tekst)):
    #     uitkomst = ""
    #     veranderd = ord(letter) + ord(str(9))
    #     uitkomst += chr(veranderd)
    #
    # # print(uitkomst)
    #
    # tekst = "metehan"
    #
    # for letter in tekst:
    #     nieuw_letter = "a"
    #     print(nieuw_letter)

    letter = "A"

    for i in range(1, 6):
        letter = ord(letter) + 1
        print(chr(letter))


if __name__ == '__main__':
    main()
