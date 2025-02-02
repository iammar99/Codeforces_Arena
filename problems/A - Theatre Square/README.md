# Theatre Square (Problem 1A)

## Problem Description
In Berland's capital city, there's a rectangular Theatre Square measuring n × m meters. For the city's anniversary celebration, the square needs to be paved with a × a square granite flagstones. The task is to determine the minimum number of flagstones required to completely cover the square.

### Key Points
- The square can be covered beyond its actual size
- Flagstones cannot be broken
- Flagstone sides must be parallel to the square's sides
- Entire square must be covered

## Constraints
- 1 ≤ n, m, a ≤ 10^9
- n, m, and a are positive integers

## Input Format
A single line containing three space-separated integers:
```
n m a
```
Where:
- n = length of the Theatre Square
- m = width of the Theatre Square
- a = size of each square flagstone

## Output Format
One integer representing the minimum number of flagstones needed.

## Solution Approach
1. For each dimension (length and width):
   - Calculate how many flagstones are needed
   - If the dimension isn't perfectly divisible by flagstone size, add one extra flagstone
2. Multiply the number of flagstones needed in each dimension

### Mathematical Formula
```
⌈n/a⌉ × ⌈m/a⌉
```
Where ⌈x⌉ represents the ceiling function (rounding up to nearest integer)

## Example
### Input
```
6 6 4
```

### Output
```
4
```