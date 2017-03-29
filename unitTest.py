import unittest
from config import *
from Gomoku import *
from random import *
caseNum = 1
class TestGomoku(unittest.TestCase):
#	def __init__(self):
	def test_case1(self):
		ls = []
		gomoku = Gomoku()
		for i in range(caseNum):
			x = randint(0, CHAT_SIZE - 1)
			y = randint(0, CHAT_SIZE - 1)
#			print(ls)
#			print(gomoku)
			if not [x, y] in ls:
				ls.append([x, y])
				who = randint(0, 1)
				gomoku.dress(YB if who == 1 else PLAYER, x, y)

	def test_out_of_range(self):
		gomoku = Gomoku()
		ls = []
		for i in range(caseNum):
			x = randint(-2 * CHAT_SIZE, 2 * CHAT_SIZE)
			y = randint(-2 * CHAT_SIZE, 2 * CHAT_SIZE)
			if not [x, y] in ls:
				ls.append([x, y])
				if x >= 0 and y >= 0 and x < CHAT_SIZE and y < CHAT_SIZE:
					gomoku.dress(YB if randint(0, 1) == 1 else PLAYER, x, y)
				else:
					with self.assertRaises(IndexError):
						gomoku.dress(YB if randint(0, 1) == 1 else PLAYER, x, y)
						
#	def test_evaluate(self):
#		num = 30
#		gomoku = Gomoku()
#		for i in range(num):
#			x = randint(0, CHAT_SIZE - 1)
#			y = randint(0, CHAT_SIZE - 1)
#			try:
#				gomoku.dress(YB if randint(0, 1) == 0 else PLAYER, y, x)
#			except Exception:
#				pass
#		res = gomoku.Evaluate()
#		print()
#		print(gomoku)
#		print(res)
	
	def test_unique(self):
		gomoku = Gomoku()
		gomoku.dress(PLAYER, 10, 2)
		gomoku.dress(PLAYER, 10, 3)
		gomoku.dress(PLAYER, 9, 5)
		gomoku.dress(PLAYER, 8, 6)
		res = gomoku.Evaluate()
		print()
		print(gomoku)
		print(res)

if __name__ == '__main__':
	unittest.main()
