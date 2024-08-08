def calculate_bmi():
    try:
        # Nhập cân nặng và chiều cao từ người dùng
        weight = float(input('Nhập cân nặng của bạn (kg): '))
        height = float(input('Nhập chiều cao của bạn (m): '))
        
        # Tính chỉ số BMI
        bmi = weight / (height ** 2)
        
        # Xác định tình trạng cơ thể dựa trên BMI
        if bmi < 16:
            status = "Gầy cấp độ III"
        elif  bmi < 17:
            status = "Gầy cấp độ II"
        elif  bmi < 18.5:
            status = "Gầy cấp độ I"
        elif  bmi < 25:
            status = "Bình thường"
        elif  bmi < 30:
            status = "Thừa cân"
        elif  bmi < 35:
            status = "Béo phì cấp độ I"
        elif  bmi < 40:
            status = "Béo phì cấp độ II"
        else:
            status = "Béo phì cấp độ III"
        
        # In ra chỉ số BMI và tình trạng cơ thể
        print(f"Chỉ số BMI của bạn là: {bmi:.2f}")
        print(f"Tình trạng cơ thể của bạn là: {status}")
    
    except ValueError:
        print("Đầu vào không hợp lệ. Vui lòng nhập số hợp lệ cho cân nặng và chiều cao.")

# Gọi hàm để thực hiện tính toán
calculate_bmi()
