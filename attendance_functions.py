from file_operations import load_attendance_from_file, save_attendance_to_file

# Function to fetch attendance data from the file
def fetch_attendance_data():
    attendance_data = load_attendance_from_file()
    return attendance_data

# Function to mark attendance (update the file)
def mark_attendance(student_name, attendance_status):
    attendance_data = load_attendance_from_file()
    
    # Find student and update attendance
    for record in attendance_data:
        if record["student"] == student_name:
            record["attendance"] = attendance_status
            break
    else:
        # If student is not found, add new entry
        attendance_data.append({"student": student_name, "attendance": attendance_status})
    
    # Save updated attendance data to the file
    save_attendance_to_file(attendance_data)