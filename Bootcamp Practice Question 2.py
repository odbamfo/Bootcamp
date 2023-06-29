''' Write a function called compareStrings that takes a garland and a flower in that order and returns the number of flowers you have that are garlands.'''

def compareStrings():
    take_Garlands = str(input('Enter a garland:'))
    take_Flowers = str(input('Enter a flower:'))
    count=0
    
    if len(take_Garlands) < 1 or len(take_Flowers) > 50:
        print('Invalid')
        return None

    if not take_Garlands.isalpha() or not take_Flowers.isalpha():
        print('Garlands and flowers should only consist of English letters')
        return None

    if len(set(take_Garlands)) != len(take_Garlands):
        print('All characters of garland should be unique')
        return None
    
    for i in range(len(take_Garlands)):
        for j in range(len(take_Flowers)):
            individual_Garlands = take_Garlands[i]
            individual_Flowers = take_Flowers[j]
            if individual_Garlands == individual_Flowers:
                count +=1
            else:
                continue
        return count
            

    
print(compareStrings())


'''GPA and Honours code'''

# Function to calculate letter grade and grade point
def calculateLetterGrade(score):
    if score <= 100 and score >= 80:
        letter_grade = 'A'
        grade_point = 4.0
    elif score < 80 and score >= 75:
        letter_grade = 'B+'
        grade_point = 3.5
    elif score < 75 and score >= 70:
        letter_grade = 'B'
        grade_point = 3.0
    elif score < 70 and score >= 65:
        letter_grade = 'C+'
        grade_point = 2.5
    elif score < 65 and score >= 60:
        letter_grade = 'C'
        grade_point = 2.0
    elif score < 60 and score >= 55:
        letter_grade = 'D+'
        grade_point = 1.5
    elif score < 55 and score >= 50:
        letter_grade = 'D'
        grade_point = 1.0
    elif score < 50:
        letter_grade = 'F'
        grade_point = 0.0
    

    return letter_grade, grade_point


# Function to determine honors category based on cumulative GPA
def getHonours(grade_point):
    if  grade_point <= 4.00 and  grade_point >= 3.85:
        return 'Summa Cum Laude'
    elif  grade_point < 3.85 and  grade_point >= 3.70:
        return 'Magna Cum Laude'
    elif  grade_point < 3.70 and  grade_point >= 3.50:
        return 'Magna Cum Laude'
    elif  grade_point < 3.50:
        return 'No Honours'


# Function to input and calculate grades for multiple courses
def calculateGrades():
    num_courses = int(input("Enter the number of courses: "))

    grades_count = {'A': 0, 'B+': 0, 'B': 0, 'C+': 0, 'C': 0, 'D+': 0, 'D': 0, 'F': 0}
    total_grade_points = 0
    total_credits = 0

    for i in range(num_courses):
        score = float(input(f"Enter the numerical score for course {i + 1}: "))
        credits = float(input(f"Enter the credit weighting for course {i + 1}: "))

        letter_grade, grade_point = calculateLetterGrade(score)

        grades_count[letter_grade] += 1
        total_grade_points += grade_point * credits
        total_credits += credits

        print(f"Course {i + 1}: Grade: {letter_grade}, Grade Point: {grade_point}")

    cumulative_gpa = total_grade_points / total_credits
    honors_category = getHonours(cumulative_gpa)

    print("\nGrade Summary:")
    for grade, count in grades_count.items():
        print(f"Number of {grade}s: {count}")

    print(f"\nCumulative GPA: {cumulative_gpa:.2f}")
    print(f"Honors Category: {honors_category}")


calculateGrades()




'''Write a program to accept a number from a user and calculate the sum of all numbers from 1 to a 
given number. For example, if the user entered 10 the output should be 55
(1+2+3+4+5+6+7+8+9+10). Use formatted strings to print a statement showing the sum. In this 
case, “The sum is 55.'''

lastnumber= int(input('Type a number:'))

def sumCalc(lastnumber):
    Sum = (lastnumber/2)*(1+lastnumber)
    print(f'The sum is {Sum}')

sumCalc(lastnumber)


'''Implement the len function. Name it customLen. The len function takes a string and returns the 
number of characters it has.'''

string= input("Enter a word:")

def customLen(string):
    count = 0
    for characters in string:
        count += 1
    return count

print(customLen(string))


''' Multiplication table'''

your_Number= int(input('Enter a number to be multiplied:'))

print(f"MULTIPLICATION TABLE OF {your_Number}")

def mult_table( count=1):
    if count>12:
        return
    else:
        product = count * your_Number
        print(f"{count}*{your_Number}={product}")
        count+=1
        mult_table(count)
        
mult_table()
        

"Magic Number"

magic_number = 50
your_guess = int(input('Enter your guess(1-100):'))

def respnse_to_guess():
    if your_guess>magic_number:
        print(" That number is too High!")
    elif your_guess<magic_number:
        print("That number is too Low!")
    else:
        print("Correct!")
        
respnse_to_guess()
    
sumCalc(lastnumber)
            

''' Write a function called is_vowel that takes as a parameter a string 
containing a single character and returns whether the character is a vowel. A
vowel is one of the characters ‘a’, ‘e’, ‘i', ‘o’, ‘u’. For instance, if "e" is 
supplied, your function should return True, but if "p" is supplied, it should 
return False. Your function should take into account the case of the input 
(returning True for both "A" and "a").'''

letter=str(input('Enter a letter:'))

def is_vowel(letter):
    if letter =='a' or letter =='A' or letter =='e' or letter =='E' or letter =='i' or letter =='I' or letter == 'o' or letter =='O' or letter =='u' or letter =='U':
        return True
    else:
        return False
        
result = is_vowel(letter)
print(result)
