

class Student():
	def __init__(self, name, surname, grades):
		self.__name = name
		self.surname = surname
		self.grades = grades

	def fullname(self):
		full = f"{self.name} {self.surname}"
		return full

	def average_grades(self):
		avg_res = {}
		for k , val in self.grades.items():
			avg_res[k] = sum(val) /len(val)
		return avg_res


if __name__ == '__main__':
	stefano = Student('stefano', 'rossi',
					  {'geometry':[25, 30], 'analysis':[18, 23]})
	print(stefano.fullname())
	print(stefano.name)
	stefano.name = 'marco'
	print(stefano.fullname())
	print(stefano.average_grades())

