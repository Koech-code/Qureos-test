name=input('Please input a string e.g your name: ')
print(name)

for position, character in enumerate(name, start=1):
    print(character, position)
