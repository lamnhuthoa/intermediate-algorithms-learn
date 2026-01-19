# Suffix Structures
"""
Bizon The Champion's team is faced with the problem of transforming string s into string t 
using two types of operations (suffix structures):

1. Suffix Automaton: Can delete any character from the string (can be used unlimited times)
2. Suffix Array: Can swap any two characters in the string (can be used unlimited times)

We need to determine which combination of these structures is needed to transform s into t.

* Analysis:
- If t cannot be formed from characters of s: "need tree" (impossible even with both)
- If t is a subsequence of s but characters are in different order: "both" (need automaton to delete, array to rearrange)
- If t is a subsequence of s and characters are already in sorted order: "automaton" (just delete unnecessary chars)
- If t can be obtained by rearranging s (same characters, different order): "array" (just rearrange)

* Logic:
1. Check if all characters in t exist in s with correct frequencies
   - If not: "need tree"
   - If yes: Continue
2. Check if t is a subsequence of s (delete-only approach works)
   - If yes: Check if characters in t are in non-decreasing order in s
     - If yes: "automaton" (only deletions needed)
     - If no: "both" (need deletions and swaps)
   - If no: Check if s and t have same characters (rearrangement only)
     - If yes: "array" (only swaps needed)
     - If no: "both" (need both operations) or "need tree"

* Input Format
- Line 1: String s (non-empty, lowercase English letters, max 100 characters)
- Line 2: String t (non-empty, lowercase English letters, max 100 characters)
- s and t are different

* Output Format
Print one of:
- "need tree": Cannot transform s to t even with both structures
- "automaton": Only suffix automaton needed (only delete characters)
- "array": Only suffix array needed (only rearrange characters)
- "both": Need both structures (delete and rearrange)
"""

s = input().strip()
t = input().strip()

# Check if all characters of t exist in s with sufficient frequency
from collections import Counter
s_count = Counter(s)
t_count = Counter(t)

# If t has any character not in s, or has more of a character than s
can_form = True
for char, count in t_count.items():
    if s_count[char] < count:
        can_form = False
        break

if not can_form:
    print("need tree")
else:
    # Check if t is a subsequence of s
    def is_subsequence(s, t):
        s_idx = 0
        for char in t:
            found = False
            while s_idx < len(s):
                if s[s_idx] == char:
                    s_idx += 1
                    found = True
                    break
                s_idx += 1
            if not found:
                return False
        return True
    
    is_subseq = is_subsequence(s, t)
    
    if is_subseq:
        # t is a subsequence of s
        # Check if characters of t appear in non-decreasing order in s
        # (meaning we only need to delete, no rearrangement needed)
        positions = []
        s_idx = 0
        for char in t:
            while s_idx < len(s):
                if s[s_idx] == char:
                    positions.append(s_idx)
                    s_idx += 1
                    break
                s_idx += 1
        
        # If t is a subsequence of s, we can just delete to get t (automaton only)
        print("automaton")
    else:
        # t is not a subsequence of s
        # Check if s and t have exactly the same characters (just rearrangement needed)
        if sorted(s) == sorted(t):
            print("array")
        else:
            print("both")


# ============================================================================
# ALTERNATIVE SOLUTION: More explicit logic
# ============================================================================

def solution_v2():
    """
    Alternative solution with more explicit case handling.
    """
    s = input().strip()
    t = input().strip()
    
    from collections import Counter
    
    s_count = Counter(s)
    t_count = Counter(t)
    
    # Case 1: Check if t can be formed from s's characters
    if not all(s_count[c] >= t_count[c] for c in t_count):
        print("need tree")
        return
    
    # Check if t is a subsequence of s
    def is_subsequence(text, pattern):
        it = iter(text)
        return all(c in it for c in pattern)
    
    # Case 2: t is a subsequence of s
    if is_subsequence(s, t):
        # If t is a subsequence of s, only automaton (deletion) is needed
        print("automaton")
    else:
        # Case 3: t is not a subsequence of s
        # Check if same characters exist
        if sorted(s) == sorted(t):
            # Same characters, different order - only array needed
            print("array")
        else:
            # Different characters with same frequency issue - both needed
            print("both")

# Uncomment to use: solution_v2()
