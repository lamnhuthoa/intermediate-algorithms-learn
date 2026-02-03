# Arrays
"""
You are given two arrays A and B
B consisting of integers, sorted in non-decreasing order. Check whether it is possible to choose k numbers in array A and choose 
m numbers in array B so that any number chosen in the first array is strictly less than any number chosen in the second array.

* Input
- The first line contains two integers nA, nB (1 <= nA, nB <= 10^5), separated by space — the sizes of arrays A and B respectively.
- The second line contains two integers k and m (1 <= k <= nA, 1 <= m <= nB), separated by space.
- The third line contains nA numbers a1, a2, ..., anA (1 <= ai <= 10^9), separated by space — the elements of array A.
- The fourth line contains nB numbers b1, b2, ..., bnB (1 <= bi <= 10^9), separated by space — the elements of array B.

* Output
Print "YES" (without the quotes), if you can choose k numbers in array A and m numbers in array B so that any number chosen in array 
A was strictly less than any number chosen in array B. Otherwise, print "NO" (without the quotes).
"""

nA, nB = map(int, input().split())
k, m = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort()

# Choose k smallest from A and m largest from B
chosen_A = A[:k]
chosen_B = B[-m:]

if max(chosen_A) < min(chosen_B):
    print("YES")
else:
    print("NO")



