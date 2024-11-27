# AttendanceManagement
# Attendance Management System

This project is a simple **Attendance Management System** built with Python using `Tkinter` for the graphical user interface (GUI) and `openpyxl` to handle Excel file operations. The system allows teachers or administrators to mark and track student attendance, storing data in an Excel file (`attendance.xlsx`).

## Project Structure

gopal_project/
│
├── gui.py
├── main.py
├── attendance_functions.py
├── file_operations.py
└── attendance.xlsx  # this is where attendance data is saved and loaded from

## Features

- **Mark Attendance**: Mark students as "Present" or "Absent" and save it to an Excel file.
- **View Attendance**: View the current attendance of all students.
- **Excel Storage**: All attendance data is stored in `attendance.xlsx`.

## Requirements

You need to install the following Python libraries:

- `tkinter`: For the graphical user interface.
- `openpyxl`: For reading and writing to Excel files.

### Install dependencies:

```bash
pip install openpyxl
