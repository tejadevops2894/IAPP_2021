#!/bin/python3

#final report
#check your grade status using valid studentid and LFname only

a = input("Enter StudentID or LFname: ")

if (a == "21IDT001") or (a == "John Smith"):
 print("StudentID: 21IDT001")
 print("LFname: John Smith")
 print("CourseID: 11111")
 print("CourseName: Java 101")
 print("Marks: 77")
 print("Grade: Average")

elif (a == "21IDT002") or (a == "Surya Teja"):
 print("StudentID: 21IDT002")
 print("LFname: Surya Teja")
 print("CourseID: 11111")
 print("CourseName: Java 101")
 print("Marks: 80")
 print("Grade: Good")

else:
 print("Enter valid StudentID or LFname")
