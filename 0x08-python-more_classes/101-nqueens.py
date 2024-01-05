#!/usr/bin/python3
"""
The N queens puzzle is the challenge
of placing N non-attacking queens on an NxN chessboard.
"""

from sys import argv

if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: nqueens N")
        exit(1)

    if not argv[1].isdigit():
        print("N must be a number")
        exit(1)

    n = int(argv[1])

    if n < 4:
        print("N must be at least 4")
        exit(1)

    # Initialize the answer list
    a = [[i, None] for i in range(n)]

    def already_exists(y):
        """Check that a queen does not already exist in that y value."""
        return any(y == a[x][1] for x in range(n))

    def reject(x, y):
        """Determine whether or not to reject the solution."""
        if already_exists(y):
            return False

        i = 0
        while i < x:
            if abs(a[i][1] - y) == abs(i - x):
                return False
            i += 1
        return True

    def clear_a(x):
        """Clear the answers from the point of failure on."""
        for i in range(x, n):
            a[i][1] = None

    def nqueens(x):
        """Recursive backtracking function to find the solution."""
        for y in range(n):
            clear_a(x)
            if reject(x, y):
                a[x][1] = y
                if x == n - 1:  # Accepts the solution
                    print(a)
                else:
                    nqueens(x + 1)  # Moves on to the next x value to continue

    # Start the recursive process at x = 0
    nqueens(0)
