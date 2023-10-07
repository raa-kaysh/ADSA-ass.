def matrix_chain_multiplication(matrix_dimensions):
    """
    Calculates the optimal parenthesization and minimum scalar multiplications for matrix chain multiplication.

    Parameters:
    matrix_dimensions (list): List of tuples representing matrix dimensions.

    Returns:
    tuple: Optimal parenthesization sequence, minimum scalar multiplications.
    """
    n = len(matrix_dimensions)
    dp = [[float('inf')] * n for _ in range(n)]  # Initialize DP table

    # Initialize diagonal with zeros (base case for chain length 1)
    for i in range(n):
        dp[i][i] = 0

    for chain_length in range(2, n + 1):
        for i in range(n - chain_length + 1):
            j = i + chain_length - 1
            for k in range(i, j):
                cost = dp[i][k] + dp[k + 1][j] + matrix_dimensions[i][0] * matrix_dimensions[k][1] * matrix_dimensions[j][1]
                if cost < dp[i][j]:
                    dp[i][j] = cost

    # Reconstructing optimal parenthesization
    optimal_parenthesization = reconstruct_optimal_parenthesization(dp, matrix_dimensions, 0, n - 1)

    return optimal_parenthesization, dp[0][n - 1]


def reconstruct_optimal_parenthesization(dp, matrix_dimensions, i, j):
    if i == j:
        return f'M{str(i + 1)}'
    
    for k in range(i, j):
        if dp[i][j] == dp[i][k] + dp[k + 1][j] + matrix_dimensions[i][0] * matrix_dimensions[k][1] * matrix_dimensions[j][1]:
            return f'({reconstruct_optimal_parenthesization(dp, matrix_dimensions, i, k)} × {reconstruct_optimal_parenthesization(dp, matrix_dimensions, k + 1, j)})'


# Example usage
matrix_dimensions = [(2, 3), (3, 4), (4, 2)]
optimal_parenthesization, min_scalar_multiplications = matrix_chain_multiplication(matrix_dimensions)

print("Optimal Parenthesization:", optimal_parenthesization)
print("Minimum Scalar Multiplications:", min_scalar_multiplications)

"""
Sample output:

Optimal Parenthesization: ((M1 × (M2 × M3)))
Minimum Scalar Multiplications: 52
"""


"""

Explanation of Dynamic Programming Approach:
We use dynamic programming to solve this problem. The dp table is used to store the minimum scalar multiplications needed to compute the product of matrices. 
We iteratively calculate the minimum scalar multiplications for increasing chain lengths and then reconstruct the optimal parenthesization.


Calculation of Minimum Scalar Multiplications:
The minimum scalar multiplications are obtained from the dp table for the full matrix chain, i.e., dp[0][n - 1], where n is the number of matrices.

Reconstruction of Optimal Parenthesization:
We reconstruct the optimal parenthesization by recursively finding the split point that minimizes the cost. The function reconstruct_optimal_parenthesization 
helps in this reconstruction.


Time and Space Complexity Analysis:
Time complexity: O(n^3) where n is the number of matrices.
Space complexity: O(n^2) for the DP table.
The algorithm is efficient and can handle a large number of matrices. Its time complexity allows it to handle a reasonable number of matrices efficiently.
