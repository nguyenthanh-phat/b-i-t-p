import random

def player_move(total):
    while True:
        try:
            move = int(input("Bạn có muốn thêm 1, 2 hoặc 3? "))
            if move in [1, 2, 3] and total + move <= 21:
                return move
            else:
                print("Lựa chọn không hợp lệ hoặc tổng vượt quá 21. Vui lòng chọn lại.")
        except ValueError:
            print("Vui lòng nhập một số hợp lệ.")

def computer_move(total):
    # Máy tính chọn ngẫu nhiên từ 1 đến 3, nhưng phải đảm bảo không làm tổng vượt quá 21
    return min(random.choice([1, 2, 3]), 21 - total)

def main():
    total = 0
    while total < 21:
        # Người chơi 1 (người dùng)
        print(f"Tổng hiện tại: {total}")
        move = player_move(total)
        total += move
        
        if total >= 21:
            print(f"Tổng là {total}. Bạn đã thua!")
            break
        
        # Máy tính (người chơi 2)
        move = computer_move(total)
        total += move
        print(f"Máy tính thêm {move}. Tổng hiện tại: {total}")
        
        if total >= 21:
            print(f"Tổng là {total}. Máy tính đã thua!")

if __name__ == "__main__":
    main()
