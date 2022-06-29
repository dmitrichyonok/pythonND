class Student:
	
	def __init__(self, name, grades):
		self.name = name
		self.grades = list(map(int, grades.split(',')))
		self.average_grade = self.get_average_grade()
	
	def get_average_grade(self):
		avg = sum(self.grades) / len(self.grades)

		return avg