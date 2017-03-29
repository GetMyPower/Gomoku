from config import *
import heapq

#TODO:需要优化、需要改良代码的书写
def SumUp(a, b):
	ret = [[0 for x in range(CHAT_SIZE)] for x in range(CHAT_SIZE)]
	for x in range(CHAT_SIZE):
		for y in range(CHAT_SIZE):
			ret[x][y] += a[x][y] + b[x][y]
	return ret

def xScaleTable(x, table):
	for i in range(CHAT_SIZE):
		for j in range(CHAT_SIZE):
			table[i][j] *= x
	
class Gomoku(object):
	def _init_square(self):
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
		ret = '  0 1 2 3 4 5 6 7 8 9 w y\n'
		for x in range(CHAT_SIZE):
			ret += (str(x) if x < 10 else 'w' if x == 10 else 'y') + ' '
			for y in range(CHAT_SIZE):
				ret += self.square[y][x] + ' '
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
	
	#TODO:需要修正，三连或四连被堵路的情况
	def _EvaluateRow(self, who):
		table = [[1 for x in range(CHAT_SIZE)] for x in range(CHAT_SIZE)]
		op = YB if who == PLAYER else PLAYER
		for row in range(CHAT_SIZE):
			beg = 0
			while beg < CHAT_SIZE:
				while beg < CHAT_SIZE and not self._isDress(who, beg, row):
					beg += 1
				if beg >= CHAT_SIZE:break
				
				length = 1
				while beg + length < CHAT_SIZE and self._isDress(who, beg + length, row):
					length += 1
				end = beg + length - 1
				
#				print('find group ({}) to ({}) in row {}'.format(beg, end, row))
				
				cur = beg - 1
				while cur >= 0 and not self._isDress(op, cur, row):
					value = EvalUnit ** (length - (beg - cur) + 1)
					if value <= 1: break
					table[cur][row] *= value
					cur -= 1
				cur = end + 1
				while cur < CHAT_SIZE and not self._isDress(op, cur, row):
					value = EvalUnit ** (length - (cur - end) + 1)
					if value <= 1: break
					table[cur][row] *= value
					cur += 1					
				beg = end + 1
		return table
				
	def _EvaluateColumn(self, who):
		table = [[1 for x in range(CHAT_SIZE)] for x in range(CHAT_SIZE)]
		op = YB if who == PLAYER else PLAYER
		for column in range(CHAT_SIZE):
			beg = 0
			while beg < CHAT_SIZE:
				while beg < CHAT_SIZE and not self._isDress(who, column, beg):
					beg += 1
				if beg >= CHAT_SIZE:break
			
				length = 1
				while beg + length < CHAT_SIZE and self._isDress(who, column, beg + length):
					length += 1
				end = beg + length - 1
			
#				print('find group ({}) to ({}) in column {}'.format(beg, end, column))
			
				cur = beg - 1
				while cur >= 0 and not self._isDress(op, column, cur):
					value = EvalUnit ** (length - (beg - cur) + 1)
					if value <= 1: break
					table[column][cur] *= value
					cur -= 1
				cur = end + 1
				while cur < CHAT_SIZE and not self._isDress(op, column, cur):
					value = EvalUnit ** (length - (cur - end) + 1)
					if value <= 1: break
					table[column][cur] *= value
					cur += 1
				beg = end + 1
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
			bx = start_x
			by = 0
			while bx >= 0:
				while bx >= 0 and not self._isDress(who, bx, by):
					bx -= 1
					by += 1
				if bx < 0:break
			
				length = 1
				while bx - length >= 0 and self._isDress(who, bx - length, by + length):
					length += 1
				ex = bx - length + 1
				ey = by + length - 1
			
#				print('find group ({}, {}) to ({}, {}) '.format(bx, by, ex, ey))

				cur_x = bx + 1
				cur_y = by - 1
				while cur_y >= 0 and not self._isDress(op, cur_x, cur_y):
					value = EvalUnit ** (length - (cur_x - bx) + 1)
					if value <= 1: break
					table[cur_x][cur_y] *= value
					cur_x += 1
					cur_y -= 1
				cur_x = ex - 1
				cur_y = ey + 1
				while cur_x >= 0 and not self._isDress(op, cur_x, cur_y):
					value = EvalUnit ** (length - (ex - cur_x) + 1)
					if value <= 1: break
					table[cur_x][cur_y] *= value
					cur_x -= 1
					cur_y += 1
				
				bx = ex - 1
				by = ey + 1
		
		for start_y in range(1, CHAT_SIZE - 5 + 1):
			by = start_y
			bx = CHAT_SIZE - 1
			while by < CHAT_SIZE:
				while by < CHAT_SIZE and not self._isDress(who, bx, by):
					bx -= 1
					by += 1
#					print('{}, {}'.format(bx, by))
				if by >= CHAT_SIZE:break
	
				length = 1
				while by + length < CHAT_SIZE and self._isDress(who, bx - length, by + length):
					length += 1
				ex = bx - length + 1
				ey = by + length - 1
	
				print('find group ({}, {}) to ({}, {}) '.format(bx, by, ex, ey))

				cur_x = bx + 1
				cur_y = by - 1
				while cur_x < CHAT_SIZE and not self._isDress(op, cur_x, cur_y):
					value = EvalUnit ** (length - (cur_x - bx) + 1)
					if value <= 1: break
					table[cur_x][cur_y] *= value
					cur_x += 1
					cur_y -= 1
				cur_x = ex - 1
				cur_y = ey + 1
				while cur_y < CHAT_SIZE and not self._isDress(op, cur_x, cur_y):
					value = EvalUnit ** (length - (ex - cur_x) + 1)
					if value <= 1: break
					table[cur_x][cur_y] *= value
					cur_x -= 1
					cur_y += 1
		
				bx = ex - 1
				by = ey + 1
		return table
				
	def GetRandAnswer(self, ls): #TODO
		return ls
				
				
	def _Evaluate(self, who):
		# A size * size zeors matrix
		row = self._EvaluateRow(who)
		column = self._EvaluateColumn(who)
		slope = self._EvaluateSlope(who)
		#DEBUG:
#		print('row:')
#		print(row)
#		print('\n\n')
#		print('column')
#		print(column)
#		print('\n\n')
#		print('slope')
#		print(slope)
#		print('\n\n')
#		print(SumUp(column, slope))
		return SumUp(row, SumUp(column, slope))
	
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
		heap = []
		for y in range(CHAT_SIZE):
			for  x in range(CHAT_SIZE):
				if not self._isDress(YB, y, x) and not self._isDress(PLAYER, y, x):
					heapq.heappush(heap, (evaluate[y][x], y, x))
		largest = heapq.nlargest(PICK_N_LARGEST, heap)
		return self.GetRandAnswer(largest)
		
					
if __name__ == '__main__':
	gomoku = Gomoku()
