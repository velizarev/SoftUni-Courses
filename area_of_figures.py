from math import pi

figure = input()

if figure == "square":
    length = float(input())
    result = length * length # формула за намиране лице на квадрат
    print(f"{result:.3f}")

elif figure == "rectangle":
    length = float(input())
    length1 = float(input())
    result = length * length1
    print(f"{result:.3f}")

elif figure == "circle":
    length = float(input())
    result = pi * (length ** 2) # формула за намиране на лице на кръг лицето = пи * (страната на 2 ра степен)
    print(f"{result:.3f}")

elif figure == "triangle":
    lenght = float(input())
    height = float(input())
    result = (lenght * height) / 2 # формула за лице на триъгърник
    print(f'{result:.3f}')