class NQueens:
    def __init__(self, n):
        self.n = n
        self.board = [[0] * n for _ in range(n)]
        self.row = [False] * n
        self.col = [False] * n
        self.diag1 = [False] * (2 * n - 1)
        self.diag2 = [False] * (2 * n - 1)
        self.solutions = []

    def solve(self):
        self.solve_helper(0)
        return self.solutions

    def solve_helper(self, col):
        if col == self.n:
            self.solutions.append([row[:] for row in self.board])
            return True

        for row in range(self.n):
            if self.is_valid(row, col):
                self.board[row][col] = 1
                self.row[row] = True
                self.col[col] = True
                self.diag1[row + col] = True
                self.diag2[row - col + self.n - 1] = True
                self.solve_helper(col + 1)
                self.board[row][col] = 0
                self.row[row] = False
                self.col[col] = False
                self.diag1[row + col] = False
                self.diag2[row - col + self.n - 1] = False

    def is_valid(self, row, col):
        return not self.row[row] and not self.col[col] and not self.diag1[row + col] and not self.diag2[row - col + self.n - 1]


n = 4
solver = NQueens(n)
solutions = solver.solve()

print(f"Found {len(solutions)} solutions for {n}-queens problem:")
for i, solution in enumerate(solutions):
    print(f"Solution {i + 1}:")
    for row in solution:
        print(row)
    print()

'''
This code solves the N-Queens problem using a backtracking algorithm. The N-Queens problem is the task of placing N chess queens on an N×N chessboard in such a way that no two queens threaten each other.

Here's an explanation of the code:

1. The `NQueens` class is defined to encapsulate the solving logic for the N-Queens problem. The constructor takes an integer `n` as input, which represents the size of the chessboard.

2. In the constructor, various instance variables are initialized to keep track of the state and solutions of the problem:
   - `self.board` is a 2D list representing the chessboard. Each element is initially set to 0.
   - `self.row`, `self.col`, `self.diag1`, and `self.diag2` are boolean lists used to mark whether a row, column, and two diagonals are occupied or not.
   - `self.solutions` is an empty list to store the found solutions.

3. The `solve` method is used to initiate the solving process. It calls the `solve_helper` method to recursively find all valid solutions.

4. The `solve_helper` method takes a parameter `col` that represents the current column being processed. It uses backtracking to explore different positions for the queen in each column.

5. The base case of the recursive `solve_helper` method is when `col` reaches the maximum number of columns (`self.n`). In this case, a valid solution has been found, and the current state of the chessboard is added to the `self.solutions` list.

6. Inside the `solve_helper` method, a loop iterates over each row in the current column. It checks if the current position is valid for placing a queen by calling the `is_valid` method.

7. If the position is valid, the queen is placed on the chessboard, and the state variables (`self.row`, `self.col`, `self.diag1`, `self.diag2`) are updated accordingly.

8. The `solve_helper` method then recurses to the next column by calling itself with `col + 1`.

9. After the recursive call returns, the queen is removed from the current position (backtracking), and the state variables are reset.

10. The `is_valid` method checks whether a given position is valid for placing a queen. It verifies that no other queen occupies the same row, column, and diagonals.

11. Finally, after the `solve` method is called to find all solutions, the code prints the number of solutions found and displays each solution by iterating over the `solutions` list.

The code essentially utilizes backtracking to systematically explore different configurations of queens on the chessboard. It finds all valid solutions to the N-Queens problem and displays them on the console.
'''