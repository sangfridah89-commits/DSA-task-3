
matrix = [
    [0, 0, 3],
    [0, 0, 0],
    [4, 0, 5]
]

sparse = []

rows = len(matrix)
columns = len(matrix[0])

for i in range(rows):
    for j in range(columns):
        if matrix[i][j] != 0:
            sparse.append([i, j, matrix[i][j]])

print("Original Matrix:")

for row in matrix:
    print(row)

print("\nSparse Matrix Representation:")
print("Row Column Value")

for item in sparse:
    print(item[0], "  ", item[1], "   ", item[2])

print("\nNumber of non-zero elements:", len(sparse))
