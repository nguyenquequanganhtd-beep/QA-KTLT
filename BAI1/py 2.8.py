a, b = 1, 2
total = 0
LIMIT = 4000000
print("Dãy số Fibonacci nhỏ hơn 4,000,000:")
print(a, end=", ")
while a <= LIMIT:
    if a % 2 == 0:
        total += a
    a, b = b, a + b
    if a <= LIMIT:
        print(a, end=", ")
print("...") 
print("\n" + "-"*30) 
print(f"Tổng các số chẵn trong dãy Fibonacci (nhỏ hơn {LIMIT}): {total}")
