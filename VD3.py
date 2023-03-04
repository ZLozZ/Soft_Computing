
def tinh_f(x, y):
    return float(4*(x**2) - 4*y*x + 4*(y**2))

def cap_nhap(x, y, z):
    x_new = float(x - z*(8*x - 4*y))
    y_new = float(y - z*(8*y - 4*x))
    return x_new, y_new


x = int(input("Nhập giá trị khởi tạo x ban đầu: "))
y = int(input("Nhập giá trị khởi tạo y ban đầu: "))
z =float(input("Nhập tốc độ học: "))
d = float(input("Nhap dieu kien hoi tu: "))

dem = 0
while True:
    if tinh_f(x, y) < d:
        print("Lặp {}, x = {:.4f}, y = {:.4f}, f = {:.4f}".format(dem, x, y, tinh_f(x, y)))
        break
    print("Lặp {}, x = {:.4f}, y = {:.4f}, f = {:.4f}".format(dem, x, y, tinh_f(x, y)))
    x, y = cap_nhap(x, y, z)
    dem+=1

