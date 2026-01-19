# Array - Find Minimum Segment with k Distinct Values
"""
Given an array a of n elements: a_1, a_2, ..., a_n

Your task is to find a minimal segment [l, r] (1 ≤ l ≤ r ≤ n) such that among the elements 
a_l, a_{l+1}, ..., a_r, there are exactly k distinct values.

A segment [l, r] (1 ≤ l ≤ r ≤ n) with length m = r - l + 1 that satisfies the given property 
is called minimal if there is no segment [x, y] that also satisfies the property and has length 
smaller than m, where 1 ≤ l ≤ x ≤ y ≤ r ≤ n.

Note: The segment [l, r] does not need to be the shortest among all segments with k distinct values.

* Input Format
- Line 1: Two integers n and k separated by space (1 ≤ n, k ≤ 10^5)
- Line 2: n integers separated by space: a_1, a_2, ..., a_n (1 ≤ a_i ≤ 10^5)

* Output Format
Print a pair of numbers separated by space: l and r (1 ≤ l ≤ r ≤ n), where [l, r] is the answer.
If no segment exists with exactly k distinct values, print "-1 -1".
If multiple answers exist, print any one of them.

* Approach: Sliding Window + Two Pointers
1. Use two pointers (left, right) to maintain a sliding window
2. Expand the window by moving right pointer until we have exactly k distinct values
3. Once we have k distinct values, try to shrink from left while maintaining k distinct values
4. Track the minimal segment found
5. Continue until right pointer reaches the end

* Algorithm Steps:
1. Initialize left = 0, right = 0
2. Use a frequency map (dictionary/Counter) to track distinct elements in current window
3. Expand right pointer, add elements to frequency map
4. When we have exactly k distinct elements, record the segment
5. Try to shrink from left while we still have k distinct elements
6. Continue until right reaches the end

* Time Complexity: O(n)
  - Each element is visited at most twice (once by right pointer, once by left pointer)
  - Dictionary operations (insert, delete, check) are O(1) on average
  - Overall: Two pointer traversal O(n) + O(1) operations per element = O(n)

* Space Complexity: O(k)
  - The frequency map stores at most k distinct elements
  - Maximum space used is proportional to k distinct values in the window
  - In worst case, O(min(n, max_value)) but typically O(k)

* Examples:
Example 1: n=4, k=2, array=[1, 2, 2, 3]
- Segment [1, 2]: elements [1, 2] → 2 distinct values ✓
- Output: 1 2

Example 2: n=8, k=3, array=[1, 1, 2, 2, 3, 3, 4, 5]
- Segment [2, 5]: elements [1, 2, 2, 3, 3] → 3 distinct values {1, 2, 3} ✓
- Output: 2 5

Example 3: n=7, k=4, array=[4, 7, 7, 4, 7, 4, 7]
- Only 2 distinct values {4, 7} exist → impossible to have 4 distinct
- Output: -1 -1
"""

##################################

def find_minimal_segment(n, k, A):
    MAXA = 10**5 + 1
    count = [0] * MAXA
    
    unique = 0
    j = 0
    
    for i in range(n):
        if count[A[i]] == 0:
            unique += 1
        count[A[i]] += 1
        
        if unique == k:
            while count[A[j]] > 1:
                count[A[j]] -= 1
                j += 1
                
            return j + 1, i + 1
        
    return -1, -1

n, k = map(int, input().split())
a = list(map(int, input().split()))

result = find_minimal_segment(n, k, a)
print(' '.join(map(str, result)))

#################################

from collections import defaultdict

n, k = map(int, input().split())
a = list(map(int, input().split()))

# Edge case: if k > number of distinct elements in array
distinct_values = len(set(a))
if k > distinct_values:
    print("-1 -1")
else:
    # Sliding window approach
    freq = defaultdict(int)  # Frequency map of elements in current window
    left = 0
    min_length = float('inf')
    result_l, result_r = -1, -1
    
    for right in range(n):
        # Add element at right pointer
        freq[a[right]] += 1
        
        # Try to shrink window from left while we have at least k distinct
        while len(freq) > k:
            freq[a[left]] -= 1
            if freq[a[left]] == 0:
                del freq[a[left]]
            left += 1
        
        # When we have exactly k distinct values
        if len(freq) == k:
            current_length = right - left + 1
            # Check if this is a minimal segment
            if current_length < min_length:
                min_length = current_length
                result_l = left + 1  # Convert to 1-indexed
                result_r = right + 1  # Convert to 1-indexed
    
    if result_l == -1:
        print("-1 -1")
    else:
        print(result_l, result_r)


# ============================================================================
# ALTERNATIVE SOLUTION: More Verbose with Detailed Comments
# ============================================================================

def solution_v2():
    """
    Alternative solution with more detailed steps and comments.
    """
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    
    # Check if it's possible to have k distinct values
    if k > len(set(a)):
        print("-1 -1")
        return
    
    left = 0
    freq = {}
    min_segment = None
    min_length = float('inf')
    
    for right in range(n):
        # Expand: add right element to window
        if a[right] not in freq:
            freq[a[right]] = 0
        freq[a[right]] += 1
        
        # Shrink: remove elements from left while we have more than k distinct
        while len(freq) > k:
            freq[a[left]] -= 1
            if freq[a[left]] == 0:
                del freq[a[left]]
            left += 1
        
        # Record if we have exactly k distinct values
        if len(freq) == k:
            current_length = right - left + 1
            if current_length < min_length:
                min_length = current_length
                min_segment = (left + 1, right + 1)  # 1-indexed
    
    if min_segment is None:
        print("-1 -1")
    else:
        print(min_segment[0], min_segment[1])

# Uncomment to use: solution_v2()


# ============================================================================
# ALTERNATIVE SOLUTION: Find ALL minimal segments
# ============================================================================

def solution_v3():
    """
    Alternative solution that finds all minimal segments and returns one.
    """
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    
    if k > len(set(a)):
        print("-1 -1")
        return
    
    left = 0
    freq = defaultdict(int)
    min_length = float('inf')
    result = None
    
    for right in range(n):
        freq[a[right]] += 1
        
        # Shrink window from left
        while len(freq) > k:
            freq[a[left]] -= 1
            if freq[a[left]] == 0:
                del freq[a[left]]
            left += 1
        
        # Check for minimal segment
        if len(freq) == k:
            length = right - left + 1
            if length < min_length:
                min_length = length
                result = (left + 1, right + 1)
    
    print(result[0], result[1]) if result else print("-1 -1")

# Uncomment to use: solution_v3()


# ============================================================================
# ALTERNATIVE SOLUTION: Two Pointers with Manual Shrinking
# ============================================================================

def solution_v4():
    """
    Two-pointer solution that explicitly handles shrinking the window.
    This version shows the two-pointer pattern more clearly.
    
    Time Complexity: O(n) - each element visited at most twice
    Space Complexity: O(k) - frequency map size
    """
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    
    if k > len(set(a)):
        print("-1 -1")
        return
    
    left = 0
    right = 0
    freq = defaultdict(int)
    min_length = float('inf')
    result = None
    
    # Expand right pointer until we have k distinct values
    while right < n:
        # Add current element
        freq[a[right]] += 1
        
        # Shrink from left while we have more than k distinct
        while len(freq) > k:
            freq[a[left]] -= 1
            if freq[a[left]] == 0:
                del freq[a[left]]
            left += 1
        
        # Record the segment if we have exactly k distinct
        if len(freq) == k:
            current_length = right - left + 1
            if current_length < min_length:
                min_length = current_length
                result = (left + 1, right + 1)  # Convert to 1-indexed
        
        right += 1
    
    if result is None:
        print("-1 -1")
    else:
        print(result[0], result[1])

# Uncomment to use: solution_v4()


# ============================================================================
# SOLUTION: Two Pointers - Step by Step with Visualization
# ============================================================================

def solution_v5():
    """
    Two-pointer solution with step-by-step comments for clarity.
    
    Visual Example: array = [1, 1, 2, 2, 3, 3, 4, 5], k = 3
    
    Step 1: left=0, right=0, add a[0]=1
            freq={1:1}, distinct=1
    
    Step 2: left=0, right=1, add a[1]=1
            freq={1:2}, distinct=1
    
    Step 3: left=0, right=2, add a[2]=2
            freq={1:2, 2:1}, distinct=2
    
    Step 4: left=0, right=3, add a[3]=2
            freq={1:2, 2:2}, distinct=2
    
    Step 5: left=0, right=4, add a[4]=3
            freq={1:2, 2:2, 3:1}, distinct=3 ← Found k distinct!
            segment [0, 4] = [1, 1, 2, 2, 3], length=5
            Record: (1, 5) in 1-indexed
    
    Step 6: left=0, right=5, add a[5]=3
            freq={1:2, 2:2, 3:2}, distinct=3
            Shrink: left=0, remove a[0]=1
            freq={1:1, 2:2, 3:2}, distinct=3
            segment [1, 5], length=5
    
    ...continue until right reaches end
    
    Final result: (2, 5) with minimal length
    """
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    
    # Quick check: if k distinct values don't exist in array
    distinct_in_array = len(set(a))
    if k > distinct_in_array:
        print("-1 -1")
        return
    
    left = 0
    freq = defaultdict(int)
    min_segment_length = float('inf')
    best_segment = None
    
    for right in range(n):
        # EXPAND: Add element at right
        freq[a[right]] += 1
        
        # SHRINK: Remove elements from left while we have > k distinct
        while len(freq) > k:
            freq[a[left]] -= 1
            if freq[a[left]] == 0:
                del freq[a[left]]
            left += 1
        
        # CHECK: If we have exactly k distinct values
        if len(freq) == k:
            segment_length = right - left + 1
            # Update best segment if current is shorter
            if segment_length < min_segment_length:
                min_segment_length = segment_length
                best_segment = (left + 1, right + 1)  # 1-indexed
    
    if best_segment is None:
        print("-1 -1")
    else:
        print(best_segment[0], best_segment[1])

# Uncomment to use: solution_v5()
