class Puzzle():

	def __init__(self, puzzle):
		self.puzzle_matrix = puzzle.replace(", ", "").split("\n")
		self.rows = len(self.puzzle_matrix)
		self.cols = len(self.puzzle_matrix[0])

	def find_word_horizontal(self, word):
		"""
		Find the first horizontal instance of the provided word
		"""
		coords = []
		for row in range(self.rows):
			try:
				start = self.puzzle_matrix[row].index(word)
			except ValueError:
				continue
			for i in range(len(word)):
				coords.append((row, start + i))
			break
		return coords

	def find_word_vertical(self, word):
		"""
		Find the first vertical instance of the provided word
		"""
		coords = []
		col_string = "".join([self.puzzle_matrix[i][0] for i in range(self.rows)])
		start = col_string.index(word)
		for i in range(len(word)):
			coords.append((start + i, 0))
		return coords
