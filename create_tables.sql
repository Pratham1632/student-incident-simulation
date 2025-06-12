CREATE DATABASE IF NOT EXISTS student_mgmt;

USE student_mgmt;

CREATE TABLE IF NOT EXISTS students (
    student_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100) UNIQUE,
    course VARCHAR(100),
    status VARCHAR(20)
);

CREATE TABLE IF NOT EXISTS incidents (
    incident_id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT,
    issue_description TEXT,
    status VARCHAR(20) DEFAULT 'Open',
    resolution TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    resolved_at TIMESTAMP NULL,
    FOREIGN KEY (student_id) REFERENCES students(student_id)
);