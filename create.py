import openpyxl

def create_attendance_file(filename):
    # Create a new workbook and access the active sheet
    workbook = openpyxl.Workbook()
    sheet = workbook.active

    # Add headers to the first row
    sheet.append(["Student", "Attendance"])

    # Add some initial sample data (you can modify these)
    students = [
        ("John Doe", "Present"),
        ("Jane Smith", "Absent"),
        ("Michael Johnson", "Present"),
        ("Emily Davis", "Absent"),
        ("Sarah Wilson", "Present")
    ]

    # Add student attendance data to the sheet
    for student, attendance in students:
        sheet.append([student, attendance])

    # Save the workbook to the specified file
    workbook.save(filename)
    print(f"Attendance file '{filename}' created successfully.")

# Create the attendance file
create_attendance_file("attendance.xlsx")