a = int(input("Enter the start of the range (a): "))
b = int(input("Enter the end of the range (b): "))
print(f"\n--- Calculating reciprocals for numbers in range ({a}, {b}) ---")
for j in range(a + 1, b):
    print(f"\nNumber (j): {j}")
    reciprocal_result = 1 / j
    print(f"-> Reciprocal (1/{j}): 1/{j}")
    print(f"-> Decimal result: {reciprocal_result}")
print("\n--- End of calculation ---")
