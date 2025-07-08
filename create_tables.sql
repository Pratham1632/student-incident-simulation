-- Create the database if it doesn't exist
CREATE DATABASE IF NOT EXISTS student_mgmt;

-- Use the student_mgmt database
USE student_mgmt;

-- Create the students table
CREATE TABLE IF NOT EXISTS students (
    student_id INT AUTO_INCREMENT PRIMARY KEY,   -- Unique ID for each student
    name VARCHAR(100) NOT NULL,                  -- Student name
    email VARCHAR(100) UNIQUE,                   -- Unique email ID
    course VARCHAR(100),                         -- Course enrolled
    status VARCHAR(20) DEFAULT 'Active'          -- Enrollment status (Active/Inactive/etc.)
);

-- Create the incidents table
CREATE TABLE IF NOT EXISTS incidents (
    incident_id INT AUTO_INCREMENT PRIMARY KEY,  -- Unique ID for each incident
    student_id INT NOT NULL,                     -- FK reference to students table
    issue_description TEXT NOT NULL,             -- Details of the incident
    status VARCHAR(20) DEFAULT 'Open',           -- Incident status (Open/Investigating/Resolved)
    resolution TEXT,                             -- Resolution notes
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- When incident was created
    resolved_at TIMESTAMP NULL,                  -- When incident was resolved
    FOREIGN KEY (student_id) REFERENCES students(student_id)
        ON DELETE CASCADE ON UPDATE CASCADE      -- Maintain referential integrity
);
