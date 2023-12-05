class Student():
	def __init__(self,name,surname, grades):
		self.name = name
		self.surname = surname
		self.grades = grades


	def get_fullname(self):
		# we could also have used the __repr__ method
		print('%s %s'%(self.name,self.surname))
	    #return '%s %s'%(self.name,self.surname)

	def get_avg_grades(self):
		mean = sum(self.grades)/len(self.grades)
		self.avg = mean # here we create a class attribute that stores the average value
		#an alternative could have been to return the value
		#return mean






if __name__ == '__main__':

	a = 'pietro'
	s = 'rando'
	g = [10,8,9]

	student1 = Student(a,s,g)
	student1.get_fullname()
	student1.get_avg_grades()
	#print(student1.avg)
	student1.avg = 0.0


	student2 = Student('Mario','Rossi',[3,5,6,7])
	student2.get_fullname()
