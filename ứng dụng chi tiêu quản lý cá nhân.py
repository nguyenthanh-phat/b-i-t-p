def display_expenses(expenses):
    if not expenses:
        print("Danh sách chi tiêu trống.")
        return
    
    print("\nDanh sách chi tiêu:")
    for i, expense in enumerate(expenses, start=1):
        name, amount, date = expense
        print(f"{i}. Tên: {name}, Giá trị: {amount} VND, Ngày: {date}")

def add_expense(expenses):
    name = input("Nhập tên mục chi tiêu: ")
    amount = float(input("Nhập giá trị chi tiêu (VND): "))
    date = input("Nhập ngày chi tiêu (dd/mm/yyyy): ")
    expenses.append((name, amount, date))
    print("Mục chi tiêu đã được thêm.")

def remove_expense(expenses):
    display_expenses(expenses)
    try:
        index = int(input("Nhập số thứ tự của mục chi tiêu cần xoá: ")) - 1
        if 0 <= index < len(expenses):
            removed_expense = expenses.pop(index)
            print(f"Mục chi tiêu '{removed_expense[0]}' đã được xoá.")
        else:
            print("Số thứ tự không hợp lệ.")
    except ValueError:
        print("Vui lòng nhập một số hợp lệ.")

def main():
    expenses = []
    while True:
        print("\nChọn thao tác:")
        print("1. Thêm mục chi tiêu")
        print("2. Xoá mục chi tiêu")
        print("3. Hiển thị tất cả các mục chi tiêu")
        print("4. Thoát")
        
        choice = input("Nhập lựa chọn của bạn: ")
        
        if choice == '1':
            add_expense(expenses)
        elif choice == '2':
            remove_expense(expenses)
        elif choice == '3':
            display_expenses(expenses)
        elif choice == '4':
            print("Thoát chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")

if __name__ == "__main__":
    main()
