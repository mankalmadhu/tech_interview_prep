"""
Let's trace a couple of cells for n=3.

Size: 2 * 3 - 1 = 5. The matrix is 5x5.

Center: (3-1, 3-1) = (2, 2).

For the cell at (0, 0):

i=0, j=0.

distance = max(abs(0-2), abs(0-2)) = max(2, 2) = 2.

value = 1 + 2 = 3.

For the cell at (1, 2):

i=1, j=2.

distance = max(abs(1-2), abs(2-2)) = max(1, 0) = 1.

value = 1 + 1 = 2.


"""


def generate_pattern(n):
  """
  Generate a pattern where the input number is the outermost layer.
  Input: n (e.g., 4)
  Output: 2n-1 x 2n-1 matrix
  """
  size = 2 * n - 1
  matrix = [[0 for _ in range(size)] for _ in range(size)]

  for i in range(size):
    for j in range(size):
      # Calculate distance from center
      # Center is at position (n-1, n-1)
      distance_from_center = max(abs(i - (n - 1)), abs(j - (n - 1)))
      # Value at each position is 1 + distance_from_center
      matrix[i][j] = 1 + distance_from_center  # n-distance_from_center to invert the pattern

  return matrix


def print_pattern(matrix):
  """Print the matrix in the required format"""
  for row in matrix:
    print(' '.join(map(str, row)))


# Generate and print the pattern
if __name__ == "__main__":
  A = 4
  result = generate_pattern(A)
  print_pattern(result)
