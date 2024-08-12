# my_string = '''Hello mina'''
# print(my_string)

# s = "Hello, World!"



# s = s.lower()
# s1 = "hello, world!"

# print(s1 == s)

# input_string = input("Nhập một chuỗi ký tự bất kỳ: ")

# # words = input_string.split()

# # num_words = len(input_string.split())


# print("Số cụm từ được phân cách bởi dấu cách là:",len(input_string.split()))

# l = [x for x in range(10)]
# print(l)
# Nhập một chuỗi các số nguyên từ bàn phím, ngăn cách nhau bởi dấu cách
input_string = input("Nhập các số nguyên, ngăn cách nhau bởi dấu cách: ")

# Sử dụng split() để tách chuỗi thành danh sách các chuỗi con
string_list = input_string.split()

# Chuyển đổi danh sách các chuỗi con thành danh sách các số nguyên
int_list = [int(num) for num in string_list]

# Sắp xếp danh sách các số nguyên theo thứ tự tăng dần
int_list.sort()

# In mảng số nguyên đã sắp xếp
print("Mảng số nguyên đã sắp xếp theo thứ tự tăng dần:", int_list)





