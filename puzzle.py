class Puzzle():

    def __init__(self, puzzle):
        self.puzzle_matrix = puzzle.replace(", ", "").split("\n")
        self.rows = len(self.puzzle_matrix)
        self.cols = len(self.puzzle_matrix[0])

    def __find_word_in_matrix(self, word, strings, coord_func, reversed_string=False):
        """
        Find the given word in the matrix using the provided strings, string_func, and
        coord_func for modularity.
        Paramaters: word            - the substring the function is atempting to locate
                    strings         - the strings the function should search
                    coord_func      - a function containing the logic for
                                      determaning the coordinates
                    reversed_string - the boolean that determins if the function should
                                      attempt to find a solution with the string reveresd
        Returns: the coordinates of the word within the strings
        """
        for index, string in enumerate(strings):
            start = string.find(word)
            if start > -1:
                return [coord_func(start + i, index) for i in range(len(word))]

        if reversed_string:
            return []

        return self.__find_word_in_matrix(word[::-1], strings, coord_func, True)[::-1]

    def find_word_horizontal(self, word):
        """
        Find the first horizontal instance of the provided word
        Paramaters: word - the substring the function is atempting to locate
        Returnes: the coordinates of the word if they exist
        """
        def coord_func(coord, row):
            return (row, coord)

        return self.__find_word_in_matrix(word, self.puzzle_matrix, coord_func)

    def find_word_vertical(self, word):
        """
        Find the first vertical instance of the provided word
        Paramaters: word - the substring the function is atempting to locate
        Returnes: the coordinates of the word if they exist
        """
        def coord_func(coord, col):
            return (coord, col)

        string_lst = []
        for col in range(self.cols):
            string_lst.append("".join([self.puzzle_matrix[row][col] for row in range(self.rows)]))

        return self.__find_word_in_matrix(word, string_lst, coord_func)

    def __find_word_diagnal(self, word, puzzle_matrix, coord_func):
        """
        Logic for finding a substring in the diagnals of a matrix
        Paramaters: word          - the substring the function is atempting to locate
                    puzzle_matrix - the matrix the function will search
                    coord_func    - a function containing the logic for
                                      determaning the coordinates
        Returns: the coordinates of the provided word within the desending diagnals
                 of the puzzle_matrix
        """
        string_lst = []

        # create list of strings above (and including) the desending diagnal
        min_dim = min(self.rows, self.cols)
        for col in range(self.cols):
            string_lst.append("".join([puzzle_matrix[i][col + i] for i in range(min_dim)]))
            min_dim -= 1

        # create list of strings below the desending diagnal
        min_dim = min(self.rows, self.cols) - 1
        for row in range(1, self.rows):
            string_lst.append("".join([puzzle_matrix[row + i][i] for i in range(min_dim)]))
            min_dim -= 1

        return self.__find_word_in_matrix(word, string_lst, coord_func)

    def find_word_diagnal_desending(self, word):
        """
        Find the first diagnal desending instance of the provided word
        Paramaters: word - the substring the function is atempting to locate
        Returnes: the coordinates of the word if they exist
        """
        def coord_func(coord, index):
            if index == 0:
                return (coord, coord)
            elif index > self.cols:
                return (index - self.cols + 1, coord)
            return (coord, index)

        return self.__find_word_diagnal(word, self.puzzle_matrix, coord_func)

    def find_word_diagnal_assending(self, word):
        """
        Find the first diagnal assending instance of the provided word
        Paramaters: word - the substring the function is atempting to locate
        Returnes: the coordinates of the word if they exist
        """
        def coord_func(coord, index):
            if index == 0:
                return (self.rows - 1 - coord, coord)
            elif index > self.rows:
                index -= self.cols - 1
                return (self.cols - 1 - index, coord)
            return (self.cols - 1 - coord, index)

        reversed_matrix = self.puzzle_matrix[::-1]
        return self.__find_word_diagnal(word, reversed_matrix, coord_func)
