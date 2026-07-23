# 🎓 Student Grade Management System

A simple console-based Student Grade Management System developed in Python. This application allows users to manage student records efficiently by adding, updating, searching, deleting, and viewing student information. The project also stores records permanently using a JSON file.

---

## 📌 Features

- Add new student records
- View all students
- Search students by Roll Number or Name
- Update existing student information
- Delete student records
- Automatic grade calculation
- Display class statistics
  - Average Marks
  - Highest Scorer
  - Lowest Scorer
- Sort students by marks
- Persistent data storage using JSON
- Input validation for marks

---

## 🛠 Technologies Used

- Python 3.x
- JSON
- OS Module

---

## 📂 Project Structure

```
Student_Grade_Management_System/
│
├── main.py
├── students.json
├── README.md
├── LICENSE
└── screenshots/
```

---

## 🚀 How to Run

### Clone the repository

```bash
git clone https://github.com/yourusername/student-grade-management.git
```

### Navigate to the project folder

```bash
cd student-grade-management
```

### Run the project

```bash
python main.py
```

---

## 📋 Menu

```
1. Add Student
2. View Students
3. Search Student
4. Update Student
5. Delete Student
6. Class Statistics
7. Sort Students
8. Exit
```

---

## 💾 Data Storage

All student records are automatically saved in a **students.json** file.

Example:

```json
{
    "101": {
        "Name": "Yashvir",
        "Marks": 92,
        "Grade": "A+"
    }
}
```

---

## 📊 Grade Criteria

| Marks | Grade |
|--------|-------|
| 90 - 100 | A+ |
| 80 - 89 | A |
| 70 - 79 | B |
| 60 - 69 | C |
| 50 - 59 | D |
| Below 50 | F |

---

## 📚 Python Concepts Used

- Functions
- Dictionaries
- Loops
- Conditional Statements
- File Handling
- JSON Serialization
- Exception Handling
- Sorting
- Modular Programming

---

## 🔮 Future Improvements

- SQLite Database Integration
- Tkinter GUI
- Login Authentication
- Export Student Report to PDF
- CSV Import/Export
- Attendance Management
- Subject-wise Marks
- GPA Calculation

---

## 👨‍💻 Author

**Yashvir Bhardwaj**

- GitHub: https://github.com/Yashvir10
- LinkedIn: https://www.linkedin.com/in/yashvirbhardwaj

---

## 📜 License

This project is licensed under the MIT License.