from operator import index


name=input('Please input a string e.g your name: ')
print(name)

for index, character in enumerate(name, start=1):
    print(character, index)
