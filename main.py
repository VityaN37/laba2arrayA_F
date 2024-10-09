import matplotlib.pyplot as plt
import numpy as np
a = []

print("enter n number 2 to 100")
n = int(input())
print("enter k number 0 to 100")
k = int(input())
print("enter number 1 - 3")
print("1.filling with file")
print("2.filling random")
print("3.generator")
choice = int(input())

# инициализация матрицы а
if choice==1:
    #a = np.loadtxt('data.txt', dtype=int)
    file = open('data.txt', 'r')
    for i in range(n):
        st = file.readline()
        a.append([int(x) for x in st.split()])

    print("A")
    for i in a:
        print(i)

elif choice==2:
    a = np.random.randint(-10, 10, size=(n,n))
    print("A")
    for i in a:
        print(" ".join(f"{value:3d}" for value in i))
elif choice==3:
    a=[[0] * n for _ in range(n)]
    size_a= len(a)
    if n % 2 == 0: #Чётная матрица
        for i in range(n):
            for j in range(n):
                if size_a/2>i and size_a/2>j: #B
                    a[i][j]=1
                elif size_a/2<=i and size_a/2>j: #C
                    a[i][j]=2
                elif size_a/ 2 > i and size_a/2 <= j: #E
                    a[i][j] = 3
                elif size_a/ 2 <= i and size_a/2 <= j: #D
                    a[i][j] = 4
    else: #неЧётная матрица
        for i in range(n):
            for j in range(n):
                if i==(size_a-1)/2 or j==(size_a-1)/2:
                    continue
                elif size_a/2>i and size_a/2>j: #B
                    a[i][j]=1
                elif size_a/2<=i and size_a/2>j: #C
                    a[i][j]=2
                elif size_a/2 <= j: #E
                    a[i][j] = 3
                elif size_a / 2 <= i and size_a/2 <= j: #D
                    a[i][j] = 4

    print("A")
    for i in a:
        print(i)
else:
    print("incorrect input")

f=[[0]*n for _ in range(n)]
for i in range(n):      #копирую a в f
    for j in range(n):
        f[i][j] = a[i][j]
print("F")
#f = np.copy(a)
for i in f:
    print(i)
max_value_of_odd_cows=-11
the_sum_of_odd_rows=0
size = len(a)
if n%2 == 0: #Чётная матрица
    for i in range(n):
        for j in range(n):
            if size/2>i and size/2<=j:
                if j%2 !=0:
                    if max_value_of_odd_cows<f[i][j]:
                        max_value_of_odd_cows=f[i][j]
                if i%2 !=0:
                    the_sum_of_odd_rows+=f[i][j]
else: #неЧётная матрица
    for i in range(n):
        for j in range(n):
            if i == (size - 1) / 2 or j == (size - 1) / 2:
                continue
            else:
                if size / 2 > i and size / 2 <= j:
                    if j % 2 != 0:
                        if max_value_of_odd_cows < f[i][j]:
                            max_value_of_odd_cows = f[i][j]
                    if i % 2 != 0:
                        the_sum_of_odd_rows += f[i][j]

print(f"max_value_of_odd_cows {max_value_of_odd_cows}")
print(f"the_sum_of_odd_rows {the_sum_of_odd_rows}")

size_f=len(f)
array_E=[]
array_B=[]
array_C=[]
iterator_B=0
iterator_E=0
iterator_C=0
amount_diagonal_values_F=0
def_matrix_a=0
#записываем значиния областей в отдельные массивы , смена местами областей
if max_value_of_odd_cows>the_sum_of_odd_rows: #если макс число больше
    if n%2 == 0:  #если чётная матрица
        for i in range(n):
            for j in range(n):
                if size_f/2>i and size/2>j:
                    array_B.append(f[i][j])
        for i in range(n):
            for j in range(n):
                if size_f/2<=i and size/2>j:
                    array_C.append(f[i][j])
        for i in range(n): # смена местами в и с симметрично
            for j in range(n):
                if size_f/2>i and size/2>j:
                    f[i][j]=array_C[iterator_C]
                    iterator_C+=1
        for i in range(n):
            for j in range(n):
                if size_f/2<=i and size/2>j:
                    f[i][j] = array_B[iterator_B]
                    iterator_B += 1

    else: #если не чётная матрица
        for i in range(n):
            for j in range(n):
                if i == (size_f - 1) / 2 or j == (size_f - 1) / 2:
                    continue
                elif size_f/2>i and size/2>j:
                    array_B.append(f[i][j])
        for i in range(n):
            for j in range(n):
                if i == (size_f - 1) / 2 or j == (size_f - 1) / 2:
                    continue
                elif size_f/2<=i and size/2>j:
                    array_C.append(f[i][j])
        for i in range(n):# смена местами в и с симметрично
            for j in range(n):
                if i == (size_f - 1) / 2 or j == (size_f - 1) / 2:
                    continue
                elif size_f/2>i and size/2>j:
                    f[i][j] = array_C[iterator_C]
                    iterator_C += 1
        for i in range(n):
            for j in range(n):
                if i == (size_f - 1) / 2 or j == (size_f - 1) / 2:
                    continue
                elif size_f/2<=i and size/2>j:
                    f[i][j] = array_B[iterator_B]
                    iterator_B += 1

else: #если сумма чисел больше или равна макс
    if n%2 == 0: #если чётная матрица
        for i in range(n):
            for j in range(n):
                if size_f/2>i and size/2>j:
                    array_B.append(f[i][j])
        for i in range(n):
            for j in range(n):
                if size_f/2>i and size/2<=j:
                    array_E.append(f[i][j])

        for i in range(n-1,-1,-1): # смена местами в и е несимметрично
            for j in range(n-1,-1,-1):
                if size_f/2>i and size/2>j:
                    f[i][j] = array_E[iterator_E]
                    iterator_E += 1
        for i in range(n-1,-1,-1): #2
            for j in range(n-1,-1,-1):
                if size_f/2>i and size/2<=j:
                    f[i][j] = array_B[iterator_B]
                    iterator_B += 1
    else:  #если не чётная матрица
        for i in range(n):
            for j in range(n):
                if i == (size_f - 1) / 2 or j == (size_f - 1) / 2:
                    continue
                elif size_f/2>i and size/2>j:
                    array_B.append(f[i][j])
        for i in range(n):
            for j in range(n):
                if i == (size_f - 1) / 2 or j == (size_f - 1) / 2:
                    continue
                elif size_f/2>i and size/2<=j:
                    array_E.append(f[i][j])
        for i in range(n-1,-1,-1): # смена местами в и е несимметрично
            for j in range(n-1,-1,-1):
                if i == (size_f - 1) / 2 or j == (size_f - 1) / 2:
                    continue
                elif size_f/2>i and size/2>j:
                    f[i][j] = array_E[iterator_E]
                    iterator_E += 1
        for i in range(n-1,-1,-1):
            for j in range(n-1,-1,-1):
                if i == (size_f - 1) / 2 or j == (size_f - 1) / 2:
                    continue
                elif size_f/2>i and size/2<=j:
                    f[i][j] = array_B[iterator_B]
                    iterator_B += 1

print(f"array_B {array_B}")
print(f"array_E {array_E}")
print(f"array_C {array_C}")

print("F с заменой областей")
for i in f:
    print(i)
print("A ")
for i in a:
    print(i)
for i in range(n): #определяем сумму диагональных элементов матрицы F
    for j in range(n):
        if i==j or i+j==size_f-1:
            amount_diagonal_values_F+=f[i][j]

print(f"amount_diagonal_values_F {amount_diagonal_values_F}")

def_matrix_a = int(np.linalg.det(a)) #определяем определитель матрицы А

print(f"def_matrix_a {def_matrix_a}")

# 1 выражение если определитель больше чем сумма чисел
if def_matrix_a>amount_diagonal_values_F:
    #1
    power_A = np.linalg.matrix_power(a,-1) # матрица А в -1 степени(А**-1)
    print("А**-1")
    for i in power_A:
        print(i)
    #2
    transposition_A = [[0] * n for _ in range(n)]  #транспонируем матрицу А
    for i in range(n):  # at
        for j in range(n):
            transposition_A[i][j] = a[j][i]
    print("transposition_A")
    for i in transposition_A:
        print(i)
    #3
    multiplication_powerA_At= [[0] * n for _ in range(n)]
    for i in range(n):  # А**-1 * A**t
        for j in range(n):
            sum_multiplication_powerA_At= 0
            for p in range(n):
                sum_multiplication_powerA_At+= power_A[i][p] * transposition_A[p][j]
            multiplication_powerA_At[i][j] = sum_multiplication_powerA_At
    print("multiplication_powerA_At")
    for i in multiplication_powerA_At:
        print(i)
    #4
    power_F = np.linalg.matrix_power(f, 2)  # матрица F в -1 степени(F**-1)
    print("F**-1")
    for i in power_F:
        print(i)
    #5
    for i in range(n):  # k*power_F умножение матрицы на число
        for j in range(n):
            power_F[i][j] *=k
    #6
    difference_powerF_multiplication_powerA_At = [[0] * n for _ in range(n)]
    for i in range(n):  # multiplication_powerA_At -
        for j in range(n):
            difference_powerF_multiplication_powerA_At[i][j] = multiplication_powerA_At[i][j] - power_F[i][j]
    print("difference_powerF_multiplication_powerA_At Конечная матрица")
    for i in difference_powerF_multiplication_powerA_At:
        print(i)
# 2 выражение если определитель меньше или равен  сумме чисел
else:
    #1
    transposition_F = [[0] * n for _ in range(n)]  # транспонируем матрицу F
    for i in range(n):  # at
        for j in range(n):
            transposition_F[i][j] = f[j][i]
    print("transposition_F")
    for i in transposition_F:
        print(i)
    #2
    transposition_A = [[0] * n for _ in range(n)]  # транспонируем матрицу А
    for i in range(n):  # At
        for j in range(n):
            transposition_A[i][j] = a[j][i]
    print("transposition_A")
    for i in transposition_A:
        print(i)

    #3
    G=[[0]*n for _ in range(n)] # нижняя треугольная матрица G
    G= np.tril(a)
    print("G")
    for i in G:
        print(i)

    #4
    difference_G_transposition_F = [[0] * n for _ in range(n)]
    for i in range(n):  # разность между G и транспонированной Ft
        for j in range(n):
            difference_G_transposition_F[i][j] = G[i][j] - transposition_F[i][j]
    print("difference_G_transposition_F")
    for i in difference_G_transposition_F:
        print(i)

    #5
    Sum_At_dif_G_Ft = [[0] * n for _ in range(n)]
    for i in range(n):  # сумма между транспонированной At и G-Ft
        for j in range(n):
            Sum_At_dif_G_Ft[i][j] = transposition_A[i][j]+difference_G_transposition_F[i][j]
    print("Sum_At_dif_G_Ft")
    for i in Sum_At_dif_G_Ft:
        print(i)

    #6
    for i in range(n):  # Sum_At_dif_G_Ft * K
        for j in range(n):
            Sum_At_dif_G_Ft[i][j] *= k

    print("Sum_At_dif_G_Ft Конечная матрица")
    for i in Sum_At_dif_G_Ft:
        print(i)

    # Первый график - простое изображение матрицы (heatmap)
plt.subplot(1, 3, 1)
plt.imshow(f, cmap='viridis')
plt.colorbar()
plt.title('Heatmap')

# Второй график - линиями (line plot)
plt.figure()
plt.subplot(1, 3, 2)
for i in range(size_f):
    plt.plot(a[i,:])
plt.title('Line Plot')

# Третий график - гистограмма значений матрицы
plt.subplot(1, 3, 3)
plt.hist(f.flatten(), bins=3)
plt.title('Histogram')

# Настройка отображения графиков
plt.tight_layout()
plt.show()