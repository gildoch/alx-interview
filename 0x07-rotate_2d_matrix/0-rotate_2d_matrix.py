def rotate_2d_matrix(matrix):
    """
    Rotates a given n x n 2D matrix 90 degrees clockwise in-place.
    Args:
        matrix: List of lists where each inner list represents a row of the
        matrix.
    """
    n = len(matrix)
    # Transpose the matrix (swap rows with columns)
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    # Reverse each row to achieve the 90-degree rotation
    for row in matrix:
        row.reverse()
