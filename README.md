# COL100 Assignment

# A1
This file contains four small Python functions from the assignment.

## Logic

### `digit_dominance(n)`

Converts the number to a string and checks every digit one by one.
It counts how many digits are even and how many are odd, then returns:

- `MoreEven` if even digits are more
- `MoreOdd` if odd digits are more
- `Equal` if both counts are same

### `number_hill(n)`

Builds a number pattern row by row.
First it creates the upper half from `1` to `n`, then creates the lower half from `n-1` back to `1`.
Each row increases up to the middle number and then decreases again.

### `first_repeated_digit(n)`

Checks digits from right to left using `% 10`.
A set is used to store digits that have already appeared.
If a digit is found again, it is returned as the first repeated digit from the right side.
If no digit repeats, it returns `No Repetition`.

### `hollow_right_triangle(n)`

Creates a right triangle pattern using stars.
The first two rows and the last row are filled with stars.
For the middle rows, only the first and last positions have stars, and the inside is filled with spaces.

## Running Tests

Run the visible tests with:

```bash
cd A1
python3 test_visible.py
```
# A2

## A2 Logic

The A2 solutions mainly use recursion. Each public function calls a helper
function where the actual recursive work happens, then prints the final answer
in the format required by the visible tests.

### `power(x, y)`

Computes `x` raised to the power `y` recursively.
The idea is to reduce the exponent by one at every step:

- `power(x, 0)` is the base case and returns `1`
- otherwise, the answer is `x * power(x, y - 1)`

Before each recursive call, the helper prints the current function call, so the
output shows how the recursion moves toward the base case.

### `isEven(n)` and `isOdd(n)`

Checks parity using mutual recursion.
The idea is that an even number becomes odd when reduced by `1`, and an odd
number becomes even when reduced by `1`.

- `isEven(0)` returns `True`
- `isOdd(0)` returns `False`
- for any other number, `isEven(n)` calls `isOdd(n - 1)`
- similarly, `isOdd(n)` calls `isEven(n - 1)`

The input is converted using `abs(n)` first, so negative numbers are handled by
checking their positive value.

### `count_paths(grid)`

Counts the number of valid paths from the top-left cell to the bottom-right
cell of a grid.
The idea is to try only two moves from each cell: down and right.

The helper returns:

- `0` if the current position goes outside the grid
- `0` if the current cell is blocked with `1`
- `1` if the destination cell is reached
- otherwise, paths from the cell below plus paths from the cell on the right

This works because every valid path from a cell must start with either a down
move or a right move.

### `is_palindrome(s)`

Checks whether a string is a palindrome after ignoring spaces, punctuation, and
letter case.
First, the function builds a cleaned string containing only lowercase
alphanumeric characters.

Then the helper compares characters from both ends:

- if the left index crosses the right index, the string is a palindrome
- if the two characters are different, it returns `False`
- otherwise, it moves inward and checks the next pair

The comparison is printed at each step so the recursive checking process is
visible.

### `generate_subsets(nums)`

Generates all subsets of a list using backtracking.
At each index, there are two choices:

- include the current element in the subset
- skip the current element

When the index reaches the end of the list, the current subset is copied into
the result. The copy is important because the same temporary list is reused
while backtracking.

## Running A2 Tests

Run the visible tests with:

```bash
cd A2
python3 test_visible.py
```