def print_day_of_week():
    try:
        # Nhập số từ người dùng và chuyển đổi thành int
        number = int(input('Nhập một số từ 1 đến 7: '))
        
        # Kiểm tra số nhập vào và in ngày tương ứng
        if number == 1:
            print("Monday")
        elif number == 2:
            print("Tuesday")
        elif number == 3:
            print("Wednesday")
        elif number == 4:
            print("Thursday")
        elif number == 5:
            print("Friday")
        elif number == 6:
            print("Saturday")
        elif number == 7:
            print("Sunday")
        else:
            print("error, out of range")
    except ValueError:
        print("Đầu vào không hợp lệ")

# Gọi hàm để thực hiện kiểm tra
print_day_of_week()