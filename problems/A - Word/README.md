# Word Case Conversion Problem

## Description

Vasya has created a browser extension that changes the case of letters in words to make them consistent. The rules are:
- If a word has more uppercase letters, convert all letters to uppercase
- If a word has more lowercase letters, convert all letters to lowercase
- If a word has an equal number of uppercase and lowercase letters, convert all letters to lowercase

The goal is to make these changes while modifying the minimum number of letters possible.

## Input
- First line contains a word *s*
- *s* consists of uppercase and lowercase Latin letters
- Length of *s* is between 1 and 100 characters

## Output
Print the corrected word *s* according to the rules above.

## Examples

### Example 1
```
Input:
HoUse

Output:
house
```

### Example 2
```
Input:
ViP

Output:
VIP
```

### Example 3
```
Input:
maTRIx

Output:
matrix
```

## Rules Summary
1. Count uppercase and lowercase letters
2. If uppercase count > lowercase count → convert all to uppercase
3. If lowercase count > uppercase count → convert all to lowercase
4. If uppercase count = lowercase count → convert all to lowercase