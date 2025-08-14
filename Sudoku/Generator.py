import random
from Solver import solve

class Generator:
    def __init__(self, size=9, subgrid_size=3):
        self.size = size
        self.subgrid_size = subgrid_size
        self.board = [[0] * size for _ in range(size)]

    def fill_diagonal(self):
        for i in range(0, self.size, self.subgrid_size):
            self.fill_subgrid(i, i)

    def fill_subgrid(self, row, col):
        nums = list(range(1, self.size + 1))
        random.shuffle(nums)
        for i in range(self.subgrid_size):
            for j in range(self.subgrid_size):
                self.board[row + i][col + j] = nums.pop()

    def remove_numbers(self, attempts=40):
        count = attempts
        while count > 0:
            row, col = random.randint(0, self.size - 1), random.randint(0, self.size - 1)
            while self.board[row][col] == 0:
                row, col = random.randint(0, self.size - 1), random.randint(0, self.size - 1)
            
            backup = self.board[row][col]
            self.board[row][col] = 0
            board_copy = [row[:] for row in self.board]

            if not self.has_unique_solution(board_copy):
                self.board[row][col] = backup
                count -= 1

    def has_unique_solution(self, board):
        return solve(board)

    def generate_sudoku(self):
        self.fill_diagonal()
        solve(self.board)
        self.remove_numbers()
        return self.board

if __name__ == "__main__":
    generator = Generator()
    sudoku_board = generator.generate_sudoku()
    
    from Sudoku import Grid
    import pygame

    pygame.init()
    win = pygame.display.set_mode((540, 600))
    pygame.display.set_caption("Sudoku")
    board = Grid(9, 9, 540, 540, win)
    board.board = sudoku_board
    board.update_model()
    
    while True:
        pygame.event.pump()
        board.draw()
        pygame.display.update()
