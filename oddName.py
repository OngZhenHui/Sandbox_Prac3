"""Ong Zhen Hui"""
def main():
    name = get_name()
    frequency = int(input("Determine the frequency: "))
    print_name(name, frequency)


def print_name(name, frequency):
    print(name[::frequency])


def get_name():
    name = input("Enter your name: ")
    while name == "":
        print("No input received")
        name = input("Enter your name: ")
    return name


main()