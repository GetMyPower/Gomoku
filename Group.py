class Group(object):
	def __init__(self, begin, end):
		self.begin = begin
		self.end = end
		self.length = end - begin + 1
		
	def __str__(self):
		return 'Group: ({}, {}) length: {}'.format(self.begin, self.end, self.length)
		
	def __lt__(self, other):
		return self.begin < other.begin
		
class Correction(object):
	def __init__(self, pos, value):
		self.position = pos
		self.value = value
