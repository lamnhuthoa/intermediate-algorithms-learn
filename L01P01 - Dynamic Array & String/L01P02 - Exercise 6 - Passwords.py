# Passwords
"""
Vanya is managed to enter his favourite site Codehorses. Vanya uses n distinct passwords for sites at all, 
however he can't remember which one exactly he specified during Codehorses registration.

Vanya will enter passwords in order of non-decreasing their lengths, and he will enter passwords of same length in arbitrary order. 
Just when Vanya will have entered the correct password, he is immediately authorized on the site. Vanya will not enter any password twice.

Entering any passwords takes one second for Vanya. But if Vanya will enter wrong password k times, then he is able to make the next try 
only 5 seconds after that. Vanya makes each try immediately, that is, at each moment when Vanya is able to enter password, he is doing that.

Determine how many seconds will Vanya need to enter Codehorses in the best case for him (if he spends minimum possible number of second) 
and in the worst case (if he spends maximum possible amount of seconds).

* Input Format
- The first line of the input contains two integers n and k (1 <= n, k <= 100) — the number of Vanya's passwords and the number of failed 
  tries, after which the access to the site is blocked for 5 seconds.
- The next n lines contains passwords, one per line — pairwise distinct non-empty strings consisting of latin letters and digits. 
  Each password length does not exceed 100 characters.
- The last line of the input contains the Vanya's Codehorses password. It is guaranteed that the Vanya's Codehorses password is equal 
  to some of his n passwords.

* Output Format
Print two integers — time (in seconds), Vanya needs to be authorized to Codehorses in the best case for him and in the worst case respectively.
"""

n, k = map(int, input().split())
passwords = []
for _ in range(n):
    passwords.append(input().strip())

correct_password = input().strip()

# Sort passwords by length, then by content (to have consistent ordering for same length)
passwords.sort(key=lambda x: len(x))

# Find the position of correct password in sorted order
correct_pos = passwords.index(correct_password) + 1  # 1-indexed position

# Best case: correct password is the first among passwords of its length
# Group passwords by length
from collections import defaultdict
length_groups = defaultdict(list)
for pwd in passwords:
    length_groups[len(pwd)].append(pwd)

# Find how many passwords have length < correct_password's length
smaller_length_count = sum(len(group) for length, group in length_groups.items() if length < len(correct_password))

# Best case: correct password is entered as the 1st attempt among its length group
best_case = smaller_length_count + 1

# Calculate blocked time for best case
wrong_attempts_best = best_case - 1
blocked_times_best = (wrong_attempts_best // k) * 5
best_case_total = best_case + blocked_times_best

# Worst case: correct password is the last among passwords of its length
same_length_count = len(length_groups[len(correct_password)])
worst_case = smaller_length_count + same_length_count

# Calculate blocked time for worst case
wrong_attempts_worst = worst_case - 1
blocked_times_worst = (wrong_attempts_worst // k) * 5
worst_case_total = worst_case + blocked_times_worst

print(best_case_total, worst_case_total)


# ============================================================================
# ALTERNATIVE SOLUTION 1: More Concise Version
# ============================================================================

def solution_v2():
    """
    More concise version using simpler counting logic.
    """
    n, k = map(int, input().split())
    passwords = [input().strip() for _ in range(n)]
    correct_password = input().strip()
    
    # Sort passwords by length
    passwords.sort(key=len)
    
    # Count passwords with shorter length
    shorter = sum(1 for pwd in passwords if len(pwd) < len(correct_password))
    
    # Count passwords with same length
    same_length = sum(1 for pwd in passwords if len(pwd) == len(correct_password))
    
    # Best case: correct password is first among same length
    best = shorter + 1
    best_blocked = (best - 1) // k * 5
    best_total = best + best_blocked
    
    # Worst case: correct password is last among same length
    worst = shorter + same_length
    worst_blocked = (worst - 1) // k * 5
    worst_total = worst + worst_blocked
    
    print(best_total, worst_total)

# Uncomment to use: solution_v2()


# ============================================================================
# ALTERNATIVE SOLUTION 2: Direct Calculation without Dictionary
# ============================================================================

def solution_v3():
    """
    Direct calculation version that doesn't use defaultdict.
    Sorts passwords and iterates to find boundaries.
    """
    n, k = map(int, input().split())
    passwords = [input().strip() for _ in range(n)]
    correct_password = input().strip()
    
    correct_len = len(correct_password)
    
    # Sort by length
    passwords.sort(key=len)
    
    # Find index where passwords of correct length start
    first_same_len = -1
    last_same_len = -1
    
    for i, pwd in enumerate(passwords):
        if len(pwd) == correct_len:
            if first_same_len == -1:
                first_same_len = i
            last_same_len = i
    
    # Best case: first position in same length group (1-indexed)
    best = first_same_len + 1
    best_blocked = best // k * 5 if best > 1 else 0
    best_total = best + best_blocked
    
    # Worst case: last position in same length group (1-indexed)
    worst = last_same_len + 1
    worst_blocked = worst // k * 5 if worst > 1 else 0
    worst_total = worst + worst_blocked
    
    print(best_total, worst_total)

# Uncomment to use: solution_v3()
