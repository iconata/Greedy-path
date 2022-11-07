import random


def generate_random_matrix():
    matrix = []
    temp_list = []
    for row in range(height):
        for col in range(width):
            temp_list.append(random.randint(0, 10))
        matrix.append(temp_list)
        temp_list = []

    return matrix


def find_path(matrix):
    for i in matrix:
        print i
    path = [matrix[0][0]]

    curr_col = 0
    result = matrix[0][0]

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


if __name__ == '__main__':
    width = int(input("Please enter width of the matrix: "))
    height = int(input("Please enter height of the matrix: "))

    print find_path(generate_random_matrix())
