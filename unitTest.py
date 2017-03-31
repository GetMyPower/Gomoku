import unittest
from config import *
from Gomoku import *
from random import *
caseNum = 1
class TestGomoku(unittest.TestCase):
#	def __init__(self):
#	def test_case1(self):
#		ls = []
#		gomoku = Gomoku()
#		for i in range(caseNum):
#			x = randint(0, CHAT_SIZE - 1)
#			y = randint(0, CHAT_SIZE - 1)
##			print(ls)
##			print(gomoku)
#			if not [x, y] in ls:
#				ls.append([x, y])
#				who = randint(0, 1)
#				gomoku.dress(YB if who == 1 else PLAYER, x, y)

#	def test_out_of_range(self):
#		gomoku = Gomoku()
#		ls = []
#		for i in range(caseNum):
#			x = randint(-2 * CHAT_SIZE, 2 * CHAT_SIZE)
#			y = randint(-2 * CHAT_SIZE, 2 * CHAT_SIZE)
#			if not [x, y] in ls:
#				ls.append([x, y])
#				if x >= 0 and y >= 0 and x < CHAT_SIZE and y < CHAT_SIZE:
#					gomoku.dress(YB if randint(0, 1) == 1 else PLAYER, x, y)
#				else:
#					with self.assertRaises(IndexError):
#						gomoku.dress(YB if randint(0, 1) == 1 else PLAYER, x, y)
#						
#	def test_evaluate(self):
#		num = 40
#		gomoku = Gomoku()
#		for i in range(num):
#			x = randint(0, CHAT_SIZE - 1)
#			y = randint(0, CHAT_SIZE - 1)
#			try:
#				gomoku.dress(YB if randint(0, 1) == 0 else PLAYER, y, x)
#			except Exception:
#				pass
#		print()
#		print(gomoku)
#		print(gomoku.Evaluate())
#		print()
#		print(gomoku._Evaluate(YB))
#		print()
#		print(gomoku._Evaluate(PLAYER))
	
#	def test_special_case1(self):
#		gomoku = Gomoku()
#		gomoku.dress(PLAYER, 0, 3)
#		gomoku.dress(PLAYER, 1, 3)
#		gomoku.dress(PLAYER, 2, 3)
#		res = gomoku.Evaluate()
#		print()
#		print(gomoku)
#		print(res)
#		
#	def test_special_case2(self):
#		gomoku = Gomoku()
#		gomoku.dress(PLAYER, 3, 3)
#		gomoku.dress(PLAYER, 1, 3)
#		gomoku.dress(PLAYER, 2, 3)
#		gomoku.dress(YB, 4, 3)
#		res = gomoku.Evaluate()
#		print()
#		print(gomoku)
#		print(res)
##		
#	def test_special_case3(self):
#		gomoku = Gomoku()
#		gomoku.dress(PLAYER, 1, 3)
#		gomoku.dress(PLAYER, 2, 3)
#		gomoku.dress(YB, 4, 3)
#		res = gomoku.Evaluate()
#		print()
#		print(gomoku)
#		print(res)
##		
#	def test_special_case4(self):
#		gomoku = Gomoku()
#		gomoku.dress(PLAYER, 3, 2)
#		gomoku.dress(PLAYER, 4, 2)
#		gomoku.dress(YB, 2, 2)
#		res = gomoku.Evaluate()
#		print()
#		print(gomoku)
#		print(res)
#		
#	def test_special_case5(self):
#		gomoku = Gomoku()
#		gomoku.dress(PLAYER, 0, 2)
#		gomoku.dress(PLAYER, 1, 2)
#		gomoku.dress(YB, 4, 2)
#		res = gomoku.Evaluate()
#		print()
#		print(gomoku)
#		print(res)
##		
#	def test_special_case6(self):
#		gomoku = Gomoku()
#		gomoku.dress(PLAYER, 1, 2)
#		gomoku.dress(PLAYER, 2, 2)
#		gomoku.dress(YB, 4, 2)
#		gomoku.dress(YB, 3, 2)
#		res = gomoku.Evaluate()
#		print()
#		print(gomoku)
#		print(res)
#		
#	def test_special_case7(self):
#		gomoku = Gomoku()
#		gomoku.dress(PLAYER, 0, 2)
#		gomoku.dress(PLAYER, 1, 2)
#		gomoku.dress(YB, 4, 2)
#		gomoku.dress(PLAYER, 3, 2)
#		res = gomoku.Evaluate()
#		print()
#		print(gomoku)
#		print(res)
#	def test_unique(self):
#		gomoku = Gomoku()
#		gomoku.dress(PLAYER, 6, 1)
#		gomoku.dress(PLAYER, 5, 2)
#		gomoku.dress(PLAYER, 4, 3)
#		gomoku.dress(PLAYER, 2, 5)
#		res = gomoku.Evaluate()
#		print()
#		print(gomoku)
#		print(res)
#	def test_special_col_case2(self):
#		gomoku = Gomoku()
#		gomoku.dress(PLAYER, 4, 1)
#		gomoku.dress(PLAYER, 4, 2)
#		gomoku.dress(PLAYER, 4, 0)
#		gomoku.dress(YB, 4, 4)
#		res = gomoku.Evaluate()
#		print()
#		print(gomoku)
#		print(res)

#	def test_special_col_case6(self):
#		gomoku = Gomoku()
#		gomoku.dress(PLAYER, 4, 2)
#		gomoku.dress(PLAYER, 4, 1)
#		gomoku.dress(YB, 4, 3)
#		res = gomoku.Evaluate()
#		print()
#		print(gomoku)
#		print(res)

#	def test_special_slope_case1(self):
#		gomoku = Gomoku()
#		gomoku.dress(PLAYER, 8, 0)
#		gomoku.dress(PLAYER, 7, 1)
#		gomoku.dress(PLAYER, 6, 2)
#		res = gomoku.Evaluate()
#		print()
#		print(gomoku)
#		print(res)

#	def test_special_slope2_case1(self):
#		gomoku = Gomoku()
#		gomoku.dress(PLAYER, 12, 4)
#		gomoku.dress(PLAYER, 11, 5)
#		gomoku.dress(PLAYER, 10, 6)
#		gomoku.dress(YB, 8, 8)
#		res = gomoku.Evaluate()
#		print()
#		print(gomoku)
#		print(res)
#		
#	def test_special_main_slope_case1(self):
#		gomoku = Gomoku()
#		gomoku.dress(PLAYER, 6, 0)
#		gomoku.dress(PLAYER, 7, 1)
#		gomoku.dress(PLAYER, 8, 2)
#		res = gomoku.Evaluate()
#		print()
#		print(gomoku)
#		print(res)
#		
#	def test_special_main_slope_case2(self):
#		gomoku = Gomoku()
#		gomoku.dress(PLAYER, 6, 0)
#		gomoku.dress(PLAYER, 7, 1)
#		gomoku.dress(PLAYER, 8, 2)
#		gomoku.dress(YB, 10, 4)
#		res = gomoku.Evaluate()
#		print()
#		print(gomoku)
#		print(res)

#	def test_special_main_slope_case6(self):
#		gomoku = Gomoku()
#		gomoku.dress(PLAYER, 7, 1)
#		gomoku.dress(PLAYER, 8, 2)
#		gomoku.dress(YB, 9, 3)
#		res = gomoku.Evaluate()
#		print()
#		print(gomoku)
#		print(res)
#		
#	def test_special_main_slope2_case1(self):
#		gomoku = Gomoku()
#		gomoku.dress(PLAYER, 0, 7)
#		gomoku.dress(PLAYER, 1, 8)
#		gomoku.dress(PLAYER, 2, 9)
#		res = gomoku.Evaluate()
#		print()
#		print(gomoku)
#		print(res)
#		
#	def test_special_main_slope2_case6(self):
#		gomoku = Gomoku()
#		gomoku.dress(PLAYER, 1, 8)
#		gomoku.dress(PLAYER, 2, 9)
#		gomoku.dress(YB, 3, 10)
#		res = gomoku.Evaluate()
#		print()
#		print(gomoku)
#		print(res)

#	def test_special_main_slope2_case4(self):
#		gomoku = Gomoku()
#		gomoku.dress(PLAYER, 1, 8)
#		gomoku.dress(PLAYER, 2, 9)
#		gomoku.dress(YB, 0, 7)
#		res = gomoku.Evaluate()
#		print()
#		print(gomoku)
#		print(res)
#	def test_mayby_bug(self):
#		gomoku = Gomoku()
#		gomoku.dress(PLAYER, 4, 0)
#		gomoku.dress(PLAYER, 5, 0)
#		gomoku.dress(YB, 5, 1)
#		gomoku.dress(PLAYER, 7, 1)
#		ret = gomoku.Evaluate()
#		print(gomoku)
#		print(ret)

	def test_release(self):
		gomoku = Gomoku()
		gomoku.Evaluate()
		
		
		
		
		
if __name__ == '__main__':
	unittest.main()
