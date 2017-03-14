import csv
credits=[]
grade=[]
GPA=[]
def calculateGrade():

	totalcreditsEachYear=0
	AverrageEachYear=0

	totalcredits=0
	Averrage=0
	for i in range(0,len(grade)):
		if grade[i]=="": #check ""
			try:
				# calculate Grade Each year and add to GPA
				GPA.append(AverrageEachYear/totalcreditsEachYear)
				# calculate totla Grade  and add to GPA
				GPA.append(Averrage/totalcredits)
				# set to zero of calculator each Year
				totalcreditsEachYear=0
				AverrageEachYear=0
			except ZeroDivisionError:
				continue
		else:
				# sum of grade * credits of Each year 
			totalcreditsEachYear=totalcreditsEachYear+credits[i] 
			AverrageEachYear=AverrageEachYear+float(grade[i]*credits[i])
				# sum of grade * credits of total Grade 
			totalcredits=totalcredits+credits[i] 
			Averrage=Averrage+(grade[i]*credits[i]) #calculateGPA
	return GPA
def convertGradeToNumber(grade):
	charGrade=['A','B+','B','C+','C','D+','D','F']
	valueGrade=[4.0,3.5,3.0,2.5,2.0,1.5,1.0,0.0]
	for i in range(0,len(grade)):
		for j in range(0,len(charGrade)):
			if grade[i]==charGrade[j]:
				grade[i]=valueGrade[j]
def readcsv(file):
	with open(file, 'r') as f:
	    reader = csv.reader(f)
	    for row in reader: #add value from csv to array (row[2],row[3])
			try: #check value Error
			    credits.append(float(row[2]))
			    grade.append(row[3])
			except ValueError:
			   continue
	convertGradeToNumber(grade)
def showGrade(GPA):
	Year=0
	for i in range(0,len(GPA)):
		if i%2 == 0: #check show GPA year and Averrage GPA
			if i%4 ==0: #check 2 term and add 1 to Year
				Year=Year+1
				Term = 0
			Term =Term+1
			print "GPA Year "+str(Year)+" Term "+str(Term)+": %.2f"%GPA[i]
		else:
			print "Averrage GPA : %.2f"%GPA[i]
			print ""

# read csv 
readcsv('AverageGrade.csv')
# show Grade
showGrade(calculateGrade())


