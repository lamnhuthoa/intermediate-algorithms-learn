# Vitaly and Strings
"""
Vitaly is a diligent student who never missed a lesson in his five years of studying in the university. 
He always does his homework on time and passes his exams in time.

During the last lesson the teacher has provided two strings s and t to Vitaly. 
The strings have the same length, they consist of lowercase English letters, string s is lexicographically smaller than string t. 

Vitaly wondered if there is such string that is lexicographically larger than string s and at the same is lexicographically smaller than string t. 
This string should also consist of lowercase English letters and have the length equal to the lengths of strings s and t.

* Input format
- The first line contains string s (1 <= s <= 100), consisting of lowercase English letters. Here, |s| denotes the length of the string.
- The second line contains string t (|s| = |t|), consisting of lowercase English letters.
It is guaranteed that the lengths of string s and t are the same and string s is lexicographically less than t.

* Output
- If the string that meets the given requirements doesn't exist, print a single string "No such string" (without the quotes).
- If such string exists, print it. If there are multiple answers, print any of them.
"""

def next_lexicographic_string(s: str, t: str) -> str:
    s_list = list(s)
    n = len(s_list)
    for i in range(n - 1, -1, -1):
        if s_list[i] != 'z':
            s_list[i] = chr(ord(s_list[i]) + 1)
            for j in range(i + 1, n):
                s_list[j] = 'a'
            candidate = ''.join(s_list)
            if candidate < t:
                return candidate
            else:
                return "No such string"
    return "No such string"
            
s = input()
t = input()
result = next_lexicographic_string(s, t)
print(result)