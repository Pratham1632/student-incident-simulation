from db_config import get_connection
import datetime

def log_incident(student_id, description):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO incidents (student_id, issue_description) VALUES (%s, %s)",
        (student_id, description)
    )
    conn.commit()
    conn.close()

def resolve_incident(incident_id, resolution):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE incidents SET status = 'Resolved', resolution = %s, resolved_at = NOW() WHERE incident_id = %s",
        (resolution, incident_id)
    )
    conn.commit()
    conn.close()

def list_open_incidents():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM incidents WHERE status = 'Open'")
    for row in cursor.fetchall():
        print(row)
    conn.close()