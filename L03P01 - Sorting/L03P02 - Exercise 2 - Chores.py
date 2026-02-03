def solve():
    try:
        input_line1 = input().split()
        if not input_line1:
            return
        
        num_chores = int(input_line1[0]) # n: tổng số công việc
        petya_target_count = int(input_line1[1]) # a: số việc Petya cần làm
        vasya_target_count = int(input_line1[2]) # b: số việc Vasya cần làm
        
        # Nhập danh sách độ phức tạp của các công việc
        complexities = list(map(int, input().split()))
    except EOFError:
        return
    
    
    # Bước 1: Sắp xếp để dễ dàng phân chia nhóm theo độ phức tạp theo thứ tự tăng dần
    complexities.sort()
    
    # Bước 2: Xác định ranh giới giữa hai anh em
    # Vasya lấy 'vasya_target_count' công việc đầu tiên (chỉ số 0 đến b-1)
    # Petya lấy 'petya_target_count' công việc còn lại (chỉ số b đến n-1)
    vasya_last_chore_idx = vasya_target_count - 1
    petya_first_chore_idx = vasya_target_count
    
    max_complexity_vasya = complexities[vasya_last_chore_idx]
    min_complexity_petya = complexities[petya_first_chore_idx]
    
    # Bước 3: Kiểm tra tính tồn tại của x
    # Nếu giá trị nhỏ nhất của Petya bằng giá trị lớn nhất của Vasya
    # thì không có số nguyên x nào nằm giữa chúng để phân tách 2 nhóm
    if min_complexity_petya == max_complexity_vasya:
        print(0)
    else:
        # Số lượng giá trị x thỏa mãn max_vasya <= x < min_petya
        number_of_valid_x = min_complexity_petya - max_complexity_vasya
        print(number_of_valid_x)