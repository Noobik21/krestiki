board = [[" " for _ in range(3)] for _ in range(3)]
def print_board():
    for row in board:
        print(" | ".join(row))
        print("-" * 10)

def check_winner(player):
    # Проверяем строки, столбцы и диагонали
    for i in range(3):
        if all(board[i][j] == player for j in range(3)):  # строка
            return True
        if all(board[j][i] == player for j in range(3)):  # столбец
            return True
    if all(board[i][i] == player for i in range(3)):  # главная диагональ
        return True
    if all(board[i][2 - i] == player for i in range(3)):  # побочная диагональ
        return True
    return False


player = "X"

for _ in range(9):  # максимум 9 ходов
    print_board()
    print(f"Ход игрока {player}")

    row = int(input("Введите номер строки (0, 1, 2): "))
    col = int(input("Введите номер столбца (0, 1, 2): "))

    if board[row][col] != " ":
        print(" Клетка занята! Попробуйте снова.")
        continue

    board[row][col] = player

    if check_winner(player):
        print_board()
        print(f"Победил игрок {player}!")
        break

    # Смена игрока
    player = "O" if player == "X" else "X"
else:
    print_board()
    print("Ничья!")