from config import *
import heapq
import re
from Group import *
import copy

def MyQuit():
	s = ''
	while(s != 'q'):
		s = input('输入q结束对战\n>>> ')

def findMax(table):
	Max = table[0][0]
	for i in range(CHAT_SIZE):
		for j in range(CHAT_SIZE):
			if table[i][j] > Max:
				Max = table[i][j]
	return Max
#TODO:
def EvaluateRecurse(g, x, y, deep):
#	print(g, x, y, deep)
	gomoku = copy.deepcopy(g)
	who = YB if deep % 2 == 0 else PLAYER
	gomoku.dress(who, x, y)
	
	ls = gomoku.Evaluate()
	if gomoku.YBHasWin == True:
		return YB_WIN_INT
	if gomoku.PLAYERHasWin == True:
		return YB_LOSE_INT

			
	if (deep == 0):
		s = gomoku._Evaluate(YB)
		p = gomoku._Evaluate(PLAYER)
		return findMax(s) - findMax(p)
	
	if deep % 2 == 0:
		Min = MAX_INT
		for play in ls:
			tmp = EvaluateRecurse(gomoku, play[1], play[2], deep - 1)
#			print(gomoku, play[1], play[2], tmp)
			if tmp < Min:
				Min = tmp
		return Min
	elif deep % 2 == 1:
		Max = MIN_INT
		for play in ls:
			tmp = EvaluateRecurse(gomoku, play[1], play[2], deep - 1)
#			print(gomoku, play[1], play[2], tmp)
			if tmp > Max:
				Max = tmp
		return Max


def MatchContinueDress(who, s):
	ret = []
	pattern = MATCH_YB_CONTINUE_DRESS if who == YB else MATCH_PLAYER_CONTINUE_DRESS
	for i in re.finditer(pattern, s):
		group = Group(i.span()[0], i.span()[1] - 1)
#		print(group)
		ret.append(group)
	ret.sort()
	return ret

def ParseIntPair(s):
	ls = s.split(' ')
	ret = []
	if not re.match(r'\w \w$', s):
		raise SyntaxError('Syntax Error')
	
	try:
		for num in ls:
			ret.append(INDEX_LIST.index(num))
	except Exception:
		raise IndexError('Position Not Valid')
	return tuple(ret)

def SideCorrection(table):
#	cor = 1 / (EvalUnit ** 0.5)
#	for x in range(CHAT_SIZE):
#		table[x][0] *= cor
#		table[x][CHAT_SIZE - 1] *= cor
#	for y in range(CHAT_SIZE):
#		table[0][y] *= cor
#		table[CHAT_SIZE - 1][y] *= cor
	pass

#TODO:注意双向！要写全！
def MatchCaseCorrection(self, who, _str):
#	''' 
#	1 #XXX__ __平均为 **2.5
#	2 #XXX_# _衰减 / unit
#	4 #XX_ _ _ left _ down to / (unit ** 0.5)
#	5 #XX__# left _ 衰减为/unit
#	6 #XX_#  _ down to /unit
#	7 #XX_X# _ down to / (unit)
#	
#	8 _XXXX_
#	9 #XXXX_
#	
#	w_yb XXXXX
#	w_player XXXXX
#	12 _XXX_
#	13_XXXX
#	'''
	op = YB if who == PLAYER else PLAYER
#	s1 = op + who * 3 + EMPTY * 2
	s2 = op + who * 3 + EMPTY + op
#	s3 = op + EMPTY + who * 2 + EMPTY + op
#	s4 = op + who * 2 + EMPTY * 3
#	s5 = op + who * 2 + EMPTY * 2 + op
#	s6 = op + who * 2 + EMPTY + op
	s7 = op + who * 2 + EMPTY + who + op
#	
#	s8 = EMPTY + YB * 4 + EMPTY
#	s9 = PLAYER + YB * 4 + EMPTY
#	s10 = EMPTY + PLAYER * 4 + EMPTY
#	s11 = YB + PLAYER * 4 + EMPTY
	s12 = EMPTY + 3 * who + EMPTY
	s13 = EMPTY + 4 * who
	s_w_yb = 5 * YB
	s_w_player = 5 * PLAYER
#	
	s = op + _str + op
	ret = []
#	for i in re.finditer(s1, s):
#		beg = i.span()[0]
#		pos1 = beg + 4
#		pos2 = beg + 5
#		c1 = Correction(pos1 - 1, EvalUnit ** -0.5)
#		c2 = Correction(pos2 - 1, EvalUnit ** 0.5)
#		ret.append(c1)
#		ret.append(c2)
##		print('case1')
	for i in re.finditer(s2, s):
		beg = i.span()[0]
		pos = beg + 4
		ret.append(Correction(pos - 1, 1 / (EvalUnit**2)))
#		print('case 2')
#	for i in re.finditer(s4, s):
#		beg = i.span()[0]
#		pos1 = beg + 3
#		pos2 = beg + 4
#		ret.append(Correction(pos1 - 1, 1 / (EvalUnit**0.5)))
#		ret.append(Correction(pos2 - 1, EvalUnit ** 0.5))
##		print('case4')
#	for i in re.finditer(s5, s):
#		beg = i.span()[0]
#		pos = beg + 3
#		ret.append(Correction(pos - 1, 1 / (EvalUnit**0.5)))
##		print('case5')
#	for i in re.finditer(s6, s):
#		beg = i.span()[0]
#		pos = beg + 3
#		ret.append(Correction(pos - 1, 1 / EvalUnit))
##		print('case6')
	for i in re.finditer(s7, s):
		beg = i.span()[0]
		pos = beg + 3
		ret.append(Correction(pos - 1, 1 / (EvalUnit**2)))
##		print('case7')
#		
#	if who == YB:
#		for i in re.finditer(s8, s):
#			pos1 = i.span()[0]
#			#a very most big number
#			#8 是对称的
#			ret.append(Correction(pos1 - 1, EvalUnit ** 4))
##			print('about to win 1')
#		for i in re.finditer(s9, s):
#			pos = i.span()[0] + 5
#			ret.append(Correction(pos - 1, EvalUnit ** 4))
##			print('about to win 2')
#		
#	if who == PLAYER:
#		for i in re.finditer(s10, s):
#			pos1 = i.span()[0]
#			#a rather big number
#			#10是对称的
#			ret.append(Correction(pos1 - 1, EvalUnit ** 2))
##			print('about to win 3')
#		for i in re.finditer(s11, s):
#			pos = i.span()[0] + 5
#			ret.append(Correction(pos - 1, EvalUnit ** 2))
##			print('about to win 4')
	for i in re.finditer(s12, s):
		pos = i.span()[0]
		ret.append(Correction(pos - 1, EvalUnit ** 0.5))
#		print('_XXX_')
	for i in re.finditer(s13, s):
		pos = i.span()[0]
		ret.append(Correction(pos - 1, EvalUnit**2))
	if who == YB:
		for i in re.finditer(s_w_yb, s):
			self.YBHasWin = True
	if who == PLAYER:
		for i in re.finditer(s_w_player, s):
			self.PLAYERHasWin = True
	return ret


def SumUp(a, b):
	ret = [[0 for x in range(CHAT_SIZE)] for x in range(CHAT_SIZE)]
	for x in range(CHAT_SIZE):
		for y in range(CHAT_SIZE):
			lhs = 0 if a[x][y] == 1 else a[x][y]
			rhs = 0 if b[x][y] == 1 else b[x][y]
			ret[x][y] += lhs + rhs
	return ret

def xScaleTable(x, table):
	for i in range(CHAT_SIZE):
		for j in range(CHAT_SIZE):
			table[i][j] *= x
	
class Gomoku(object):
	def _init_square(self):
		self.YBHasWin = False
		self.PLAYERHasWin = False
		self.last_x = -1
		self.last_y = -1
		self.square = []
		for i in range(CHAT_SIZE):
			tmp = [EMPTY for x in range(CHAT_SIZE)]
			self.square.append(tmp)				
			
	def __init__(self):
		self._init_square()		
	
	def _checkIndex(self, x, y):
		if x < 0 or x >= CHAT_SIZE:
			raise IndexError('x index out of range')
		elif y < 0 or y >= CHAT_SIZE:
			raise IndexError('y index out of range')
	
	def _checkPerson(self, who):
		if who != YB and who != PLAYER and who != EMPTY:
			raise ValueError('not exist this person')
	
	def _checkEmpty(self, x, y):
		if self.square[x][y] != EMPTY:
			raise RuntimeError('position({}, {}) has been dressed'.format(x, y))
			
	
	def __str__(self):
		ret = '  '
		for x in range(CHAT_SIZE):
			ret += INDEX_LIST[x] + ' '
		ret += '\n'
		
		for y in range(CHAT_SIZE):
			ret += INDEX_LIST[y] + ' '
			for x in range(CHAT_SIZE):
				ret += ('!' if x == self.last_x and y == self.last_y else self.square[x][y]) + ' '
			ret += '\n'
		return ret
	
	def _isDress(self, who, x, y):
		self._checkIndex(x, y)
		self._checkPerson(who)
		return self.square[x][y] == who
	
	def dress(self, who, x, y):
		self._checkIndex(x, y)
		self._checkPerson(who)
		self._checkEmpty(x, y)
		self.square[x][y] = who
	
	def _EvaluateRow(self, who):
		''' 
		#XXX__ __平均为 **2.5
		#XXX_# _衰减 / unit
		#_XX_# _ _衰减 /unit 
		#XX_ _ _ left _ down to /unit
		#XX__# left _ 衰减为/unit
		#XX_#  _ down to /unit
		#XX_X# _ down to / (unit)During handling of the above exception
		'''
		table = [[1 for x in range(CHAT_SIZE)] for x in range(CHAT_SIZE)]
		op = YB if who == PLAYER else PLAYER
		for y in range(CHAT_SIZE):
			row_str = ''
			for x in range(CHAT_SIZE):
				row_str += self.square[x][y]
			group_list = MatchContinueDress(who, row_str)
			for group in group_list:
				b = group.begin - 1
				while b >= 0 and not self._isDress(op, b, y):
					value = EvalUnit ** (group.length - (group.begin - b) + 2)
					if value <= 1: break
#					print(b, y, value)
					table[b][y] *= value
					b -= 1
				b = group.end + 1
				while b < CHAT_SIZE and not self._isDress(op, b, y):
					value = EvalUnit ** (group.length - (b - group.end) + 2)
					if value <= 1:break
#					print(b, y, value)
					table[b][y] *= value
					b += 1
			
			correction = MatchCaseCorrection(self, who, row_str)
			for item in correction:
				table[item.position][y] *= item.value
			
			correction = MatchCaseCorrection(self, who, row_str[::-1])
			for item in correction:
				table[CHAT_SIZE - 1 - item.position][y] *= item.value
		return table
				
	def _EvaluateColumn(self, who):
		table = [[1 for x in range(CHAT_SIZE)] for x in range(CHAT_SIZE)]
		op = YB if who == PLAYER else PLAYER
		for col in range(CHAT_SIZE):
			col_str = ''.join(self.square[col])
#			print('::', col_str)
			group_list = MatchContinueDress(who, col_str)
			for group in group_list:
				b = group.begin - 1
				while b >= 0 and not self._isDress(op, col, b):
					value = EvalUnit ** (group.length - (group.begin - b) + 2)
					if value <= 1: break
#					print(col, b, value)
					table[col][b] *= value
					b -= 1
				b = group.end + 1
				while b < CHAT_SIZE and not self._isDress(op, col, b):
					value = EvalUnit ** (group.length - (b - group.end) + 2)
					if value <= 1:break
#					print(col, b, value)
					table[col][b] *= value
					b += 1
					
#			print(':', col_str)
			correction = MatchCaseCorrection(self, who, col_str)
			for item in correction:
				table[col][item.position] *= item.value
			
			correction = MatchCaseCorrection(self, who, col_str[::-1])
			for item in correction:
				table[col][CHAT_SIZE - 1 - item.position] *= item.value
		return table
	
	def _EvaluateSlope(self, who):
		'''
		对斜线上的连棋求值
		对每条斜线，按从右上到左下的顺序遍历
		长度不足5的斜线一定无法连成5子，直接忽略
		副对角线将矩形分成两份，两个for循环依次对两份求值
		'''
		table = [[1 for x in range(CHAT_SIZE)] for x in range(CHAT_SIZE)]
		op = YB if who == PLAYER else PLAYER
		for start_x in range(5 - 1, CHAT_SIZE):
			slope_str = ''
			x = start_x
			y = 0
			while x >= 0:
				slope_str += self.square[x][y]
				x -= 1
				y += 1
#			if (start_x == CHAT_SIZE - 1) : print('here',slope_str)
			group_list = MatchContinueDress(who, slope_str)
			for group in group_list:
				bx = start_x - group.begin + 1
				by = 0 + group.begin - 1
				while by >= 0 and not self._isDress(op, bx, by):
					value = EvalUnit ** (group.length - (bx - start_x + group.begin) + 2)
					if value <= 1: break
#					print(1, bx, by, value)
					table[bx][by] *= value
					bx += 1
					by -= 1
				bx = start_x - group.end - 1
				by = 0 + group.end + 1
				while bx >= 0 and not self._isDress(op, bx, by):
					value = EvalUnit ** (group.length - (start_x - group.end - bx) + 2)
					if value <= 1:break
					table[bx][by] *= value
					bx -= 1
					by += 1
#			print(':', slope_str)
			correction = MatchCaseCorrection(self, who, slope_str)
			for item in correction:
				table[start_x - item.position][0 + item.position] *= item.value
			
			correction = MatchCaseCorrection(self, who, slope_str[::-1])
			for item in correction:
				table[item.position][start_x - item.position] *= item.value
					
		'''part two'''
		for start_y in range(1, CHAT_SIZE - 5 + 1):
			slope_str = ''
			y = start_y
			x = CHAT_SIZE - 1
			while x >= 0 and y < CHAT_SIZE:
				slope_str += self.square[x][y]
				x -= 1
				y += 1
#			if (start_x == CHAT_SIZE - 1) : print('here',slope_str)
			group_list = MatchContinueDress(who, slope_str)
			for group in group_list:
#				print(group)
				bx = CHAT_SIZE - 1 - group.begin + 1
				by = start_y + group.begin - 1
				while by >= 0 and bx < CHAT_SIZE and not self._isDress(op, bx, by):
					value = EvalUnit ** (group.length - (start_y + group.begin - by) + 2)
					if value <= 1: break
#					print(bx, by, value)
					table[bx][by] *= value
					bx += 1
					by -= 1
				bx = CHAT_SIZE - 1 - group.end - 1
				by = start_y + group.end + 1
				while bx >= 0 and by < CHAT_SIZE and not self._isDress(op, bx, by):
					value = EvalUnit ** (group.length - (by - start_y - group.end) + 2)
					if value <= 1:break
#					print(bx, by, value)
					table[bx][by] *= value
					bx -= 1
					by += 1
					
			correction = MatchCaseCorrection(self, who, slope_str)		
			for item in correction:
				table[CHAT_SIZE - 1 - item.position][start_y + item.position] *= item.value
			
			correction = MatchCaseCorrection(self, who, slope_str[::-1])
			for item in correction:
				table[start_y + item.position][CHAT_SIZE - 1 - item.position] *= item.value
		#TODO:start here
		return table
	
	def _EvaluateMainSlope(self, who):
		table = [[1 for x in range(CHAT_SIZE)] for x in range(CHAT_SIZE)]
		op = YB if who == PLAYER else PLAYER
		for start_x in range(0, CHAT_SIZE - 5 + 1):
			slope_str = ''
			x = start_x
			y = 0
			while x < CHAT_SIZE:
				slope_str += self.square[x][y]
				x += 1
				y += 1
#			if (start_x == CHAT_SIZE - 1) : print('here',slope_str)
			group_list = MatchContinueDress(who, slope_str)
			for group in group_list:
				bx = start_x + group.begin - 1
				by = 0 + group.begin - 1
				while by >= 0 and bx >= 0 and not self._isDress(op, bx, by):
					value = EvalUnit ** (group.length - (start_x + group.begin - bx) + 2)
					if value <= 1: break
#					print(bx, by, value)
					table[bx][by] *= value
					bx -= 1
					by -= 1
				bx = start_x + group.end + 1
				by = 0 + group.end + 1
				while bx < CHAT_SIZE and not self._isDress(op, bx, by):
					value = EvalUnit ** (group.length - (bx - start_x - group.end) + 2)
					if value <= 1:break
#					print(bx, by, value)
					table[bx][by] *= value
					bx += 1
					by += 1
					
			correction = MatchCaseCorrection(self, who, slope_str)
			for item in correction:
				table[start_x + item.position][0 + item.position] *= item.value
			
			correction = MatchCaseCorrection(self, who, slope_str[::-1])
			for item in correction:
				table[CHAT_SIZE - 1 - item.position][CHAT_SIZE - 1 - start_x - item.position] *= item.value
					
		'''part two'''
		for start_y in range(1, CHAT_SIZE - 5 + 1):
			slope_str = ''
			y = start_y
			x = 0
			while x >= 0 and y < CHAT_SIZE:
				slope_str += self.square[x][y]
				x += 1
				y += 1
#			if (start_x == CHAT_SIZE - 1) : print('here',slope_str)
			group_list = MatchContinueDress(who, slope_str)
			for group in group_list:
#				print(group)
				bx = 0 + group.begin - 1
				by = start_y + group.begin - 1
				while by < CHAT_SIZE and bx >= 0 and not self._isDress(op, bx, by):
					value = EvalUnit ** (group.length - (start_y + group.begin - by) + 2)
					if value <= 1: break
#					print(bx, by, value)
					table[bx][by] *= value
					bx -= 1
					by -= 1
				bx = 0 + group.end + 1
				by = start_y + group.end + 1
				while bx < CHAT_SIZE and by < CHAT_SIZE and not self._isDress(op, bx, by):
					value = EvalUnit ** (group.length - (by - start_y - group.end) + 2)
					if value <= 1:break
#					print(bx, by, value)
					table[bx][by] *= value
					bx += 1
					by += 1
					
			correction = MatchCaseCorrection(self, who, slope_str)
			for item in correction:
				table[0 + item.position][start_y + item.position] *= item.value
			
			correction = MatchCaseCorrection(self, who, slope_str[::-1])
			for item in correction:
				table[CHAT_SIZE - 1 - start_y - item.position][CHAT_SIZE - 1 - item.position] *= item.value
				
		return table
	
					
				
	def GetRandAnswer(self, ls): #TODO
		Max = MIN_INT
		x = ls[0][1]
		y = ls[0][2]
		for play in ls:
			tmp = EvaluateRecurse(self, play[1], play[2], RECURSE_DEEP)
			print(tmp, play[1], play[2])
			if tmp > Max:
				Max = tmp
				x = play[1]
				y = play[2]
				
		return x, y
				
				
	def _Evaluate(self, who):
		# A size * size zeors matrix
		row = self._EvaluateRow(who)
		column = self._EvaluateColumn(who)
		slope = self._EvaluateSlope(who)
		main_slop = self._EvaluateMainSlope(who)
		#DEBUG:
#		if who == YB:
#			print('row:')
#			print(row)
#		print('\n\n')
#		print('column')
#		print(column)
#		print('\n\n')
#		print('slope')
#		print(slope)
#		print('\n\n')
#		print(SumUp(column, slope))
		return SumUp(SumUp(row,column), SumUp(main_slop, slope))
	
	#TODO:堆的处理：value = 1的值直接舍弃。其余情况按概率选择下子
	def Evaluate(self):
		evaluateSelf = self._Evaluate(YB)
		evaluatePlayer = self._Evaluate(PLAYER)
		xScaleTable(AGRESSIVE, evaluateSelf)
		xScaleTable(1 - AGRESSIVE, evaluatePlayer)
		#DEBUG:
#		print(evaluateSelf)
#		print(evaluatePlayer)
		evaluate = SumUp(evaluateSelf, evaluatePlayer)
		SideCorrection(evaluate)
		
		heap = []
		for y in range(CHAT_SIZE):
			for  x in range(CHAT_SIZE):
				if not self._isDress(YB, y, x) and not self._isDress(PLAYER, y, x):
					heapq.heappush(heap, (evaluate[y][x], y, x))
		largest = heapq.nlargest(PICK_N_LARGEST, heap)
		return largest
		
	def GetNextDressPosition(self):
		self.last_x, self.last_y = self.GetRandAnswer(self.Evaluate())
		return self.last_x, self.last_y
		
					
if __name__ == '__main__':
	print('请选择难度等级, 1 简单，2 中等，3 困难')
	difficulty = -1
	try:
		difficulty = int(input('>>> '))
	except ValueError:
		print('请输入1~3的整数')
	while(difficulty != 1 and difficulty != 2 and difficulty != 3):
		difficulty = input('>>> ')
	if difficulty == 1:
		RECURSE_DEEP = 0
	elif difficulty == 2:
		RECURSE_DEEP = 4
	elif difficulty == 3:
		RECURSE_DEEP = 6

	print(RECURSE_DEEP)
	gomoku = Gomoku()
	print(gomoku)
	while(True):
		s = input('>>> ')
		try:
			x, y = ParseIntPair(s)
		except (Exception):
			print('please input <x, y>')
			continue
		try:	
			gomoku.dress(PLAYER, x, y)
			gomoku.Evaluate()
			if gomoku.PLAYERHasWin == True:
				print('YOU has Win!!')
				MyQuit()
				break
			x, y = gomoku.GetNextDressPosition()
			gomoku.dress(YB, x, y)
			print(gomoku)
			gomoku.Evaluate()
		except (RuntimeError, ValueError, IndexError):
			print('Unable to Dress {}, {}'.format(INDEX_LIST[x], INDEX_LIST[y]))
		if gomoku.YBHasWin == True:
			print('You Lose!')
			MyQuit()
			break
#		except Exception:
#			print('Unknow Bug')
		
			
			
			
			
			
	
