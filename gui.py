import tkinter as tk
from tkinter import messagebox
from attendance_functions import fetch_attendance_data, mark_attendance

# Function to initialize the app and set up the GUI
def run_app():
    # Set up the main window
    window = tk.Tk()
    window.title("Attendance Management System")

    # Create widgets for user interaction
    student_label = tk.Label(window, text="Student Name")
    student_label.pack()

    student_entry = tk.Entry(window)
    student_entry.pack()

    attendance_label = tk.Label(window, text="Attendance Status")
    attendance_label.pack()

    attendance_var = tk.StringVar(window)
    attendance_var.set("Present")  # default value

    attendance_menu = tk.OptionMenu(window, attendance_var, "Present", "Absent")
    attendance_menu.pack()

    def submit_attendance():
        student_name = student_entry.get()
        attendance_status = attendance_var.get()
        
        # Mark the attendance for the student
        mark_attendance(student_name, attendance_status)
        
        messagebox.showinfo("Success", f"Attendance for {student_name} marked as {attendance_status}")

    submit_button = tk.Button(window, text="Submit", command=submit_attendance)
    submit_button.pack()

    # Display current attendance data
    def show_attendance():
        attendance_data = fetch_attendance_data()
        attendance_window = tk.Toplevel(window)
        attendance_window.title("Attendance Data")
        
        for record in attendance_data:
            tk.Label(attendance_window, text=f"{record['student']}: {record['attendance']}").pack()

    show_button = tk.Button(window, text="Show Attendance", command=show_attendance)
    show_button.pack()

    # Run the main window
    window.mainloop()