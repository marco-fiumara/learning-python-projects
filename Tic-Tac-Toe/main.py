matrix = []

for i in range(3):
    matrix.append([])
    for j in range(3):
        matrix[i].append("_")


def print_field():
    print(f'''---------
| {matrix[0][0]} {matrix[0][1]} {matrix[0][2]} |
| {matrix[1][0]} {matrix[1][1]} {matrix[1][2]} |
| {matrix[2][0]} {matrix[2][1]} {matrix[2][2]} |
---------''')


def winner_check():
    # Row check
    for i in range(3):
        if matrix[i][0] != "_" and matrix[i][0] == matrix[i][1] == matrix[i][2]:
            print(f"{matrix[i][0]} wins")
            return "Win"
    # Column check
    for row in range(1):
        for num in range(3):
            if matrix[row][num] != "_" and matrix[row][num] == matrix[row + 1][num] == matrix[row + 2][num]:
                print(f"{matrix[row][num]} wins")
                return "Win"
    # Diagonal check
    if matrix[1][1] != "_" and ((matrix[0][0] == matrix[1][1] == matrix[2][2]) or (matrix[0][2] == matrix[1][1] == matrix[2][0])):
        print(f"{matrix[1][1]} wins")
        return "Win"
    # Draw check
    total = 0
    for k in range(0, 3, 1):
        if "_" not in matrix[k]:
            total += 1
            print(total)
            if total == 3:
                print("Draw")
                return "Draw"
    # Game still playing
    else:
        return "Continue"


print_field()

playing = True
turn = 0

while playing:
    x = input('Enter the coordinates: ').split()
    if x[0] not in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']:
        print('You should enter numbers!')
        continue
    x, y = int(x[0]), int(x[1])
    if x not in range(4) or y not in range(4):
        print('Coordinates should be from 1 to 3!')
    elif matrix[abs(y - 3)][x - 1] != '_':
        print('This cell is occupied! Choose another one!')
    else:
        if turn % 2 == 0:
            matrix[abs(y - 3)][x - 1] = 'X'
            turn += 1
            print_field()
            result = winner_check()
            if result == "Draw" or result == "Win":
                playing = False
            else:
                continue
        else:
            matrix[abs(y - 3)][x - 1] = 'O'
            turn += 1
            print_field()
            result = winner_check()
            if result == "Draw" or result == "Win":
                playing = False
            else:
                continue
