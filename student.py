#Defines a student class capable of storing 2 names and a dictionary of courses/marks
#can compute the arithmetic mean average of a student's grades
class Student:	
	name= ""
	family= ""
	courseMarks={}
	def	__init__(self, name, family):
		self.name = name
		self.family = family
	def addCourseMark(self, course, mark):	
		self.courseMarks[course] = mark
	def average(self):
		"""
		>>> zak = Student("Zak","Turchansky")
		>>> zak.addCourseMark("CMPUT 410", 85)
		>>> zak.addCourseMark("CMPUT 495", 100)
		>>> zak.addCourseMark("INT D 450", 92)
		>>> zak.average()
		92
		"""
		mean=0
		numCourses=0
		for mark in self.courseMarks.values():
			mean += mark
			numCourses += 1
		if numCourses == 0:
			return 0
		return mean/numCourses
#create a test instance of the student and print out the values it stores		
zak = Student("Zak","Turchansky")
zak.addCourseMark("CMPUT 410", 85)
zak.addCourseMark("CMPUT 495", 100)
zak.addCourseMark("INT D 450", 92)
print zak.name + " " + zak.family
for course, mark in zak.courseMarks.items():
	print str(course) + ": " + str(mark)
#print zak.courseMarks
print "Average: " + str(zak.average())
#Unit Tests
assert zak.name == "Zak"
assert zak.family == "Turchansky"
assert zak.courseMarks["CMPUT 410"] == 85
assert zak.average() == 92

if __name__ == "__main__":
    import doctest
    doctest.testmod()

