'''Question 1: This code is to take inputs from a user and calculate their final
weighted grade'''

hwWeight = 0.4

examWeight = 0.5

discussionWeight = 0.1

hwGrade = float(input('Enter your homework grade:'))
examGrade = float(input('Enter your exam grade:'))
discussionGrade = float(input('Enter your discussion grade:'))

finalGrade = (hwWeight*hwGrade)+(examWeight*examGrade)+(discussionWeight*discussionGrade)

print('The final grade is:',finalGrade)


'''Question 3: This code is supposed to compute the final amount for compound 
interest after a number of years.'''

P = 10000.0
n = 12.0
r =0.08

t= float(input('Enter how many years money should be compounded:'))

finalAmount= P*(1+(r/n))**(n*t)
print('The final compounded amount is:',finalAmount)

'''Question 4: This code is supposed to calculate and print out a students gpa 
and honours they would recieve based on their final score'''

score=float(input('Enter your score out of 100:'))


def calculateGPA(score):
    if score>=80 and score<=100:
        return 4.00
    elif score<80 and score>=75:
        return 3.50
    elif score<75 and score>=70:
        return 3.00
    elif score<70 and score>=65:
        return 2.50
    elif score<65 and score>=60:
        return 2.00
    elif score<60 and score>=55:
        return 1.50
    elif score<55 and score>=50:
        return 1.00
    elif score<50:
        return 0.00
    
def getHonours(gpa):
    if gpa<=4.00 and gpa>=3.85:
        return 'Summa Cum Laude'
    elif gpa<3.85 and gpa>=3.70:
        return 'Magna Cum Laude'
    elif gpa<3.70 and gpa>=3.50:
        return 'Magna Cum Laude'
    elif gpa<3.50:
        return 'No Honours'
        
gpa = calculateGPA(score)
honours = getHonours(gpa)
print('GPA:',gpa)
print('Honours:',honours)

'''Question 5: This code asks the user to input the value of the radius of a
circle and outputs the area of the circle'''

import math

radius = float(input('Enter a radius:'))

area_of_circle=math.pi*(radius)**2

print("The area is:",area_of_circle)

'''Question 6: Asks the user for three lengths and tells the user if a triangle 
could be made from those lengths'''
'''Part A'''

def is_triangle(a,b,c):
    if a+b<c or a+c<b or b+c<a:
        print('FALSE')
    else:
        print('TRUE')
        
is_triangle(4,13,12)

'''Part B'''

def is_triangle(a,b,c):
    if a+b<c or a+c<b or b+c<a:
        return('FALSE')
    else:
        return('TRUE')
        
length1 = int(input('Enter first side length:' ))
length2 = int(input('Enter second side length:' ))
length3 = int(input('Enter third side length:' ))

evaluation= is_triangle(length1,length2,length3)
print('Can the lengths form a triangle?', evaluation)
