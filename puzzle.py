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
				for i in range(len(word)):
					coords.append((row, start + i))
				return coords
			except ValueError:
				continue
