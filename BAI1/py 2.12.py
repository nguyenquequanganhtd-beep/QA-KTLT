import re
valid_passwords = []
input_string = input("Nhập chuỗi mật khẩu (cách nhau bởi dấu phẩy): ")
password_list = input_string.split(',')
print("\n--- Bắt đầu kiểm tra ---")
for p in password_list:
    if len(p) < 6 or len(p) > 12:
        continue
    is_valid = True
    if not re.search("[a-z]", p):
        is_valid = False
    elif not re.search("[0-9]", p):
        is_valid = False
    elif not re.search("[A-Z]", p):
        is_valid = False
    elif not re.search("[\$#@]", p):
        is_valid = False
    if is_valid:
        valid_passwords.append(p)
print("\n--- Kết quả lọc ---")
print(",".join(valid_passwords))
