students = {}

while True:
    print("\nAttendance Management System")
    print("1. Add Student")
    print("2. Mark Attendance")
    print("3. View Attendance")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter student name: ")
        students[name] = "Not Marked"

    elif choice == "2":
        name = input("Enter student name: ")
        if name in students:
            status = input("Present(P) / Absent(A): ")
            if status.upper() == "P":
                students[name] = "Present"
            else:
                students[name] = "Absent"
        else:
            print("Student not found!")

    elif choice == "3":
        print("\nAttendance Report")
        for name, status in students.items():
            print(name, "-", status)

    elif choice == "4":
        break

    else:
        print("Invalid Choice")