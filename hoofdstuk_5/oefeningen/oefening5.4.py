from random import randint


def calculate_response(answer, guess):
    if guess > answer:
        return "Too high"
    elif guess < answer:
        return "Too low"
    else:
        return "Exactly!"


def main():
    number = randint(1, 10)
    user_guess = int(input("Your guess = "))
    turns = 0

    while turns < 3:
        reply = calculate_response(number, user_guess)
        print(reply)

        if reply == "Exactly":
            turns += 4
        else:
            turns += 1
            user_guess = int(input("Your guess = "))


if __name__ == '__main__':
    main()
