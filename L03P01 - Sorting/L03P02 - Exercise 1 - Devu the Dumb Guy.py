def solve():
    # Nhập n (số môn học) và x (thời gian học mỗi chương ban đầu)
    try:
        line1 = input().split()
        if not line1:
            return
        n = int(line1[0])
        x = int(line1[1])
        
        # Nhập danh sách số chương của mỗi môn học
        chapters = list(map(int, input().split()))
    except EOFError:
        return

    # Bước 1: Sắp xếp danh sách chương theo thứ tự tăng dần
    # Điều này đảm bảo môn nhiều chương nhất sẽ được học với thời gian ít nhất
    chapters.sort()
    
    total_time = 0
    current_time_per_chapter = x
    
    # Bước 2: Duyệt qua từng môn học đã sắp xếp
    for c in chapters:
        # Cộng dồn thời gian học của môn hiện tại vào tổng
        total_time += c * current_time_per_chapter
        
        # Bước 3: Giảm thời gian học mỗi chương cho môn tiếp theo
        # Quy tắc: không được giảm xuống dưới 1 giờ
        if current_time_per_chapter > 1:
            current_time_per_chapter -= 1
            
    # Bước 4: In ra tổng thời gian tối thiểu
    print(total_time)

if __name__ == "__main__":
    solve()