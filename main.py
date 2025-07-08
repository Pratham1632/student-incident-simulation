import sqlite3
import datetime

# ---------- DB Setup ----------
conn = sqlite3.connect("student_incidents.db")
cursor = conn.cursor()

# Create tables
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    student_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    department TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS incidents (
    incident_id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER,
    incident_type TEXT,
    status TEXT DEFAULT 'Open',
    description TEXT,
    reported_on TEXT,
    resolved_on TEXT,
    FOREIGN KEY(student_id) REFERENCES students(student_id)
)
""")
conn.commit()

# ---------- CLI Actions ----------
def add_student():
    name = input("Enter student name: ")
    department = input("Enter department: ")
    cursor.execute("INSERT INTO students (name, department) VALUES (?, ?)", (name, department))
    conn.commit()
    print(f"✅ Student '{name}' added.\n")

def log_incident():
    student_id = input("Enter student ID: ")
    incident_type = input("Incident type (e.g., Misconduct, Attendance, Health): ")
    description = input("Incident description: ")
    reported_on = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    cursor.execute("""
        INSERT INTO incidents (student_id, incident_type, description, reported_on)
        VALUES (?, ?, ?, ?)
    """, (student_id, incident_type, description, reported_on))
    conn.commit()
    print(f"✅ Incident logged for Student ID {student_id}.\n")

def view_incidents():
    cursor.execute("""
        SELECT i.incident_id, s.name, i.incident_type, i.status, i.reported_on, i.resolved_on
        FROM incidents i
        JOIN students s ON i.student_id = s.student_id
        ORDER BY i.reported_on DESC
    """)
    rows = cursor.fetchall()

    if not rows:
        print("⚠️ No incidents found.\n")
        return

    print("\n--- Incident List ---")
    for row in rows:
        print(f"ID: {row[0]} | Student: {row[1]} | Type: {row[2]} | Status: {row[3]} | Reported: {row[4]} | Resolved: {row[5]}")
    print()

def update_status():
    incident_id = input("Enter incident ID to update: ")
    new_status = input("New status (Open / Investigating / Resolved): ")

    resolved_on = None
    if new_status.lower() == "resolved":
        resolved_on = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    cursor.execute("""
        UPDATE incidents
        SET status = ?, resolved_on = ?
        WHERE incident_id = ?
    """, (new_status, resolved_on, incident_id))
    conn.commit()
    print(f"✅ Incident {incident_id} status updated to '{new_status}'.\n")

# ---------- CLI Loop ----------
def menu():
    while True:
        print("\n===== Student Incident Management CLI =====")
        print("1. Add Student")
        print("2. Log New Incident")
        print("3. View All Incidents")
        print("4. Update Incident Status")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            log_incident()
        elif choice == "3":
            view_incidents()
        elif choice == "4":
            update_status()
        elif choice == "5":
            print("Exiting system. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.\n")

if __name__ == "__main__":
    menu()
    conn.close()
