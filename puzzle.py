class Puzzle():

	def __init__(self, puzzle):
		self.puzzle = puzzle.replace(", ", "").split("\n")
		self.rows = len(self.puzzle)
		self.cols = len(self.puzzle[0])

	def find_word_horizontal(self, word):
		coords = []
		start = self.puzzle[0].index(word)
		for i in range(len(word)):
			coords.append((0, start + i))
		return coords