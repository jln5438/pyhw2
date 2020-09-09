#Author: Jacob Noethiger jln5438@psu.edu
def getGradePoint(grade):
  GPA=0.0
  if(grade=='A'):
    GPA=4.0
  elif(grade=='A-'):
    GPA=3.67
  elif(grade=='B+'):
    GPA=3.33
  elif(grade=='B'):
    GPA=3.0
  elif(grade=='B-'):
    GPA=2.67
  elif(grade=='C+'):
    GPA=2.33
  elif(grade=='C'):
    GPA=2.0
  elif(grade=='D'):
    GPA=1.0
  return GPA

letterGrade=input("Enter your course 1 letter grade: ")
credit1=int(input("Enter your course 1 credit: "))
GPA1=getGradePoint(letterGrade)
print("Grade point for course 1 is: "+str(GPA1))

letterGrade=input("Enter your course 2 letter grade: ")
credit2=int(input("Enter your course 2 credit: "))
GPA2=getGradePoint(letterGrade)
print("Grade point for course 2 is: "+str(GPA2))

letterGrade=input("Enter your course 3 letter grade: ")
credit3=int(input("Enter your course 3 credit: "))
GPA3=getGradePoint(letterGrade)
print("Grade point for course 3 is: "+str(GPA3))

GPA=((credit1*GPA1)+(credit2*GPA2)+(credit3*GPA3))/(credit1+credit2+credit3)
print("Your GPA is: "+str(GPA))