"""Ong Zhen Hui"""
name = input("Enter your name: ")

while name == "":
    print("No input received")
    name = input("Enter your name: ")

print(name[::2])