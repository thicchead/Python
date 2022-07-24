def get_number_of_participants(res):
    print(len(res[0]))


def get_number_of_tests(res):
    print(len(res))


def highest_heart_rate(res):
    highest = 0

    for number in res:
        # print(number)
        # if number > highest:
        #     highest = number
        if max(number) > highest:
            highest = max(number)

    print(highest)


def lowest_heart_rate(res):
    lowest = 300

    for number in res:
        if min(number) < lowest:
            lowest = min(number)

    print(lowest)


def average_heart_rate(res):
    numbers = []
    total_test_1 = 0
    total_test_2 = 0
    total_test_3 = 0
    total_test_4 = 0

    for i in range(len(res)):
        # numbers = res[i]
        # print(numbers)
        for j in range(len(res[0])):
            actual_numbers = res[i][j]
            numbers.append(actual_numbers)
            # number_strings = str(actual_numbers)
            # total_test_1 = str(total_test_1)
            # total_test_1 += number_strings[0:5]
            # print(actual_numbers)
            # som += actual_numbers

    for i in range(6):
        total_test_1 += numbers[i]

    for i in range(6, 12):
        total_test_2 += numbers[i]

    for i in range(12, 18):
        total_test_3 += numbers[i]

    for i in range(18, 24):
        total_test_4 += numbers[i]

    # print(total_test_1)
    # print(total_test_2)
    # print(total_test_3)
    # print(total_test_4)

    average_test_1 = total_test_1 / len(res[0])
    print(average_test_1)

    average_test_2 = total_test_2 / len(res[1])
    print(average_test_2)

    average_test_3 = total_test_3 / len(res[2])
    print(average_test_3)

    average_test_4 = total_test_4 / len(res[3])
    print(average_test_4)

    # print("numbers = " + str(numbers))


def heart_rate_difference(res):
    results = []
    results_p_1 = []
    results_p_2 = []
    results_p_3 = []
    results_p_4 = []
    results_p_5 = []
    results_p_6 = []

    for i in range(len(res)):
        for j in range(len(res[0])):
            all_results = res[i][j]
            results.append(all_results)

    # for i in range(len(res[0])):
    #     for j in range(len(res)):
    #         print(res[i][j])
    # print(results)

    for i in range(0, 19, 6):
        results_p_1.append(results[i])
    # print(results_p_1)

    for i in range(1, 20, 6):
        results_p_2.append(results[i])
    # print(results_p_2)

    for i in range(2, 21, 6):
        results_p_3.append(results[i])

    for i in range(3, 22, 6):
        results_p_4.append(results[i])

    for i in range(4, 23, 6):
        results_p_5.append(results[i])

    for i in range(5, 24, 6):
        results_p_6.append(results[i])

    difference_1 = max(results_p_1) - min(results_p_1)
    print(difference_1)

    difference_2 = max(results_p_2) - min(results_p_2)
    print(difference_2)

    difference_3 = max(results_p_3) - min(results_p_3)
    print(difference_3)

    difference_4 = max(results_p_4) - min(results_p_4)
    print(difference_4)

    difference_5 = max(results_p_5) - min(results_p_5)
    print(difference_5)

    difference_6 = max(results_p_6) - min(results_p_6)
    print(difference_6)
    # print(results_p_1)
    # print("results = " + str(results))


def main():
    results = [[72, 75, 71, 73, 72, 76],
               [91, 90, 94, 93, 88, 91],
               [130, 135, 139, 142, 129, 138],
               [120, 118, 110, 105, 121, 119]]

    get_number_of_participants(results)
    get_number_of_tests(results)
    highest_heart_rate(results)
    lowest_heart_rate(results)
    average_heart_rate(results)
    heart_rate_difference(results)


if __name__ == '__main__':
    main()
