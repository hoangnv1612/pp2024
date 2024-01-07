def input_number_of_students():
    num_students = int(input("Enter the number of students in the class: "))
    return num_students

def input_student_information(num_students):
    students = []
    for i in range(num_students):
        id = input("Enter student ID: ")
        name = input("Enter student name: ")
        dob = input("Enter student date of birth: ")
        student_info = {'id': id, 'name': name, 'dob': dob}
        students.append(student_info)
    return students

def input_number_of_courses():
    num_courses = int(input("Enter the number of courses: "))
    return num_courses

def input_course_information(num_courses):
    courses = []
    for i in range(num_courses):
        id = input("Enter course ID: ")
        name = input("Enter course name: ")
        course_info = {'id': id, 'name': name}
        courses.append(course_info)
    return courses

def main():
    num_students = input_number_of_students()
    student_info = input_student_information(num_students)
    num_courses = input_number_of_courses()
    course_info = input_course_information(num_courses)
    
    print("Student information:")
    for student in student_info:
        print(student['id'], student['name'], student['dob'])
    
    print("\nCourse information:")
    for course in course_info:
        print(course['id'], course['name'])

if __name__ == "__main__":
    main()
