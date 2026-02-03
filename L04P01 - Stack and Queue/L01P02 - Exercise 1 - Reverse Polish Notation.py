def transform_to_rpn(expression):
    stack = []  # Ngăn xếp để lưu trữ toán tử và dấu ngoặc mở
    result = [] # Danh sách lưu kết quả ký pháp Ba Lan ngược
    
    for char in expression:
        # Nếu là toán hạng (chữ cái), thêm ngay vào kết quả
        if char.isalpha():
            result.append(char)
        
        # Nếu là dấu ngoặc mở hoặc toán tử, đẩy vào ngăn xếp
        elif char in "(+-*/^":
            stack.append(char)
        
        # Nếu là dấu ngoặc đóng
        elif char == ")":
            # Lấy các toán tử ra khỏi ngăn xếp cho đến khi gặp dấu ngoặc mở
            while stack and stack[-1] != "(":
                result.append(stack.pop())
            
            # Loại bỏ dấu ngoặc mở khỏi ngăn xếp
            if stack and stack[-1] == "(":
                stack.pop()
                
    return "".join(result)

def solve():
    # Nhập số lượng bộ test
    try:
        t_str = input().strip()
        if not t_str:
            return
        t = int(t_str)
        
        # Xử lý từng biểu thức
        for _ in range(t):
            expression = input().strip()
            if expression:
                print(transform_to_rpn(expression))
    except EOFError:
        pass

if __name__ == "__main__":
    solve()