import random
def display(board):
    for i in range(9):
        for j in range(9):
            print(board[i][j], end=" ")
        print()
def isvalid(board, row, col, num):
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False
    startr, startc = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[startr + i][startc + j] == num:
                return False
    return True
def solve(board):
    empty = find_empty(board)
    if not empty:
        return True
    row, col = empty
    for num in range(1, 10):
        if isvalid(board, row, col, num):
            board[row][col] = num
            if solve(board):
                return True 
            board[row][col] = 0
    return False
def find_empty(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i, j)
    return None
def generate(difficulty):
    board = [[0] * 9 for _ in range(9)]
    solve(board)
    num_to_remove = 0
    if difficulty == 'easy':
        num_to_remove = 30
    elif difficulty == 'medium':
        num_to_remove = 40
    elif difficulty == 'hard':
        num_to_remove = 50
    while num_to_remove > 0:
        row, col = random.randint(0, 8), random.randint(0, 8)
        if board[row][col] != 0:
            board[row][col] = 0
            num_to_remove -= 1

    return board

if __name__ == "__main__":
    difficulty = input("Enter difficulty level (easy, medium, hard): ").lower()

    if difficulty not in ['easy', 'medium', 'hard']:
        print("Invalid difficulty level. Please enter 'easy', 'medium', or 'hard'.")
    else:
        sudoku = generate(difficulty)
        print("\nGenerated Sudoku Puzzle:")
        display(sudoku)
        original = [row[:] for row in sudoku]
        print("\nEnter your solution:")
        for i in range(9):
            for j in range(9):
                sudoku[i][j] = int(input(f"Enter value for cell ({i+1}, {j+1}): "))
        if sudoku == original:
            print("Congratulations! Your solution is correct.")
        else:
            print("Sorry, your solution is incorrect. Here is the correct solution:")
            display(original)