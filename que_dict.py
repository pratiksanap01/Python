""" WAP to enter marks of 3 subjects from the user and store them in a dictionary. Start with
 an empty dictionary & add one by one. Use subject name as key & marks as value."""
 
 
marks = {}

phy_marks = int(input("Enter a marks of PHY :"))
chem_marks = int(input("Enter a marks of CHEM :"))
math_marks = int(input("Enter a marks of MATH :"))

marks.update({"phy": phy_marks}) 
marks.update({"chem": chem_marks}) 
marks.update({"math": math_marks}) 

print(marks)