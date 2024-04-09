import math
# Khởi tạo giá trị ban đầu
x = float(input('Nhập giá trị x(0): '))
alpha = float(input('Nhập giá trị learning rate: '))
dk = float(input('Nhập điều kiện hội tụ: '))
n = int(input('Nhập số lần lặp mong muốn: '))

# Khởi tạo giá trị tối thiểu
min_value = float("inf")
min_x = None

print("\nGiá trị khởi tạo của hàm f(x, y) là:", x**2 + 5*(math.sin(x)))
print("Giá trị của x và y tại điểm tối thiểu lúc khởi tạo là:", x)

# Vòng lặp gradient descent
prev_fx = float("inf")  # Lưu giá trị của hàm ở lần lặp trước
for i in range(1, n): 
    # Tính giá trị hàm số và đạo hàm riêng tại (x, y)
    df_dx = 2*x + 5*(math.cos(x))
    
    # Cập nhật giá trị của x và y theo công thức gradient descent
    x -= alpha * df_dx
    fx = x**2 + 5*(math.sin(x))

    # So sánh với giá trị nhỏ nhất đã tìm thấy trước đó
    if abs(fx) < min_value:
        min_value = fx
        min_x = abs(x)
        save = i

    print("\nGiá trị nhỏ nhất tại lần lặp thứ", i, "của hàm f(x, y) là:", round(fx,5))
    print("Giá trị của x và y tại thời điểm đó là:", round(x,5))

    # Kiểm tra điều kiện dừng
    if (abs(fx) < dk or i == n or round(fx, 5) == round(prev_fx, 5)):
        print("\n***********************************************************************************")
        print("\nĐã đạt điều kiện dừng sau", i, "lần lặp.")
        break
    prev_fx = fx

# In ra kết quả tìm được
print("\n***********************************************************************************")
print("\nGiá trị nhỏ nhất của hàm f(x, y) là:", round(min_value,5))
print("Giá trị của x và y tại lần lặp thứ", save, "là:", round(min_x,5))
print("\n***********************************************************************************")
