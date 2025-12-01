
students = []
courses = []
marks = {}   



def input_number_of_students():
    n = int(input("Enter number of students: "))
    for _ in range(n):
        student_id = input("Student ID: ")
        name = input("Student Name: ")
        dob = input("Date of Birth: ")
        students.append({
            "id": student_id,
            "name": name,
            "dob": dob
        })


def input_number_of_courses():
    n = int(input("Enter number of courses: "))
    for _ in range(n):
        cid = input("Course ID: ")
        name = input("Course Name: ")
        courses.append({
            "id": cid,
            "name": name
        })


def enter_marks_for_course():
    course_id = input("Enter course ID to input marks: ")

    marks[course_id] = {}

    print(f"Entering marks for course: {course_id}")
    for student in students:
        mark = float(input(f"Enter mark for {student['name']}: "))
        marks[course_id][student["id"]] = mark

def list_courses():
    print("\n--- COURSE LIST ---")
    for c in courses:
        print(f"{c['id']} - {c['name']}")


def list_students():
    print("\n--- STUDENT LIST ---")
    for s in students:
        print(f"{s['id']} - {s['name']} - DOB: {s['dob']}")


def show_student_marks():
    course_id = input("Enter course ID to view marks: ")

    if course_id not in marks:
        print("No marks found for this course!")
        return

    print(f"\n--- Marks for course {course_id} ---")
    for student in students:
        sid = student["id"]
        if sid in marks[course_id]:
            print(f"{student['name']}: {marks[course_id][sid]}")
        else:
            print(f"{student['name']}: No mark")

def main():
    while True:
        print("\n===== STUDENT MARK MANAGEMENT =====")
        print("1. Input students")
        print("2. Input courses")
        print("3. Enter marks for a course")
        print("4. List students")
        print("5. List courses")
        print("6. Show student marks for a course")
        print("0. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            input_number_of_students()
        elif choice == "2":
            input_number_of_courses()
        elif choice == "3":
            enter_marks_for_course()
        elif choice == "4":
            list_students()
        elif choice == "5":
            list_courses()
        elif choice == "6":
            show_student_marks()
        elif choice == "0":
            break
        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()
