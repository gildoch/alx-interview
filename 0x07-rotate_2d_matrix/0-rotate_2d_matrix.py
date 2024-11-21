def rotate_2d_matrix(matrix):
    """
    Rotates a 2D matrix 90 degrees clockwise in-place.
    Args:
        matrix: A list of n lists where each inner list represents a row of the
        matrix.
    """
    n = len(matrix)

    # Process each layer from the outermost to the innermost
    for layer in range(n // 2):
        first, last = layer, n - 1 - layer  # Define the boundaries of the
        current layer

        for i in range(first, last):
            offset = i - first  # Offset for elements in the current layer

            # Save the top-left element
            top_left = matrix[first][i]

            # Move bottom-left to top-left
            matrix[first][i] = matrix[last - offset][first]

            # Move bottom-right to bottom-left
            matrix[last - offset][first] = matrix[last][last - offset]

            # Move top-right to bottom-right
            matrix[last][last - offset] = matrix[i][last]

            # Move top-left to top-right
            matrix[i][last] = top_left
