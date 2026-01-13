# # 1. Fashion in Berland
# """
# According to rules of the Berland fashion, a jacket should be fastened by all the buttons except only one, 
# but not necessarily it should be the last one. 
# Also if the jacket has only one button, it should be fastened, so the jacket will not swinging open.

# You are given a jacket with N buttons. Determine if it is fastened in a right way.
# """
# n = int(input())
# l = list(map(int, input().split()))
# reject = False

# if len(l) == 1:
#     if l[0] == 0:
#         reject = True
# elif len(l) > 1:
#     count_unfastened = 0

#     for i in range(len(l)):
#         if l[i] == 0:
#             count_unfastened += 1
            
#     if count_unfastened != 1:
#         reject = True
            
# print("YES" if not reject else "NO")

# # Improved version
# n = input(input())
# l = list(map(int, input().split()))

# zeros = l.count(0)

# if n == 1:
#     print("YES" if l[0] == 1 else "NO")
# else:
#     print("YES" if zeros == 1 else "NO")
    
    
# # Pythonic way
# """
# Use sum of fastened buttons
# sum(a): sum of a
# with n > 1: need n - 1 fastened buttons
# with n = 1: need 1 fastened button
# """
# n = int(input())
# a = list(map(int, input().split()))
# print(sum(a))

# need = 1 if n == 1 else n - 1
# print("YES" if sum(a) == need else "NO")

# # Function approach
# def check_jacket(v: list, n: int) -> bool:
#     if n == 1:
#         if v[0] == 1:
#             return True
#         else:
#             return False
#     count = 0
#     for i in range(n):
#         if v[i] == 0:
#             count += 1
#     if count == 1:
#         return True
#     else:
#         return False
    
# n = int(input())
# v = list(map(int, input().split()))

# if check_jacket(v, n):
#     print("YES")
# else:
#     print("NO")
