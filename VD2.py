import math
def tinh_f(x):
    return float(x**2 + 5*math.sin(x))

def cap_nhap(x, z):
    return float(x - z*(x*2 + 5*math.cos(x)))


x = int(input("Nhập giá trị khởi tạo x ban đầu: "))
z =float(input("Nhập tốc độ học: "))
d = float(input("Nhap dieu kien hoi tu: "))

dem = 0
lap = 0
ptu = list()
ptu.append(x)
while True:
    #kiểm tra thỏa điều kiện dừng 1 trong 2
    if round(tinh_f(ptu[dem]), 4) == round(tinh_f(ptu[dem-1]), 4) or abs(tinh_f(x)) < d:
        if lap > 10 or abs(tinh_f(x)) < d:
            print("Lặp {}, x = {:.4f}, f = {:.4f}".format(dem, x, tinh_f(x)))
            break
        else:
            lap+=1
    print("Lặp {}, x = {:.4f}, f = {:.4f}".format(dem, x, tinh_f(x)))
    x = cap_nhap(x, z)
    ptu.append(x)
    dem+=1