import random


class GenerateMatrix(object):
    def __init__(self):
        """
        Constructor method to initialize a class instance.
        """
        self.matrix = []

    def print_matrix(self):
        """
        Method that prints the random generated matrix

        :return: None
        """
        for item in self.matrix:
            print item

    def _generate_random_matrix(self):
        """
        Protected method to generate a random matrix.

        :return: matrix as a 2D list
        """
        temp_list = []
        for row in range(height):
            for col in range(width):
                temp_list.append(random.randint(0, 15))
            self.matrix.append(temp_list)
            temp_list = []

        return self.matrix


class MatrixGreedyPath(GenerateMatrix):
    def __init__(self):
        """
        Constructor method to initialize a class instance.
        """
        super(MatrixGreedyPath, self).__init__()
        self.matrix = self._generate_random_matrix()
        self.path = []
        self.curr_col = 0

    @staticmethod
    def check_if_indices_out_of_bounds(elem_on_row, elem_on_col):
        """
        Method to check if the current index is out of bounds. If it is, the function
        corrects it, in order to avoid IndexError.

        :param elem_on_row: current row index
        :param elem_on_col: current column index
        :return: corrected row and column indices
        """
        index_correction = 1
        if elem_on_row >= height:
            elem_on_row = height - index_correction
        if elem_on_col >= width:
            elem_on_col = width - index_correction

        return elem_on_row, elem_on_col

    @staticmethod
    def check_if_at_matrix_border(curr_index):
        """
        Boolean method to check if the current index is at the border.

        :param curr_index: index to check
        :return: True or False
        """
        largest = width if width >= height else height
        index_correction = 1

        return curr_index == largest - index_correction

    def find_path(self):
        """
        Method to go through the greedy path, when comparing two indices. The function looks ahead
        and below the current element in the matrix. If the elements are equal or the element at
        the same row is greater, the path continues right, otherwise breaks the inner for cycle and
        continues from the next row at the current index.

        :return: list containing all the elements in the path
        """
        for row in range(height):
            for col in range(self.curr_col, width):
                next_element_on_column = col + 1
                next_element_on_row = row + 1

                if next_element_on_row >= height or next_element_on_column >= width:
                    next_element_on_row, next_element_on_column = self.check_if_indices_out_of_bounds(
                        next_element_on_row, next_element_on_column
                    )

                if row == height - 1:
                    for items in range(col, width):
                        self.path.append(self.matrix[row][items])
                    break
                else:
                    self.path.append(self.matrix[row][col])

                if self.check_if_at_matrix_border(col):
                    self.curr_col = width - 1
                else:
                    self.curr_col = col

                # move down
                if self.matrix[row][next_element_on_column] < self.matrix[next_element_on_row][col]:
                    break

                # move right
                elif self.matrix[row][next_element_on_column] >= self.matrix[next_element_on_row][col]:
                    continue

        return self.path


if __name__ == '__main__':
    width = int(input("Please enter width of the matrix: "))
    height = int(input("Please enter height of the matrix: "))

    matrix = MatrixGreedyPath()
    matrix.print_matrix()
    print matrix.find_path()
