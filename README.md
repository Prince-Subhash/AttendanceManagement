# AttendanceManagement
# Attendance Management System

This project is a simple **Attendance Management System** built with Python using `Tkinter` for the graphical user interface (GUI) and `openpyxl` to handle Excel file operations. The system allows teachers or administrators to mark and track student attendance, storing data in an Excel file (`attendance.xlsx`).

## Project Structure

gopal_project/ │
├── gui.py # GUI code for interacting with the system 
├── main.py # Entry point to run the application 
├── attendance_functions.py # Handles attendance data logic 
├── file_operations.py # Manages loading and saving attendance data to an Excel file 
├── attendance.xlsx # Excel file where attendance data is stored 
└── README.md # Project documentation

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
