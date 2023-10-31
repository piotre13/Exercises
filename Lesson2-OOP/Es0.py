class Animal(object):
	def __init__(self, name):
		self.name = name

	def jump(self):
		print(f"{self.name} has jumped")
	def __repr__(self):
		return 'yoooo'


class Quadruped(Animal):
	def __init__(self, name):
		Animal.__init__(self, name)
		self.n_legs = 4

q = Quadruped('yo')
q.jump()

print(q)