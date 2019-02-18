class Puzzle():

    def __init__(self, puzzle):
        self.matrix = puzzle.replace(", ", "").split("\n")
        self.rows = len(self.matrix)
        self.cols = len(self.matrix[0])

    def __find_word_in_matrix(self, word, strings, reversed_string=False):
        """
        Find the given word in the matrix using the provided strings.
        Paramaters: word            - the substring the function is atempting to locate
                    strings         - the strings the function should search
                    reversed_string - the boolean that determins if the function should
                                      attempt to find a solution with the string reveresd
        Returns: the coordinates of the word within the strings
        """
        for index, string in enumerate(strings):
            start = string.find(word)
            if start > -1:
                return [(start + i, index) for i in range(len(word))]

        if reversed_string:
            return []

        return self.__find_word_in_matrix(word[::-1], strings, True)[::-1]

    def __word_to_polar_coords(self, word, matrix):
        """
        Logic for finding a substring in the diagnals of a matrix
        Paramaters: word          - the substring the function is atempting to locate
                    matrix        - the matrix the function will search
                    coord_func    - a function containing the logic for
                                      determaning the coordinates
        Returns: the coordinates of the provided word within the desending diagnals
                 of the matrix
        """
        string_lst = [[] for i in range(self.rows + self.cols - 1)]

        for x in range(self.rows):
            for y in range(self.cols):
                string_lst[y + x].append(matrix[x][y])
        string_lst = list(map("".join, string_lst))

        return self.__find_word_in_matrix(word, string_lst)

    def __polar_coords_to_cartesian_coords(self, diagnal_coordinate, desending):
        """
        BAD NEED TO REFACTOR
        """
        index, diagnal = diagnal_coordinate
        col = 0 if desending else self.cols - 1
        row = diagnal - self.cols + 1
        if diagnal < self.cols:
            col = (self.cols - diagnal - 1) if desending else diagnal
            row = 0
        col = (col + index) if desending else (col - index)
        row += index
        return (row, col)

    def __add_coordinates(self, current_coordinates, word, func):
        """
        Executes the provided func if the word has not been found yet.
        Paramaters: current_coordinates - a list containing the coordinates of the word if found
                    word                - the substring the function is atempting to locate
                    func                - the function to execute and return if the word has not
                                          been found
        Returns: The output of the provided func
        """
        if current_coordinates == []:
            return func(word)
        return current_coordinates

    def find_word(self, word):
        """
        Find an occurence of the given word if it exists within the puzzle matrix
        Paramaters: word - the substring the function is atempting to locate
        Returnes: the coordinaters of the word within the puzzle matrix
        """
        coordinates = self.__add_coordinates([], word, self.find_word_horizontal)
        coordinates = self.__add_coordinates(coordinates, word, self.find_word_vertical)
        coordinates = self.__add_coordinates(coordinates, word, self.find_word_diagnal_desending)
        coordinates = self.__add_coordinates(coordinates, word, self.find_word_diagnal_assending)
        return coordinates

    def find_word_horizontal(self, word):
        """
        Find the first horizontal instance of the provided word
        Paramaters: word - the substring the function is atempting to locate
        Returnes: the coordinates of the word if they exist
        """
        coordinates = self.__find_word_in_matrix(word, self.matrix)
        return [(row, col) for col, row in coordinates]

    def find_word_vertical(self, word):
        """
        Find the first vertical instance of the provided word
        Paramaters: word - the substring the function is atempting to locate
        Returnes: the coordinates of the word if they exist
        """
        string_lst = []
        for col in range(self.cols):
            string_lst.append("".join([self.matrix[row][col] for row in range(self.rows)]))

        coordinates = self.__find_word_in_matrix(word, string_lst)
        return [(row, col) for row, col in coordinates]

    def find_word_diagnal_desending(self, word):
        """
        Find the first diagnal desending instance of the provided word
        Paramaters: word - the substring the function is atempting to locate
        Returnes: the coordinates of the word if they exist
        """
        reversed_matrix = [i[::-1] for i in self.matrix]
        diagnal_coordinates = self.__word_to_polar_coords(word, reversed_matrix)
        return [self.__polar_coords_to_cartesian_coords(i, True) for i in diagnal_coordinates]

    def find_word_diagnal_assending(self, word):
        """
        Find the first diagnal assending instance of the provided word
        Paramaters: word - the substring the function is atempting to locate
        Returnes: the coordinates of the word if they exist
        """
        diagnal_coordinates = self.__word_to_polar_coords(word, self.matrix)
        return [self.__polar_coords_to_cartesian_coords(i, False) for i in diagnal_coordinates]
