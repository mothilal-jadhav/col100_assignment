# COL100 Assignment

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
python3 test_visible.py
```
