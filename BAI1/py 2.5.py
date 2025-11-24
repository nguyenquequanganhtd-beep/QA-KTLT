n = int(input("Nhập vào một số tự nhiên n (> 0): "))
if n <= 0:
    print("Nhập một số tự nhiên lớn hơn 0.")
else:
    print(f"\nCác số tự nhiên giảm dần từ {n} đến 0 là:")
    while n >= 0:
        print(n)
        n = n - 1
