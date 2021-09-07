# Крестики-нолики
# Компьютер играет против человека
   
# Глобальные переменные
X = "X"
O = "O"
EMPTY = " "
TIE = "TIE"
NUM_SQUARES = 9


def display_instruct():
    """Вывод инструкций к игре."""
    print(
    """
    Добро пожаловать в величайший интеллектуальное противостояние всех времен: Крестики-Нолики.
    Это будет битва между вашим человеческим мозгом и моим кремниевым процессором.  

    Сделаете свой ход, введя число от 0 до 8. 
    Число будет соответствовать положению ячейки, как показано на рисунке:
    
                    0 | 1 | 2
                    ---------
                    3 | 4 | 5
                    ---------
                    6 | 7 | 8

    Приготовься к сражению, человек. Великая битва вот-вот начнется.. \n
    """
    )


def ask_yes_no(question):
    """Ответ на вопрос "да" или "нет"."""
    response = None
    while response not in ("y", "n"):
        response = input(question).lower()
    return response


def ask_number(question, low, high):
    """Спросите номер в диапазоне."""
    response = None
    while response not in range(low, high):
        response = int(input(question))
    return response


def pieces():
    """Определите, кто ходит первым игрок или компьютер."""
    go_first = ask_yes_no("Будешь ходить превым, кожанный мешок? (y/n): ")
    if go_first == "y":
        print("\nТогда сделайте первый ход. Тебе это понадобится.")
        human = X
        computer = O
    else:
        print("\nТвоя храбрость погубит тебя ... Я пойду первым.")
        computer = X
        human = O
    return computer, human


def new_board():
    """Создание новой игровой доски."""
    board = []
    for square in range(NUM_SQUARES):
        board.append(EMPTY)
    return board


def display_board(board):
    """Вывод игрового поля на экран."""
    print("\n\t", board[0], "|", board[1], "|", board[2])
    print("\t", "---------")
    print("\t", board[3], "|", board[4], "|", board[5])
    print("\t", "---------")
    print("\t", board[6], "|", board[7], "|", board[8], "\n")


def legal_moves(board):
    """Составления списка возможных ходов."""
    moves = []
    for square in range(NUM_SQUARES):
        if board[square] == EMPTY:
            moves.append(square)
    return moves


def winner(board):
    """Определение победителя игры."""
    WAYS_TO_WIN = ((0, 1, 2),
                   (3, 4, 5),
                   (6, 7, 8),
                   (0, 3, 6),
                   (1, 4, 7),
                   (2, 5, 8),
                   (0, 4, 8),
                   (2, 4, 6))
    
    for row in WAYS_TO_WIN:
        if board[row[0]] == board[row[1]] == board[row[2]] != EMPTY:
            winner = board[row[0]]
            return winner

    if EMPTY not in board:
        return TIE

    return None


def human_move(board, human):
    """Ввод человеческого хода."""
    legal = legal_moves(board)
    move = None
    while move not in legal:
        move = ask_number("Куда ты ходишь? (0-8):", 0, NUM_SQUARES)
        if move not in legal:
            print("\nЭта клетка уже занята, глупый человек. Выбери другую.\n")
    print("Отлично...")
    return move


def computer_move(board, computer, human):
    """Ход компьютера."""
    # make a copy to work with since function will be changing list
    board = board[:]
    # the best positions to have, in order
    BEST_MOVES = (4, 0, 2, 6, 8, 1, 3, 5, 7)

    print("I shall take square number", end=" ")
    
    # если компьютер может победить, сделай этот ход
    for move in legal_moves(board):
        board[move] = computer
        if winner(board) == computer:
            print(move)
            return move
        # закончили проверку этого хода, отмените его
        board[move] = EMPTY
    
    # Если человек может победить, заблокируйте этот ход
    for move in legal_moves(board):
        board[move] = human
        if winner(board) == human:
            print(move)
            return move
        # сделал отметку в этом ходу, отмени его
        board[move] = EMPTY

    # так как никто не может выиграть на следующем ходу, выберите лучший открытый квадрат
    for move in BEST_MOVES:
        if move in legal_moves(board):
            print(move)
            return move


def next_turn(turn):
    """Switch turns."""
    if turn == X:
        return O
    else:
        return X

    
def congrat_winner(the_winner, computer, human):
    """Поздравить победителя."""
    if the_winner != TIE:
        print(the_winner, "Выйграл!\n")
    else:
        print("Это галстук!\n")

    if the_winner == computer:
        print("Как я и предсказывал, человек, я снова торжествую.  \n" \
              "Доказательство того, что компьютеры превосходят людей во всех отношениях.")

    elif the_winner == human:
        print("Нет нет! Этого не может быть! Как-то ты обманул меня, человек. \n" \
              "Ты больше никогда не победишь! Я, компьютер, клянусь!")

    elif the_winner == TIE:
        print("Тебе очень повезло, человек, и ты каким-то образом сумел сыграть в ничью.  \n" \
              "Отпразднуйте сегодня ... это лучшее, чего ты когда-либо достиг.")


def main():
    display_instruct()
    computer, human = pieces()
    turn = X
    board = new_board()
    display_board(board)

    while not winner(board):
        if turn == human:
            move = human_move(board, human)
            board[move] = human
        else:
            move = computer_move(board, computer, human)
            board[move] = computer
        display_board(board)
        turn = next_turn(turn)

    the_winner = winner(board)
    congrat_winner(the_winner, computer, human)


# start the program
main()
input("\n\nНажмите клавишу ENTER, чтобы выйти.")
