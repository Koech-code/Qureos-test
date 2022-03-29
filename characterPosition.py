from operator import index
from turtle import position


name=input('Please input a string e.g your name: ')
print(name)

for position, character in enumerate(name, start=1):
    print(character, position)
