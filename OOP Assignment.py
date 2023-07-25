'''Student class assignment'''
class Student:
    def __init__(self, name, student_id, gender, major, yeargroup):
        self.name = name
        self.student_id = student_id
        self.gender = gender
        self.major = major
        self.yeargroup = yeargroup

    def change_major(self, new_major):
        self.major = new_major

    def __str__(self):
        return f"Name: {self.name}\nStudent ID: {self.student_id}\nGender: {self.gender}\nMajor: {self.major}\nYeargroup: {self.yeargroup}"


student1 = Student("John Doe", "123456", "Male", "Computer Science", 2023)
print(student1)
'''Print the initial student information'''
student1.change_major("Electrical Engineering")
'''Changing the major of the student'''
print(student1)
'''Print the updated student information'''

'''Course Class'''
class Course:
    def __init__(self, course_code, course_name, name_of_instructor, name_of_fi):
        self.course_code = course_code
        self.course_name = course_name
        self.name_of_instructor = name_of_instructor
        self.name_of_fi = name_of_fi
        self.enrolled_students = []

    def __str__(self):
        return f"course_code: {self.course_code}\ncourse_name: {self.course_name}\nname_of_instructor: {self.name_of_instructor}\nname_of_fi: {self.name_of_fi}\nNumber of Students Enrolled: {len(self.enrolled_students)}"

    def enroll_student(self, student):
        if not self.check_enrolment_by_ID(student.student_id):
            self.enrolled_students.append(student)
            return True
        else:
            return False

    def display_enrolled_students(self):
        print("Enrolled Students:")
        print(f"{'Name':<20} {'Student ID':<15} {'Gender':<10} {'Major':<20} {'Yeargroup'}")
        print("-" * 75)
        for student in self.enrolled_students:
            print(
                f"{student.name:<20} {student.student_id:<15} {student.gender:<10} {student.major:<20} {student.yeargroup}")

    def check_enrolment_by_ID(self, student_id):
        for student in self.enrolled_students:
            if student.student_id == student_id:
                return True
        return False

    def unenrol_student(self, student_id):
        for student in self.enrolled_students:
            if student.student_id == student_id:
                self.enrolled_students.remove(student)
                return True
        return False

    def count_male_students(self):
        num_male_students = 0
        for student in self.enrolled_students:
            if student.gender == "Male":
                num_male_students += 1
        return num_male_students

    def display_enrolment_statistics(self):
        num_students = len(self.enrolled_students)
        num_male_students = self.count_male_students()
        num_female_students = num_students - num_male_students

        yeargroup_stats = {}
        major_stats = {}
        for student in self.enrolled_students:
            yeargroup_stats[student.yeargroup] = yeargroup_stats.get(student.yeargroup, 0) + 1
            major_stats[student.major] = major_stats.get(student.major, 0) + 1

        print("Enrolment Statistics:")
        print(f"Number of Students Enrolled: {num_students}")
        print(f"Number of Male Students: {num_male_students}")
        print(f"Number of Female Students: {num_female_students}")
        print("Yeargroup Statistics:")
        for yeargroup, count in yeargroup_stats.items():
            print(f"Yeargroup {yeargroup}: {count} students")
        print("Major Statistics:")
        for major, count in major_stats.items():
            print(f"{major}: {count} students")


'''Script test'''

# Creating students
student1 = Student("John Doe", "123456", "Male", "Computer Science", 2023)
student2 = Student("Jane Smith", "987654", "Female", "Electrical Engineering", 2022)
student3 = Student("Alice Johnson", "567890", "Female", "Physics", 2024)

# Creating courses
course1 = Course("CS101", "Introduction to Computer Science", "Dr. Smith", "Jane Doe")
course2 = Course("EE201", "Electrical Engineering Fundamentals", "Prof. Brown", "John Smith")

# Enrolling students in courses
print(course1.enroll_student(student1))  # Should print True
print(course1.enroll_student(student2))  # Should print True
print(course1.enroll_student(student1))  # Should print False, already enrolled
print(course2.enroll_student(student2))  # Should print True
print(course2.enroll_student(student3))  # Should print True

# Displaying enrolled students in the courses
course1.display_enrolled_students()
course2.display_enrolled_students()

# Checking enrolment by student ID
print(course1.check_enrolment_by_ID("123456"))  # Should print True
print(course1.check_enrolment_by_ID("999999"))  # Should print False

# Unenrolling a student from a course
print(course2.unenrol_student("567890"))  # Should print True
print(course2.unenrol_student("111111"))  # Should print False

# Displaying enrolment statistics for courses
course1.display_enrolment_statistics()
course2.display_enrolment_statistics()

