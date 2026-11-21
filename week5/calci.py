import random


def main():
    score = 0
    level = get_level()
    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        attempt = 0

        while attempt < 3:
            try:
                uinput = int(input(f"{x} + {y} = "))
                if uinput == x + y:
                    score += 1
                    break
                else:
                    print("EEE")
                    attempt += 1
            except ValueError:
                print("EEE")
                attempt += 1

        if attempt == 3:
            print(f"{x} + {y} = {x + y}")

    print(f"Score: {score}")


def get_level():
    while True:
        try:
            input1 = int(input("Level: "))
            if input1 in [1,2,3]:
                return input1
        except ValueError:
            pass


def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)
    else:
        raise ValueError


if __name__ == "__main__":
    main()
