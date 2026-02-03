# Big Segment
"""
A coordinate line has n segments, the i-th segment starts at the position l_i and ends at the position r_i. 
We will denote such a segment as [l_i, r_i].

You have suggested that one of the defined segments covers all others. In other words, there is such segment 
in the given set, which contains all other ones. Now you want to test your assumption. Find in the given set 
the segment which covers all other segments, and print its number. If such a segment doesn't exist, print -1.

Formally we will assume that segment [a, b] covers segment [c, d], if they meet this condition:
a <= c <= d <= b

* Input Format
- The first line contains integer n (1 <= n <= 10^5) — the number of segments.
- Next n lines contain the descriptions of the segments. The i-th line contains two space-separated integers 
  l_i, r_i (1 <= l_i <= r_i <= 10^9) — the borders of the i-th segment.
- It is guaranteed that no two segments coincide.

* Output Format
Print a single integer — the number of the segment that covers all other segments in the set. 
If there's no solution, print -1.

The segments are numbered starting from 1 in the order in which they appear in the input.

* Approach
1. Find the segment with minimum left boundary (smallest l_i)
2. Find the segment with maximum right boundary (largest r_i)
3. If they are the same segment and it covers all others, return its number
4. Otherwise, return -1
"""

n = int(input())
segments = []

for i in range(n):
    l, r = map(int, input().split())
    segments.append((l, r, i + 1))  # Store (left, right, 1-indexed position)

# Find segment with minimum left boundary
min_left_idx = 0
for i in range(1, n):
    if segments[i][0] < segments[min_left_idx][0]:
        min_left_idx = i

# Find segment with maximum right boundary
max_right_idx = 0
for i in range(1, n):
    if segments[i][1] > segments[max_right_idx][1]:
        max_right_idx = i

# Check if they are the same segment
if min_left_idx == max_right_idx:
    # This segment has the minimum left and maximum right
    # Now check if it covers all other segments
    covering_segment = segments[min_left_idx]
    covers_all = True
    
    for i in range(n):
        if i != min_left_idx:
            # Check if covering_segment covers segments[i]
            if not (covering_segment[0] <= segments[i][0] and segments[i][1] <= covering_segment[1]):
                covers_all = False
                break
    
    if covers_all:
        print(covering_segment[2])
    else:
        print(-1)
else:
    # If min left and max right belong to different segments,
    # no single segment can cover all others
    print(-1)


# ============================================================================
# ALTERNATIVE SOLUTION 1: Simpler with min/max functions
# ============================================================================

def solution_v2():
    """
    Alternative solution using Python's built-in min/max functions.
    """
    n = int(input())
    segments = []
    
    for i in range(n):
        l, r = map(int, input().split())
        segments.append((l, r, i + 1))
    
    # Find the segment that could potentially cover all others
    # It must have the minimum left and maximum right
    min_left = min(seg[0] for seg in segments)
    max_right = max(seg[1] for seg in segments)
    
    # Find the segment with min_left and max_right
    candidate = -1
    for seg in segments:
        if seg[0] == min_left and seg[1] == max_right:
            candidate = seg[2]
            break
    
    if candidate != -1:
        # Verify it covers all segments (should be guaranteed by our logic)
        print(candidate)
    else:
        print(-1)

# Uncomment to use: solution_v2()


# ============================================================================
# ALTERNATIVE SOLUTION 2: One-pass solution with tracking
# ============================================================================

def solution_v3():
    """
    One-pass solution that tracks min left and max right simultaneously.
    """
    n = int(input())
    segments = []
    
    min_left = float('inf')
    max_right = -1
    min_left_idx = -1
    max_right_idx = -1
    
    for i in range(n):
        l, r = map(int, input().split())
        segments.append((l, r, i + 1))
        
        if l < min_left:
            min_left = l
            min_left_idx = i
        
        if r > max_right:
            max_right = r
            max_right_idx = i
    
    # Check if the same segment has both min left and max right
    if min_left_idx == max_right_idx:
        print(segments[min_left_idx][2])
    else:
        print(-1)

# Uncomment to use: solution_v3()
