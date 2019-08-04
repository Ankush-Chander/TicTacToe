class TicTacToe():
	"""Two player implementation of TicTacToe"""
	
	def __init__(self, *args,**kwargs):
		self.turn = 0
		self.board = [i+1 for i in range(9)]
		self.remaining_cells = list(range(1,10))
		self.symbols = ["0", "X"]

	def __next__(self):
		val = self.turn

		axis = [self.board[0:3], self.board[3:6], self.board[6:9], self.board[0:7:3], self.board[1:8:3],
		        self.board[2:9:3], self.board[0:9:4], self.board[2:7:2]]

		if any([self._all_equal(line) for line in axis]):
			print("Player " + str(val) + " wins.")
			raise StopIteration
		elif not self.remaining_cells:
			print("Draw")
			raise StopIteration
		else:
			is_valid_move = self.play()
			if is_valid_move:
				self.turn = 1 - self.turn
				self.printBoard()

	def __iter__(self):
		return self

	def printBoard(self):
		row = []
		for index, item in enumerate(self.board):
			row.append(str(item))
			if index%3 == 2:
				print(" | ".join(row))
				row = []

	def _all_equal(self,values):
		return all(v== values[0] for v in values)


	def play(self):
		try:
			try:
				user_sel = input("Player "+ str(self.turn)+": ")
				chosen_cell = int(user_sel)
			except Exception as err:
				raise ValueError

			if chosen_cell in self.remaining_cells:
				self.board[chosen_cell-1] = self.symbols[self.turn]
				self.remaining_cells.remove(chosen_cell)
				return True
			else:
				raise ValueError
		except ValueError as error:
			print("Please enter one of following: " + ", ".join(([str(option) for option in self.remaining_cells])))
			return False


if __name__ == '__main__':
	try:
		ttt = TicTacToe()
		ttt.printBoard()
		while True:
			next(ttt)
	except StopIteration as err:
		print("Game over")
