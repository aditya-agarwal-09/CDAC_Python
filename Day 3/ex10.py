"""
Scenario: Render a simple 2D text game board. Write a program that performs the following steps in sequence:

Creates a 
5
×
5
 grid filled with dots "." represented as a nested list.
Places a food item "F" at grid position [2, 3].
Prompts the user to enter coordinate inputs: a row and a col (integers between 0 and 4) for the snake's head.
Places the snake's head "S" at the user-supplied coordinate [row, col], overwriting the character at that position.
If the user-supplied coordinates are exactly [2, 3], print the message "Yum! The snake ate the food!" (the snake "S" will occupy index [2, 3] on the printed board, overwriting the "F").
Prints the grid neatly line-by-line (each row's elements separated by spaces).
Sample Input: (User inputs Row 0 and Column 3)
Sample Output:
. . . S .
. . . . .
. . . F .
. . . . .
. . . . .
Sample Input: (User inputs Row 2 and Column 3)
Sample Output:
. . . . .
. . . . .
. . . S .
. . . . .
. . . . .
Yum! The snake ate the food!

"""
grid = [["." for _ in range(5)] for _ in range(5)]

grid[2][3] = "F"

row = int(input("Enter row (0-4): "))
col = int(input("Enter col (0-4): "))

is_food = (row == 2 and col == 3)

grid[row][col] = "S"
                                                              
for r in grid:
    print(" ".join(r))

if is_food:
    print("Yum! The snake ate the food!")