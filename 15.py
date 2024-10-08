course = "She learning Python not phyton bro"
cours = "\nyou learning python's course\n"
coures = 'helearning python "Beginner"\n\n'
corues = '''Hi John,
Here is our first email to you.
Thank you,'''
print(corues)

print(course, cours, coures)

print(course[0]) #index 
print(course[2])
print(course[-1])
print(course[0:3]) #slicing
print("\n")

print(course[::-1]) #reverse 
print(course[::-4])  
print(course[::2]) #step 

print(len(cours)) 
print(len(course)) 
print(course.upper()) 
print(course.lower())
print(course.title())
print(course.capitalize())
print(course.find("y"))
print(course.replace("Python", "Java"))
print(course.replace("Python", "Java", 1)) 
print(course.count("Python"))
print(course.split())   
print(course.split(" "))
print(course.split("n"))    
print(course.split("not"))  
print("\n")
print("She" in course)
print("She" in cours)