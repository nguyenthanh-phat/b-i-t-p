def check_number():
    try:
        # Nhập số và chuyển đổi thành float
        n = float(input('Nhập một số bất kỳ: '))
        
        # Kiểm tra số có phải là số tự nhiên không
        if n.is_integer() and n >= 0:
            # Kiểm tra số có chia hết cho 2 không
            if n % 2 == 0:
                print("số chẵn")
            elif n % 2 == 1:
                print("số lẻ")
        else:
            print("không phải số tự nhiên")
    except ValueError:
        print("Đầu vào không hợp lệ")

# Gọi hàm để thực hiện kiểm tra
check_number()
