def main():
    character = str(input("Enter a character: "))
    print("The ASCII code for {} is {}".format(character, ord(character)))

    lower_limit = 33
    upper_limit = 127

    number = get_number(lower_limit, upper_limit)
    print("The character for {} is {}".format(number, chr(number)))

    for i in range(lower_limit, upper_limit + 1):
        print("{0:>5} {1:>5}".format(i, chr(i)))

    print("How many columns do you want to print?")
    upper_limit = lower_limit + int(input(">>>"))

    for i in range(lower_limit, upper_limit):
        print("{0:>5} {1:>5}".format(i, chr(i)))


def get_number(lower_limit, upper_limit):
    valid = False
    while valid == False:
        try:
            number = int(input("Enter a number between 33 to 127: "))
            if number < lower_limit or number > upper_limit:
                print("Invalid number; number is out of range")
            else:
                valid = True
        except ValueError:
            print("Invalid input; input is not an integer")
    return number

main()