import math

def solve_quadratic_equation():
    """
    Giải phương trình bậc hai ax^2 + bx + c = 0.
    """
    print("--- Giải Phương Trình Bậc Hai: ax^2 + bx + c = 0 ---")
    try:
        a = float(input("Nhập hệ số a: "))
        b = float(input("Nhập hệ số b: "))
        c = float(input("Nhập hệ số c: "))
    except ValueError:
        print("Lỗi: Hệ số phải là số (nguyên hoặc thập phân).")
        return
    print(f"\nPhương trình đã nhập: {a}x^2 + {b}x + {c} = 0")
    if a == 0:
        if b == 0:
            if c == 0:
                print("Phương trình có vô số nghiệm (0=0).")
            else:
                print("Phương trình vô nghiệm (0=c, c khác 0).")
        else:
            x = -c / b
            print(f"Đây là phương trình bậc nhất. Nghiệm duy nhất là x = {x:.4f}")
        return
    delta = b**2 - 4 * a * c
    print(f"Delta (Δ) = {delta:.4f}")
    if delta < 0:
        real_part = -b / (2 * a)
        imaginary_part = math.sqrt(-delta) / (2 * a)
        print("Phương trình vô nghiệm thực. Có hai nghiệm phức:")
        print(f"x1 = {real_part:.4f} + {imaginary_part:.4f}i")
        print(f"x2 = {real_part:.4f} - {imaginary_part:.4f}i")
    elif delta == 0:
        x = -b / (2 * a)
        print("Phương trình có nghiệm kép:")
        print(f"x1 = x2 = {x:.4f}")
    else:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        print("Phương trình có hai nghiệm phân biệt:")
        print(f"x1 = {x1:.4f}")
        print(f"x2 = {x2:.4f}")
solve_quadratic_equation()
