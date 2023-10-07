def is_safe(board, row, col, N):
    """
    Check if it's safe to place a queen at board[row][col].

    Parameters:
    board (list): The chessboard configuration.
    row (int): The row to check.
    col (int): The column to check.
    N (int): The size of the chessboard.

    Returns:
    bool: True if safe, False otherwise.
    """
    # Check left side of the row
    for i in range(col):
        if board[row][i] == 'Q':
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 'Q':
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 'Q':
            return False

    return True

def solve_n_queens_util(board, col, N, solutions):
    """
    Utility function to solve N-Queens problem using backtracking.

    Parameters:
    board (list): The chessboard configuration.
    col (int): Current column to consider.
    N (int): The size of the chessboard.
    solutions (list): List to store the solutions.

    Returns:
    bool: True if a solution is found, False otherwise.
    """
    if col >= N:
        # All queens are placed
        solutions.append([''.join(row) for row in board])
        return True

    res = False
    for i in range(N):
        if is_safe(board, i, col, N):
            board[i][col] = 'Q'
            res = solve_n_queens_util(board, col + 1, N, solutions) or res
            board[i][col] = '.'

    return res

def solve_n_queens(N):
    """
    Solve the N-Queens problem for a given N.

    Parameters:
    N (int): The size of the chessboard and the number of queens.

    Returns:
    list: List of all possible solutions.
    """
    board = [['.' for _ in range(N)] for _ in range(N)]
    solutions = []
    solve_n_queens_util(board, 0, N, solutions)
    return solutions

def print_solutions(solutions):
    for idx, solution in enumerate(solutions):
        print(f"Solution {idx+1}:")
        for row in solution:
            print(' '.join(row))
        print()

# Example usage
N = 4  # Adjust N as needed
solutions = solve_n_queens(N)
print_solutions(solutions)

"""
solutions for N = 4

Solution 1:
. Q . .
. . . Q
Q . . .
. . Q .

Solution 2:
. . Q .
Q . . .
. . . Q
. Q . .

Solutions for N = 8

Solution 1:
Q . . . . . . .
. . . . Q . . .
. . . . . . . Q
. . . . . Q . .
. . Q . . . . .
. . . . . . Q .
. Q . . . . . .
. . . Q . . . .

Solution 2:
Q . . . . . . .
. . . . . Q . .
. . . . . . Q .
. . . Q . . . .
. . . . . . Q .
. Q . . . . . .
. . . . Q . . .
. . Q . . . . .

Solution 3:
. Q . . . . . .
. . . . . Q . .
. . . . . . Q .
Q . . . . . . .
. . . Q . . . .
. . . . . . Q .
. . Q . . . . .
. . . . Q . . .

Solution 4:
. Q . . . . . .
. . . . . . Q .
. . . Q . . . .
. . . . . Q . .
Q . . . . . . .
. . . . Q . . .
. . Q . . . . .
. . . . . . Q .

Solution 5:
. . Q . . . . .
Q . . . . . . .
. . . . Q . . .
. Q . . . . . .
. . . . . . Q .
. . . Q . . . .
. . . . . Q . .
. . . . . . . Q

Solution 6:
. . Q . . . . .
. . . . . Q . .
Q . . . . . . .
. . . Q . . . .
. . . . . . Q .
. Q . . . . . .
. . . . Q . . .
. . . . . . Q .

Solution 7:
. . . Q . . . .
. . Q . . . . .
. . . . . Q . .
Q . . . . . . .
. . . . . . Q .
. Q . . . . . .
. . . . Q . . .
. . . . . . Q .

Solution 8:
. . . Q . . . .
. . . . . Q . .
. Q . . . . . .
. . . . Q . . .
Q . . . . . . .
. . Q . . . . .
. . . . . . Q .
. Q . . . . . .
"""

"""
Backtracking Approach Explanation:
The N-Queens problem is solved using a backtracking algorithm, which systematically explores all possible configurations of placing queens on the chessboard while 
ensuring no two queens threaten each other. The algorithm uses a recursive approach to place queens and backtrack when a solution is not possible.

is_safe function                  : checks if it's safe to place a queen at a specific position by validating the row, column, and diagonals.
solve_n_queens_util               : is a recursive backtracking function that tries to place queens column by column, ensuring they are placed safely using the is_safe 
                                    function.
The main solve_n_queens function  : initializes the chessboard, calls the utility function to solve the problem, and returns all valid solutions.
"""


"""
Time Complexity Analysis and Performance for Larger N:
The time complexity of the N-Queens problem using backtracking is difficult to determine precisely due to its dependency on the number of valid solutions 
(exponential complexity). However, for each queen placement, the algorithm explores N possibilities in each row, resulting in a time complexity of approximately O(N^N). 
In practice, this can be much less due to backtracking.

The algorithm performs well for relatively small N values (e.g., N ≤ 15) and can quickly find all possible solutions.
As N increases, the time taken grows exponentially, making the algorithm impractical for larger N (e.g., N > 15) due to the enormous number of potential solutions.
To improve performance for larger N, further optimizations such as using bit manipulation and early pruning techniques can be applied. Additionally, parallel processing 
can be utilized to speed up the search for solutions.

"""
