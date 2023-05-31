## PRACTICAL NO: 04
## N-Queens Problem
N = 4
ld = [0] * 30
rd = [0] * 30
cl = [0] * 30

def printSolution(board):
	for i in range(N):
		for j in range(N):
			print(board[i][j], end = " ")
		print()

def solveNQUtil(board, col):
	
	if (col >= N):
		return True
		
	for i in range(N):
		
		if ((ld[i - col + N - 1] != 1 and
			rd[i + col] != 1) and cl[i] != 1):
				
			board[i][col] = 1
			ld[i - col + N - 1] = rd[i + col] = cl[i] = 1
			
			if (solveNQUtil(board, col + 1)):
				return True
				
			board[i][col] = 0 # BACKTRACK
			ld[i - col + N - 1] = rd[i + col] = cl[i] = 0
			
		    
	return False
	
def solveNQ():
	board = [[0, 0, 0, 0],
			[0, 0, 0, 0],
			[0, 0, 0, 0],
			[0, 0, 0, 0]]
	if (solveNQUtil(board, 0) == False):
		printf("Solution does not exist")
		return False
	printSolution(board)
	return True

solveNQ()

'''
This code solves the N-Queens problem using backtracking. The N-Queens problem is a classic puzzle where you have to place N queens on an N x N chessboard in such a way that no two queens threaten each other.

Here's a step-by-step explanation of the code:

1. The code starts by defining the value of N, which represents the number of queens and the size of the chessboard.

2. Three arrays `ld`, `rd`, and `cl` are initialized with zeros. These arrays are used to keep track of the occupied positions by the queens in the left diagonal, right diagonal, and columns of the chessboard.

3. The `printSolution` function is defined to print the final configuration of the chessboard with queens placed.

4. The `solveNQUtil` function is the main recursive function that solves the N-Queens problem. It takes the current state of the chessboard `board` and the current column `col` as parameters.

5. The base case for the recursive function is when `col` becomes greater than or equal to `N`, indicating that all queens have been successfully placed.

6. Inside the recursive function, a loop runs through each row of the current column (`i` ranges from 0 to N-1).

7. For each row `i`, it checks if it is safe to place a queen at position `board[i][col]` by verifying that no other queen threatens it diagonally or horizontally.

8. The `ld`, `rd`, and `cl` arrays are used to check if there is a queen on the left diagonal, right diagonal, or the same column of the current position.

9. If it is safe to place a queen at `board[i][col]`, it marks that position as occupied by setting `board[i][col] = 1`, and updates the `ld`, `rd`, and `cl` arrays accordingly.

10. The `solveNQUtil` function is then recursively called with the next column (`col + 1`).

11. If the recursive call returns `True`, it means that all queens have been successfully placed, and the solution is found. It returns `True` to propagate the solution back to the initial call.

12. If the recursive call returns `False`, it means that it was not possible to place all queens in a safe manner in the current configuration. In this case, it backtracks by resetting the position `board[i][col]` to 0 and updating the `ld`, `rd`, and `cl` arrays.

13. After the loop, if no solution is found, the function returns `False`.

14. The `solveNQ` function is called to initialize the chessboard and start solving the N-Queens problem.

15. It creates an empty chessboard represented by a 2D list `board`.

16. It calls the `solveNQUtil` function with the initial state of the chessboard (`board`) and the first column (`0`).

17. If the `solveNQUtil` function returns `False`, it means that no solution exists, and it prints "Solution does not exist".

18. If the `solveNQUtil` function returns `True`, it means that a solution is found, and it calls the `printSolution` function to print the final configuration of the chessboard with the queens placed.

19. Finally, the `solveNQ` function returns `True`.

The code demonstrates a backtracking algorithm to solve the N-Queens problem by recursively exploring different possible configurations of the chessboard until a valid solution is found. It utilizes the properties of diagonals and columns to check the safety of placing queens at each position.
'''
