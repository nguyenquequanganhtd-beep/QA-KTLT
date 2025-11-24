n = int(input("Nhập vào một số nguyên n: "))
square_dict = dict() 
for i in range(1, n + 1):
    square_dict[i] = i * i
print(square_dict)
