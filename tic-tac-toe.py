def hi():
    print(" Добро пожаловать ")
    print(" -----в игру----- ")
    print(" Крестики--нолики ")
    print(" ---------------- ")

field = [[" ", " " ," "] for j in range(3)]

def playing_field():
    print(f" 0 1 2")
    for j in range(3):
        print(f"{j} {field[j][0]} {field[j][1]} {field[j][2]}")

def game():
    while True:
        x, y = map(int, input("Время вашего хода: ").split())
        if 0 <= x <= 2 and 0 <= y <= 2:
            if field[x][y] == " ":
                return x, y
            else:
                print("Выбранная клетка занята")
        else:
            print("Выбранные координаты вне диапазона игры")

def win():
    cord_of_win = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                   ((0, 0), (1, 0), (2, 0)), ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)),
                   ((0, 0), (1, 1), (2, 2)), ((0, 2), (1, 1), (2, 0)))
    for cords in cord_of_win:
        combination = []
        for i in cords:
            combination.append(field[i[0]][i[1]])
        if combination == ["X", "X", "X"]:
            print("Выйграл крестик!")
            return True
        if combination == ["0", "0", "0"]:
            print("Выйграл нолик!")
            return True
    return False

hi()
move = 0
while True:
    move += 1

    playing_field()

    if move % 2 == 1:
        print("Ход крестика")
    else:
        print("Ход нолика")

    x, y = game()

    if move % 2 == 1:
        field[x][y] = "X"
    else:
        field[x][y] = "0"

    if win():
        break

    if move == 9:
        print("В игре нет победителя")
        break