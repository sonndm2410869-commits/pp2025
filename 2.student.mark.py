class Student:
    def __init__(self):
        self.__id = None
        self.__name = None
        self.__dob = None
        self.__marks = {}

    def input(self):
        self.__id = input("Student id: ")
        self.__name = input("Student name: ")
        self.__dob = input("Student DoB: ")

    def get_id(self):
        return self.__id

    def set_mark(self, course_id, mark):
        self.__marks[course_id] = mark

    def get_mark(self, course_id):
        return self.__marks.get(course_id, None)

    def list(self):
        print(f"{self.__id} - {self.__name} - {self.__dob}")


class Course:
    def __init__(self):
        self.__id = None
        self.__name = None

    def input(self):
        self.__id = input("Course id: ")
        self.__name = input("Course name: ")

    def get_id(self):
        return self.__id

    def list(self):
        print(f"{self.__id} - {self.__name}")


class School:
    def __init__(self):
        self.students = []
        self.courses = []

    def input_students(self):
        n = int(input("Number of students: "))
        for _ in range(n):
            s = Student()
            s.input()
            self.students.append(s)

    def input_courses(self):
        n = int(input("Number of courses: "))
        for _ in range(n):
            c = Course()
            c.input()
            self.courses.append(c)

    def input_marks(self):
        course_id = input("Enter course id for entering marks: ")
        for s in self.students:
            mark = float(input(f"Mark for student {s.get_id()}: "))
            s.set_mark(course_id, mark)

    def list_students(self):
        for s in self.students:
            s.list()

    def list_courses(self):
        for c in self.courses:
            c.list()

    def show_marks(self):
        course_id = input("Course id: ")
        for s in self.students:
            m = s.get_mark(course_id)
            if m is not None:
                print(f"{s.get_id()}: {m}")


def main():
    school = School()
    while True:
        print("\n1. Input students")
        print("2. Input courses")
        print("3. Input marks")
        print("4. List students")
        print("5. List courses")
        print("6. Show marks")
        print("0. Exit")
        choice = input("Select: ")

        if choice == '1':
            school.input_students()
        elif choice == '2':
            school.input_courses()
        elif choice == '3':
            school.input_marks()
        elif choice == '4':
            school.list_students()
        elif choice == '5':
            school.list_courses()
        elif choice == '6':
            school.show_marks()
        elif choice == '0':
            break

main()
