def calculate_payment():
    try:
        # Nhập số tiền người dùng đã chi và chuyển đổi thành float
        amount_spent = float(input('Bạn đã chi bao nhiêu tiền tại cửa hàng? $'))
        
        # Xác định mức giảm giá
        if amount_spent >= 150:
            discount = 50
        elif amount_spent >= 100:
            discount = 25
        elif amount_spent >= 75:
            discount = 15
        else:
            discount = 0
        
        # Tính tổng số tiền phải thanh toán
        total_payment = amount_spent - discount
        
        # In ra tổng số tiền phải thanh toán
        print(f"Tổng số tiền bạn phải thanh toán là: ${total_payment:.2f}")
    except ValueError:
        print("Đầu vào không hợp lệ")

# Gọi hàm để thực hiện tính toán
calculate_payment()
