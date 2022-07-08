def get_tienden(getal):
    kommagetal = getal % 1
    tiende_op_eerste_plaats = kommagetal * 10
    resultaat = tiende_op_eerste_plaats // 1

    return int(resultaat)


print(get_tienden(24.1186))
