def bai_1_tong_chu_so(n):
    return sum(int(digit) for digit in str(n))

def bai_1_tong_uoc_so(n):
    return sum(i for i in range(1, n + 1) if n % i == 0)

def bai_1_kiem_tra_tam_giac(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        if a == b == c:
            return "Tam giác đều"
        elif a == b or b == c or c == a:
            return "Tam giác cân"
        elif a * a + b * b == c * c or a * a + c * c == b * b or b * b + c * c == a * a:
            return "Tam giác vuông"
        else:
            return "Tam giác nhọn hoặc tù"
    else:
        return "Không phải tam giác"

def bai_2_tinh_toan(a, b):
    return {
        'a + b': a + b,
        'a - b': a - b,
        'a * b': a * b,
        'a // b': a // b,
        'a ** b': a ** b,
        'a % b': a % b,
        'a > b': a > b,
        'a < b': a < b,
        'a == b': a == b,
        'a AND b': a & b,
        'a OR b': a | b,
        'a XOR b': a ^ b,
        'NOT a == b': not a == b,
        'a >> 1': a >> 1,
        'a << 1': a << 1
    }

def bai_3_s_tong_1(n):
    return sum((-1)**i * (i + 1) for i in range(2*n + 1))

def bai_3_s_tong_2(n):
    return sum(1 / i for i in range(1, n + 1))

def bai_3_phuong_trinh_bac_2(a, b, c):
    delta = b**2 - 4*a*c
    if delta > 0:
        return "Phương trình có 2 nghiệm phân biệt"
    elif delta == 0:
        return "Phương trình có 1 nghiệm kép"
    else:
        return "Phương trình vô nghiệm"

def bai_4_fibonacci(n):
    fibo = [0, 1]
    while len(fibo) < n:
        fibo.append(fibo[-1] + fibo[-2])
    return fibo[:n]

def bai_5_armstrong(n):
    armstrong_numbers = []
    for num in range(1, n + 1):
        if sum(int(digit)**3 for digit in str(num)) == num:
            armstrong_numbers.append(num)
    return armstrong_numbers

def bai_6_hoan_hao(n):
    hoan_hao_numbers = []
    for num in range(2, n + 1):
        if sum(i for i in range(1, num) if num % i == 0) == num:
            hoan_hao_numbers.append(num)
    return hoan_hao_numbers

def bai_7_amicable(n):
    def sum_of_divisors(num):
        return sum(i for i in range(1, num) if num % i == 0)
    amicable_pairs = []
    for a in range(1, n + 1):
        b = sum_of_divisors(a)
        if a != b and a == sum_of_divisors(b) and (b, a) not in amicable_pairs:
            amicable_pairs.append((a, b))
    return amicable_pairs

def bai_8_pascal_triangle(n):
    triangle = []
    for i in range(n):
        row = [1]
        if triangle:
            last_row = triangle[-1]
            row.extend([sum(pair) for pair in zip(last_row, last_row[1:])])
            row.append(1)
        triangle.append(row)
    return triangle

def bai_9_bits_count(a):
    return len(bin(a)[2:])

def bai_9_print_awesome():
    x = "awesome"
    print(f"Python is {x}")
    print("Python is {}".format(x))
    print("Python is " + x)

def bai_9_python_version():
    import sys
    return sys.version

if __name__ == "__main__":
    # Test bài 1
    print("Bài 1:")
    n = int(input("Nhập số nguyên dương: "))
    print("Tổng các chữ số:", bai_1_tong_chu_so(n))
    print("Tổng các ước số:", bai_1_tong_uoc_so(n))
    
    a, b, c = map(int, input("Nhập 3 số nguyên dương cách nhau bởi dấu cách: ").split())
    print("Kiểm tra tam giác:", bai_1_kiem_tra_tam_giac(a, b, c))
    
    # Test bài 2
    print("Bài 2:")
    a, b = map(int, input("Nhập 2 số a, b cách nhau bởi dấu cách: ").split())
    results = bai_2_tinh_toan(a, b)
    for k, v in results.items():
        print(f"{k}: {v}")
    
    # Test bài 3
    print("Bài 3:")
    n = int(input("Nhập số nguyên dương n: "))
    print("S(n) = 1 - 2 + 3 - 4 + ... + (2*n + 1):", bai_3_s_tong_1(n))
    print("S(n) = 1 + 1/2 + 1/3 + ... + 1/n:", bai_3_s_tong_2(n))
    
    a, b, c = map(int, input("Nhập các hệ số a, b, c cách nhau bởi dấu cách: ").split())
    print("Biện luận nghiệm phương trình bậc 2:", bai_3_phuong_trinh_bac_2(a, b, c))
    
    # Test bài 4
    print("Bài 4:")
    n = int(input("Nhập số nguyên dương n: "))
    print("Dãy Fibonacci:", bai_4_fibonacci(n))
    
    # Test bài 5
    print("Bài 5:")
    n = int(input("Nhập số nguyên dương n: "))
    print("Số Armstrong từ 1 đến n:", bai_5_armstrong(n))
    
    # Test bài 6
    print("Bài 6:")
    n = int(input("Nhập số nguyên dương n: "))
    print("Số hoàn hảo từ 1 đến n:", bai_6_hoan_hao(n))
    
    # Test bài 7
    print("Bài 7:")
    n = int(input("Nhập số nguyên dương n: "))
    print("Cặp số Amicable từ 1 đến n:", bai_7_amicable(n))
    
    # Test bài 8
    print("Bài 8:")
    n = int(input("Nhập số nguyên dương n: "))
    print("Tam giác Pascal:")
    triangle = bai_8_pascal_triangle(n)
    for row in triangle:
        print(row)
    
    # Test bài 9
    print("Bài 9:")
    a = int(input("Nhập số nguyên dương a: "))
    print("Số lượng bits cần thiết:", bai_9_bits_count(a))
    
    print("Câu b:")
    bai_9_print_awesome()
    
    print("Câu c:")
    print("Phiên bản Python hiện tại:", bai_9_python_version())
