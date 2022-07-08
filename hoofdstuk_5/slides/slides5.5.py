def is_even(getal):
    if getal % 2 == 0:
        return True


def is_oneven(getal):
    if getal % 2 != 0:
        return not is_even(getal)


print(is_even(7))