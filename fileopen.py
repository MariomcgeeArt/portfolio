from random import randint, choice

my_file = open("words.txt", "r")
lines = my_file.readlines()
print(lines)

x = randint(0, len(lines)-1)
print(lines{})