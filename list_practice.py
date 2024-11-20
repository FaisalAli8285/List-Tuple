studentDetails=["faisal", 50,"Hashir",72,"mohib", 69]
print(studentDetails)
print(studentDetails[0])
studentDetails[4]="ubaid"
#print modified list
print(studentDetails)
#slicing
print(studentDetails[2:5])
#negative slicing
print(f" negative slicing {studentDetails[-4:-1]}")
#list method
#append method : append new element at the end of list
studentDetails.append("hujjar")
#sort method : sort in ascending or descending order
marks=[100,300,50,70,50,89,97]
marks.sort()
print(marks)
marks.sort(reverse=True)
print(marks)

