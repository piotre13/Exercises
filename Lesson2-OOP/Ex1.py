import random


class Staff:    # alternative to this line ---> class Staff (object):

	def __init__(self, role, dep, salary):
		self.role = role
		self.dep = dep
		self.salary = salary

	def __repr__(self):
		return f'role:{self.role}, dep: {self.dep}, salary: {self.salary}'

	def print_info(self):
		print(f'role:{self.role}, dep: {self.dep}, salary: {self.salary}')


class Teacher (Staff):

	def __init__(self, name, dep, salary):
		Staff.__init__(self, 'Teacher', dep, salary)
		self.name = name

	def random_grade(self): # question: it is needed to define this method as a class function?
		return random.randint(0, 10)

	def print_name(self):
		print(self.name)


class BadTeach(Teacher):
	def __init__(self, name, dep, salary):
		Teacher.__init__(name, dep, salary)

	def random_grade(self): # example of polymorphism
		return random.randint(0, 5)

# for Good teacher is the same

if __name__ == '__main__':

	Bottaccioli = Teacher(10, 'DIST', 'Teacher')
	Bottaccioli.print_name()

	print(Bottaccioli)








	#Bottaccioli.print_info()
	print(Bottaccioli)

	print(Bottaccioli.role)
	print(Bottaccioli.name)

	Bottaccioli.name='Pietro'
	print(Bottaccioli.name)

	Bottaccioli.print_info()

	grade = Bottaccioli.random_grade()
	print(grade)