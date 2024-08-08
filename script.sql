CREATE DATABASE brain_tumor;
USE brain_tumor;

CREATE TABLE patients (
    id INT AUTO_INCREMENT PRIMARY KEY,
    NAME VARCHAR(100) NOT NULL,
    date_of_birth DATE,
    gender ENUM('0', '1'),
    contact_info VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

CREATE TABLE HISTORY (
    id INT AUTO_INCREMENT PRIMARY KEY,
    patient_id INT,
    flair_path VARCHAR(255) ,
    t1ce_path VARCHAR(255),
    t1_path VARCHAR(255),
    t2_path VARCHAR(255),
    segment_path VARCHAR(255),
    capture_date DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

CREATE TABLE doctors (
    id INT AUTO_INCREMENT PRIMARY KEY,
    NAME VARCHAR(100) NOT NULL,
    phone_number VARCHAR(100),
    contact_info VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

CREATE TABLE patient_doctor(
    id_patient INT,
    id_doctor INT,
    PRIMARY KEY (id_patient, id_doctor)
)
