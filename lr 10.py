import numpy as np
 
A = np.array([[1, -2, 0],
              [4, 5, -6],
              [-1, 0, 3],
              [7, 8, 9]])
def count_negative_elements_with_zero(matrix):
    count = 0
    for row in matrix:
        if 0 in row:  
            count += sum(1 for x in row if x < 0)  
    return count
def find_saddle_points(matrix):
    saddle_points = []
    for i in range(matrix.shape[0]):
        row_min = np.min(matrix[i])
        for j in range(matrix.shape[1]):
            if matrix[i, j] == row_min:
                col_max = np.max(matrix[:, j])
                if matrix[i, j] == col_max:
                    saddle_points.append((i, j))
    return saddle_points

negative_count = count_negative_elements_with_zero(A)
saddle_points = find_saddle_points(A)

print(f"Количество отрицательных элементов в строках с нулевыми элементами: {negative_count}")
print("Номера строк и столбцов седловых точек (0-индексация):", saddle_points)