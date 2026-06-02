s_name=(input("Student Name:"))
s1=int(input("Marks in S1:"))
s2=int(input("Marks in S2:"))
s3=int(input("Marks in S3:"))
s4=int(input("Marks in S4:"))
s5=int(input("Marks in S5:"))
total=s1 + s2 +s3 + s4 + s5
percent=(total / 500) * 100
print("Total marks:",total)
print("Percentage:",percent)
if percent==100:
       print("Grade:O")
elif percent>=95:
   print("Grade:A+")
elif percent>=90:
     print("Grade:A")
elif percent>=85:
     print("Grade:B")
elif percent>=75:
     print("Grade:C")
elif percent>=60:
     print("Grade:D")
else :
     print("student is failed") 
