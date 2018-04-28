"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

# TODO: Fix this!
def main():
    score = get_score()

    if score < 0 or score > 100:
        print("Invalid score")
    elif score >= 90:
        print("Excellent!")
    elif 50 <= score < 90:
        print("Passable")
    else:
        print("Bad")


def get_score():
    score = float(input("Enter score: "))
    return score


main()