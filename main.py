
# Test input with matrix 4x4
# with open('test_inputs/test01_4x4', 'r') as f:
#     matrix = [[int(num) for num in line.split(', ')] for line in f]

# Test input with matrix 8x8
# with open('test_inputs/test02_8x8', 'r') as f:
#     matrix = [[int(num) for num in line.split(', ')] for line in f]

# Test input with matrix 30x30
with open('test_inputs/test03_30x30', 'r') as f:
    mat = [[int(num) for num in line.split(', ')] for line in f]

width = len(mat[0])
height = len(mat)


def find_path(matrix):
    global width
    global height

    path = [mat[0][0]]

    curr_col = 0
    result = mat[0][0]

    for row in range(height):
        for col in range(curr_col, width):
            next_element_on_column = col + 1
            next_element_on_row = row + 1

            if next_element_on_row >= height:
                next_element_on_row = height - 1
            if next_element_on_column >= width:
                next_element_on_column = width - 1

            if row == height - 1:
                for items in range(curr_col + 1, width):
                    result += matrix[row][items]
                    path.append(matrix[row][items])
                break

            if matrix[row][next_element_on_column] >= matrix[next_element_on_row][col]:
                result += matrix[row][next_element_on_column]
                path.append(matrix[row][next_element_on_column])
            elif matrix[row][next_element_on_column] < matrix[next_element_on_row][col]:
                result += matrix[next_element_on_row][col]
                curr_col = col
                path.append(matrix[next_element_on_row][col])
                break

    return path


print find_path(mat)
