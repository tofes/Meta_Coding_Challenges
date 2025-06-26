## Problem: Uniform Integers
## A positive integer is considered uniform if all of its digits are equal. For
## example, 222 is uniform, while 223 is not.

## Given two positive integers A and B, determine the number of uniform integers
## between A and B, inclusive.

## Constraints:
## 1 <= A <= B <= 10^(12)

## Solution
## Time Complexity: O(9 * log10(B))
## Space Complexity: O(1)
## Explanation:
'''
    n = [1..9]
                         v0 = 0
    1   = 1 + 0  + 0     v1 = v0 * 10 + n = n  shift v to left and add n
    11  = 1 + 10 + 0     v2 = v1 * 10 + n
    111 = 1 + 10 + 100   v3 = v2 * 10 + n
'''
def getUniformIntegerCountInInterval(A: int, B: int) -> int:
  total = 0
  for i in range(1, 10): # O(9)
    v = i
    while v <= B:        # O(log(B))
      if A <= v <=B:
        total += 1
      v = v * 10 + i
  return total

## Test Cases
if __name__ == "__main__":
    ## Test Case 1
    A = 75
    B = 300

    print("Test Case 1")
    print("Expected Return Value = 5")
    print("Actual Return Value   = {}".format(getUniformIntegerCountInInterval(A, B)))
    print("")

    ## Test Case 2
    A = 1
    B = 9

    print("Test Case 2")
    print("Expected Return Value = 9")
    print("Actual Return Value   = {}".format(getUniformIntegerCountInInterval(A, B)))
    print("")

    ## Test Case 3
    A = 999999999999
    B = 999999999999


    print("Test Case 3")
    print("Expected Return Value = 1")
    print("Actual Return Value   = {}".format(getUniformIntegerCountInInterval(A, B)))
    print("")
