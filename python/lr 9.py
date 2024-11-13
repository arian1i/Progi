import numpy as np
# Задаем матрицу 10x10
matrix = np.random.randint(1, 100, (10, 10))

print(matrix)

def is_local_minimum(matrix, i, j):
    # Получаем размер матрицы
    rows, cols = matrix.shape
    
    # Соседние позиции
    neighbors = [
        (i-1, j), (i+1, j), (i, j-1), (i, j+1),
        (i-1, j-1), (i-1, j+1), (i+1, j-1), (i+1, j+1)
    ]
    
    # Проверяем все соседние элементы
    for ni, nj in neighbors:
        if 0 <= ni < rows and 0 <= nj < cols:
            if matrix[i, j] >= matrix[ni, nj]:
                return False
    return True
# Подсчет локальных минимумов
local_minimum_count = 0
for i in range(10):
    for j in range(10):
        if is_local_minimum(matrix, i, j):
            local_minimum_count += 1
# Нахождение суммы модулей элементов выше главной диагонали
sum_above_diagonal = 0
for i in range(10):
    for j in range(i+1, 10):
        sum_above_diagonal += abs(matrix[i, j])
print("Количество локальных минимумов:", local_minimum_count)
print("Сумма модулей элементов выше главной диагонали:", sum_above_diagonal)