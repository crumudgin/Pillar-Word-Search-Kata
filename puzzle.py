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

	def __find_word_in_matrix(self, word, strings, coord_func, reversed_string=False):
		"""
		Find the given word in the matrix using the provided strings, string_func, and
		coord_func for modularity.
		"""
		for index, string in enumerate(strings):
			coords = self.__find_word_in_string(word, string)
			if coords != []:
				return [coord_func(coord, index) for coord in coords]

		if reversed_string:
			return []

		return self.__find_word_in_matrix(word[::-1], strings, coord_func, True)[::-1]

	def find_word_horizontal(self, word):
		"""
		Find the first horizontal instance of the provided word
		"""
		def coord_func(coord, row):
			return (row, coord)

		return self.__find_word_in_matrix(word, self.puzzle_matrix, coord_func)

	def find_word_vertical(self, word):
		"""
		Find the first vertical instance of the provided word
		"""
		def coord_func(coord, col):
			return (coord, col)

		string_lst = []
		for col in range(self.cols):
			string_lst.append("".join([self.puzzle_matrix[row][col] for row in range(self.rows)]))

		return self.__find_word_in_matrix(word, string_lst, coord_func)

	def find_word_diagnal_desending(self, word):
		"""
		Find the first diagnal desending instance of the provided word
		"""
		def coord_func(coord, index):
			if index == 0:
				return (coord, coord)
			elif index > self.cols:
				return(index - self.cols + 1, coord)
			return (coord, index)

		string_lst = []

		min_dim = min(self.rows, self.cols)
		for col in range(self.cols):
			string_lst.append("".join([self.puzzle_matrix[i][col + i] for i in range(min_dim)]))
			min_dim -= 1

		min_dim = min(self.rows, self.cols) - 1
		for row in range(1, self.rows):
			string_lst.append("".join([self.puzzle_matrix[row + i][i] for i in range(min_dim)]))
			min_dim -= 1

		return self.__find_word_in_matrix(word, string_lst, coord_func)
