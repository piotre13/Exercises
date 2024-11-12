import random

class Staff():
	def __init__(self, role, dep, salary):
		self.role = role
		self.dep = dep
		self.salary = salary
	def info(self):
		info = f'role: {self.role} \n ' \
			   f'department {self.dep} \n salary {self.salary}'
		print(info)
		return info

class Teacher(Staff):
	def __init__(self, dep, salary, course):

		Staff.__init__(self,'teacher',dep,salary)
		self.course = course
	def grade_assign(self):
		return random.randint(15,30)


class BadTeacher(Teacher):
	def __init__(self, dep, salary, course):
		Teacher.__init__(dep, salary,course)

	def grade_assign(self):
		return random.randint(0,18)
class GoodTeacher(Teacher):
	def __init__(self, dep, salary, course):
		super().__init__(dep,salary,course)
	def grade_assign(self):
		return random.randint(25,30)

if __name__ == '__main__':

	Bottaccioli = Teacher('teacher','DAUIN', 0, 'ICSS')
	print(Bottaccioli.course)
	print(Bottaccioli.dep)
	print(Bottaccioli.salary)
	Bottaccioli.info()


	Pietro = GoodTeacher('DAUIN',0,'ICSS')
	Bad_one = BadTeacher('DAUIN',2000,'ICSS')
