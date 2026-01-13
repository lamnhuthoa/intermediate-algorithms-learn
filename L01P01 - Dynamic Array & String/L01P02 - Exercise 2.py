### 2. Night at the Museum
"""
Grigoriy, like the hero of one famous comedy film, found a job as a night security guard at the museum. 
At first night he received embosser and was to take stock of the whole exposition.

Embosser is a special devise that allows to "print" the text of a plastic tape. 
Text is printed sequentially, character by character. The device consists of a wheel with a lowercase English letters 
written in a circle, static pointer to the current letter and a button that print the chosen letter. 
At one move it's allowed to rotate the alphabetic wheel one step clockwise or counterclockwise. 
Initially, static pointer points to letter 'a'. Other letters are located as shown on the picture:

After Grigoriy add new item to the base he has to print its name on the plastic tape and attach it to the corresponding exhibit. 
It's not required to return the wheel to its initial position with pointer on the letter 'a'.

Our hero is afraid that some exhibits may become alive and start to attack him,
so he wants to print the names as fast as possible. Help him, for the given string find the minimum number 
of rotations of the wheel required to print it.

# Input Format
The only line of input contains the name of some exhibit — the non-empty string consisting of no more than 100 characters. 
It's guaranteed that the string consists of only lowercase English letters.

# Output Format
Print one integer — the minimum number of rotations of the wheel, required to print the name given in the input.
"""
label = input()
pos = 0
ans = 0

for c in label:
    target = ord(c) - ord('a')
    # print(target)
    diff = abs(target - pos)
    step = min(diff, 26 - diff)
    print(f"""
          Character: {c}
          Pos: {pos}
          Target to a: {target}
          Diff: select min between {diff} vs {26-diff}(26 - {diff})
          Min Step: {step}
          """)
    ans = ans + step
    pos = target
    
print(ans)

# Funtional way
def rot_dist(a: str, b: str) -> int:
    """
    Trên vòng tròn, từ pos → target có 2 đường:
        đi thẳng: diff
        đi vòng ngược lại: 26 - diff
    """
    x = ord(a) - ord('a')
    y = ord(b) - ord('a')
    diff = abs(x - y)
    return min(diff, 26 - diff)

def min_rotations_to_print(s: str) -> int:
    cur = 'a'
    total = 0
    for ch in s:
        total += rot_dist(cur, ch)
        cur = ch
    return total

s = input().strip()
print(min_rotations_to_print(s))