import numpy as np
import random

def f(x):
    return x*x

def Giaima(x, b):
    Tp = 0
    for i in range(0, b):
        c = x[i]
        Tp += x[i]*(2**i)
    return Tp

def Probability(fitness):
    Q = []
    for i in range(0, len(fitness)):
        Q.append(fitness[i]/sum(fitness))
    return Q

def select_individual(qt, q, n):
    qt_new = []
    circle_ratio = []
    for i in range(0, n):
        if i == 0:
            circle_ratio.append(float(q[i]))
        else:
            circle_ratio.append(float(circle_ratio[i-1]+q[i]))
    for i in range(0, n):
        sel = random.uniform(0, 1)
        for j in range(0, n):
            if j == 0:
                if sel > 0 and sel <= circle_ratio[j]:
                    qt_new.append(qt[j])
                    continue
            else:
                if sel > circle_ratio[j-1] and sel <= (circle_ratio[j]):
                    qt_new.append(qt[j])
    return np.array(qt_new)

def hybrid(qt, b, n):
    point = random.randint(0, (b-1))
    gen1 = 0
    gen2 = 0
    qt_hybrid = []
    if n%2 == 0:
        for i in range(0, int(n/2)):
            index_1 = random.randint(0, (n-1))
            gen1=qt[index_1]
            index_2 = random.randint(0, (n-1))
            while index_1 == index_2:
                index_2 = random.randint(0, (n-1))
            gen2=qt[index_2]
            qt_hybrid1= np.append(gen1[:point], gen2[point:])
            qt_hybrid2= np.append(gen2[:point], gen1[point:])
            qt_hybrid.append(qt_hybrid1)
            qt_hybrid.append(qt_hybrid2)
            # print(index_1)
            # print(index_2)
    else:
        for i in range(0, int((n+1)/2)):
            gen1.append(qt[random.randint(0, (n-1))])
            gen2.append(qt[random.randint(0, (n-1))])
            qt_hybrid.append(gen1[:point] + gen2[point+1:])
    return np.array(qt_hybrid)


def mutation(qt, )

b = int(input("Bạn muốn mã hóa thành mấy bit: "))
n = int(input("Mời bạn chọn số quần thể: "))
qt = np.random.randint(0, 2, size=(n, b))
print("Quần thể sau khi tạo ngẫu nhiên: ")
print(qt)
print("Giải mã:")
pt_Giaima = []
for i in range(0, 4):
    pt_Giaima.append(Giaima(qt[i], b))
    print("{} -----> {}\t\n".format(qt[i], Giaima(qt[i], b)))
print("Tính fitness: ")
fitness = []
total = 0
for i in range(0, 4):
    print("{} -----> {}\t\n".format(pt_Giaima[i], f(pt_Giaima[i])))
    total += f(pt_Giaima[i])
    fitness.append(pt_Giaima[i])
print("Total fitness: ", total)
Q = Probability(fitness)
print("Xác suất: ")
for i in range(0, len(Q)):
    print("{} ------> {}".format(fitness[i], Q[i]))
print("Total xác suất: ", sum(Q))
qt_new = select_individual(qt, Q, n)
print("Quần thể chọn để lai: ")
print(qt_new)
qt_hybrid = hybrid(qt_new, b, n)
print("Quần thể sau khi lai: ")
print(qt_hybrid)


