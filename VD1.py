
def tinh_f(x, y):
    return float(x**2 + y**2)

def cap_nhap(x, y, z):
    x_new = float(x - z*2*x)
    y_new = float(y - z*2*y)
    return x_new, y_new


x = int(input("Nhập giá trị khởi tạo x ban đầu: "))
y = int(input("Nhập giá trị khởi tạo y ban đầu: "))
z =float(input("Nhập tốc độ học: "))
d = float(input("Nhap dieu kien hoi tu: "))

count = 0
while True:
    if tinh_f(x, y) < d:
        print("Lặp {}, x = {:.4f}, y = {:.4f}, f = {:.4f}".format(count, x, y, tinh_f(x, y)))
        break
    print("Lặp {}, x = {:.4f}, y = {:.4f}, f = {:.4f}".format(count, x, y, tinh_f(x, y)))
    x, y = cap_nhap(x, y, z)
    count+=1

