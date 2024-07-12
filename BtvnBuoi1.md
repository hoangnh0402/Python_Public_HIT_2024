Câu 1:
- Python là ngôn ngữ lập trình kiểu thông dịch.
- Vì quá trình dịch và thực thi bytecode là hoàn toàn tự động và ẩn.

Câu 2:
a) khi ta khai báo biến thì kiểu dữ liệu của nó sẽ tự động được detect. Các kiểu dữ liệu cơ bản trong Python:
    - Kiểu dữ liệu số: int, double, complex, float
    - Kiểu dữ liệu chuỗi-Ký tự: string, char
    - Kiểu dữ liệu danh sách: list, tuple, range
    - Kiểu dữ liệu tập hợp: set, frozenset
    - Kiểu dữ liệu từ điển: dict
    - Kiểu dữ liệu boolean: bool
    - Kiểu dữ liệu none: NoneType
    - Kiểu dữ liệu nhị phân: bytes, bytearray, memoryview
    - Kiểu dữ liệu hỗn hợp: enum.Enum

b) Các toán tử trong Python
    1. Toán tử Số học (Arithmetic Operators)   

        +: Cộng (ví dụ: a + b)
        -: Trừ (ví dụ: a - b)
        *: Nhân (ví dụ: a * b)
        /: Chia (ví dụ: a / b)
        %: Chia lấy dư (ví dụ: a % b)
        **: Lũy thừa (ví dụ: a ** b)
        //: Chia lấy nguyên (ví dụ: a // b)

    2. Toán tử Gán (Assignment Operators)

        =: Gán giá trị (ví dụ: a = 5)
        +=: Cộng rồi gán (ví dụ: a += 5, tương đương với a = a + 5)
        -=: Trừ rồi gán (ví dụ: a -= 5, tương đương với a = a - 5)
        *=: Nhân rồi gán (ví dụ: a *= 5, tương đương với a = a * 5)
        /=: Chia rồi gán (ví dụ: a /= 5, tương đương với a = a / 5)
        %=: Chia lấy dư rồi gán (ví dụ: a %= 5, tương đương với a = a % 5)
        **=: Lũy thừa rồi gán (ví dụ: a **= 2, tương đương với a = a ** 2)
        //=: Chia lấy nguyên rồi gán (ví dụ: a //= 5, tương đương với a = a // 5)

    3. Toán tử So sánh (Comparison Operators)

        ==: So sánh bằng (ví dụ: a == b)
        !=: So sánh khác (ví dụ: a != b)
        >: Lớn hơn (ví dụ: a > b)
        <: Nhỏ hơn (ví dụ: a < b)
        >=: Lớn hơn hoặc bằng (ví dụ: a >= b)
        <=: Nhỏ hơn hoặc bằng (ví dụ: a <= b)

    4. Toán tử Logic (Logical Operators)

        and: Toán tử và (ví dụ: a and b)
        or: Toán tử hoặc (ví dụ: a or b)
        not: Toán tử phủ định (ví dụ: not a)

    5. Toán tử Nhị phân (Bitwise Operators)
        &: Phép và nhị phân (ví dụ: a & b)
        |: Phép hoặc nhị phân (ví dụ: a | b)
        ^: Phép hoặc loại trừ nhị phân (ví dụ: a ^ b)
        ~: Phép phủ định nhị phân (ví dụ: ~a)
        <<: Dịch trái nhị phân (ví dụ: a << b)
        >>: Dịch phải nhị phân (ví dụ: a >> b)

    6. Toán tử Thành viên (Membership Operators)
        in: Kiểm tra nếu một giá trị có trong một chuỗi hoặc tập hợp (ví dụ: a in b)
        not in: Kiểm tra nếu một giá trị không có trong một chuỗi hoặc tập hợp (ví dụ: a not in b)

    7. Toán tử Nhận diện (Identity Operators)
        is: Kiểm tra nếu hai biến là cùng một đối tượng (ví dụ: a is b)
        is not: Kiểm tra nếu hai biến không là cùng một đối tượng (ví dụ: a is not b)

c) Mệnh đề điều kiện và vòng lặp
    1) Mệnh đề điều kiện
        if: Kiểm tra điều kiện và thực hiện khối lệnh nếu điều kiện đúng.
        elif: Kiểm tra điều kiện khác nếu điều kiện trước đó sai.
        else: Thực hiện khối lệnh nếu tất cả các điều kiện trước đó đều sai.

    2) vòng lặp
        for: Lặp qua một dãy các phần tử, như danh sách, tuple, chuỗi, hoặc dãy số.
        while: Lặp lại khối lệnh cho đến khi điều kiện không còn đúng.
    
    3) Các lệnh Điều khiển Vòng lặp
        break: Dừng vòng lặp ngay lập tức.
        continue: Bỏ qua phần còn lại của vòng lặp hiện tại và chuyển sang lần lặp tiếp theo.
        pass: Không thực hiện hành động gì, thường dùng làm placeholder.

d) Kiểu Dữ Liệu Boolean (bool)
    True: Đại diện cho giá trị đúng.
    False: Đại diện cho giá trị sai.