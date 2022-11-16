def greet():
    print(" ____________ ")
    print("  Приветики!  ")
    print("  Ты в игре   ")
    print("кресики-нолики")
    print(" ____________ ")
    print("вводи x и y (x- номер строки, у- номер столбца)")

def field():
    print()
    print("    ⎮ 0 ⎮ 1 ⎮ 2 ⎮")
    print("- - - - - - - - - ")
    for i, row in enumerate(base):
        row_str = f"  {i} ⎮ {' ⎮ '.join(row)} ⎮ "
        print(row_str)
        print("- - - - - - - - -")
    print()

def yourmove():
    while True:
        move = input("   Ходите: ").split()
        if len(move) != 2:
            print("Нужно ввести только две координаты")
            continue

        x, y = move
        if not(x.isdigit() or not(y.isdigit())):
            print("Нужно ввести только числа")
            continue
        x, y = int(x), int(y)
        if 0 > x or x > 2 or 0 > y or y > 2:
            print("в диапозоне нет столько координат")
            continue
        if base[x][y] != " ":
            print("Клетка занята")
            continue
        return x, y
def wincombi():
    wcomb = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
             ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
             ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for comb in wcomb:
        symbols = []
        for c in comb:
            symbols.append(base[c[0]][c[1]])
        if symbols == ["x", "x", "x"]:
            print("Выиграл Х")
            return True
        if symbols == ["0", "0", "0"]:
            print("Выиграл 0")
            return True
    return False

greet()
base = [[" "] * 3 for i in range(3)]
num = 0
while True:
    num += 1
    field()
    if num % 2 == 1:
        print("Ходит крестик")
    else:
        print("Ходити нолик")
    x, y = yourmove()
    if num % 2 == 1:
        base[x][y] = "x"
    else:
        base[x][y] = "0"
    if wincombi():
        break
    if num == 9:
        print("ничья")
        break
