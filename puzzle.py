class Puzzle():

	def __init__(self, puzzle):
		self.puzzle_matrix = puzzle.replace(", ", "").split("\n")
		self.rows = len(self.puzzle_matrix)
		self.cols = len(self.puzzle_matrix[0])

	def __find_word_in_string(self, word, string):
		start = string.find(word)
		if start > -1:
			return (start + i for i in range(len(word)))
		return []

	def __find_word_in_matrix(self, word, matrix_dim, string_func, coord_func):
		"""
		Find the given word in the matrix using the provided matrix_dim, string_func, and
		coord_func for modularity.
		"""
		for index in range(matrix_dim):
			string = string_func(index)
			coords = self.__find_word_in_string(word, string)
			if coords != []:
				return [coord_func(coord, index) for coord in coords]
		return []

	def find_word_horizontal(self, word):
		"""
		Find the first horizontal instance of the provided word
		"""
		def string_func(row):
			return self.puzzle_matrix[row]

		def coord_func(coord, row):
			return (row, coord)

		coords = self.__find_word_in_matrix(word, self.rows, string_func, coord_func)
		if coords == []:
			coords = self.__find_word_in_matrix(word[::-1], self.rows, string_func, coord_func)[::-1]
		return coords

	def find_word_vertical(self, word):
		"""
		Find the first vertical instance of the provided word
		"""
		def string_func(col):
			return "".join([self.puzzle_matrix[i][col] for i in range(self.rows)])

		def coord_func(coord, col):
			return (coord, col)

		coords = self.__find_word_in_matrix(word, self.cols, string_func, coord_func)
		if coords == []:
			coords = self.__find_word_in_matrix(word[::-1], self.cols, string_func, coord_func)[::-1]
		return coords