result_list = []
for i in range(2000, 3201):
    if (i % 7 == 0) and (i % 5 != 0):
        result_list.append(str(i))
print(', '.join(result_list))
