# Skill: Array and Strings

## Syntax

- Use `while i < len(nums) - 1` to iterate and modify single array in-place.
- Use `for i in range(1, len(nums))` to skip index when using for loop.
- Use `for i in reversed(range(len(nums)))` to loop from the end.
- Use `for i, num in enumerate(nums)` to loop both index and item.
- Use `copy = nums[:]` to copy 1D array.
- Use `copy = [row[:] for row in nums]` to copy 2D array.
- Use `x, y = y, x` to swap variables
- Use `nums.reverse()` to reverse array
- Use `string[::-1]` to reverse string

## Basic Operations and Functions

- Use `%` to get remainder
- Use `//` to get floored division
- Use `**` to get exponent
- Use `^` to get unique number
- Use `~` to mirror index
- Apply `reverse()` first to rotate array
- Apply `sort()` first to detect duplication

## Bitwise Operations

- `&` AND: check identical
- `|` OR: keep positive
- `^` XOR: cancel duplication
- `~` Ones Complement: flip binary

## Conversion

- `list()` return array
- `str()` return string
- `int()` return integer
- `ord()` convert string to integer

## 1D Array Calculation

- Convert array to string or int if necessary
- Handle edge case such as `9` and `0`

## 1D Array Methodology

- Use memory instead of operation to reduce runtime and memory.
- Use pointer to track either index or item.
- Use pointer only when the output cannot be determined immediately.
- Use two-pointers (`i` and `i+1`) to track current and next position.
- Use two-pointers (`i` and `j`) to track two arrays.
- Append buffer (`#`) at the start or the end to prevent overflow.
- Use hashMap (`{}`) to track a pair of values.

## 2D Array Methodology

- Use `numpy` or `reserve` to transpose matrix
- Use `//` and `%` to iterate Sudoku
- Reorder rows, cols and boxs when iterating Sudoku

## String Methodology

- Use `string[::-1]` to reverse string.
- Use `Counte()` to count or find unique character.
- Use `lower()` and `capitalize()` to convert case.
- Use `isalnum()` to check alphanumeric
- Use `groupby()` to return iterators of grouped objects
- Use `Counter()` to return counts of hashable objects
- Use `min()` and `max()` to find shortest and longest