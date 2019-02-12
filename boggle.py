def make_grid(width, height):
    """
    Creates a grid that will hold all of the tiles
    for a boggle game | creates a dictionary with the row column tuple as the key and space as the value, (no letters yet).
    """
    return {(row, col): ' ' for row in range(height)
for col in range(width)}