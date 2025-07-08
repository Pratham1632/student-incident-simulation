# 🎓 Student Management Incident Simulation System

A simple CLI-based Python application to simulate student incident tracking workflows.  
Built with **SQLite** as the backend and **Python** for managing real-world scenarios like misconduct, health issues, or academic concerns.

---

## 🚀 Features

- Add and manage students
- Log incidents with details
- Track, update, and resolve incidents
- SQLite-based persistent storage
- CLI interface for real-world simulation

---

## 🛠️ Tech Stack

- Python 3
- SQLite3 (via `sqlite3` module – built-in)

---

## 🧩 How It Works

- Student data is stored in a `students` table.
- Incidents are linked to students via `student_id`.
- Statuses include **Open**, **Investigating**, and **Resolved**.
- Timestamps are logged for reported and resolved events.

---

## 📥 Setup Instructions

```bash
# Clone the repository
git clone https://github.com/Pratham1632/student-incident-simulation.git
cd student-incident-simulation

# Run the system
python student_incident_system.py
