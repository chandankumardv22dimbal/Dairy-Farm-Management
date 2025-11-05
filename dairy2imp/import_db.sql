-- -------------------------------------------------
-- Create and use the database
-- -------------------------------------------------
DROP DATABASE IF EXISTS gowri;
CREATE DATABASE IF NOT EXISTS gowri
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;
USE gowri;

-- -------------------------------------------------
-- 1. Animals table
-- -------------------------------------------------
CREATE TABLE IF NOT EXISTS animals (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    species VARCHAR(50),
    breed VARCHAR(50),
    age INT,
    gender ENUM('Male', 'Female') DEFAULT 'Female',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- -------------------------------------------------
-- 2. Milk production table (linked to animals)
-- -------------------------------------------------
CREATE TABLE IF NOT EXISTS milk_production (
    id INT AUTO_INCREMENT PRIMARY KEY,
    animal_id INT NOT NULL,
    date DATE NOT NULL,
    quantity_liters DECIMAL(5,2) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (animal_id) REFERENCES animals(id) ON DELETE CASCADE
);

-- -------------------------------------------------
-- 3. Feed records table (linked to animals)
-- -------------------------------------------------
CREATE TABLE IF NOT EXISTS feed_records (
    id INT AUTO_INCREMENT PRIMARY KEY,
    animal_id INT NOT NULL,
    feed_type VARCHAR(100),
    quantity_kg DECIMAL(5,2),
    date DATE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (animal_id) REFERENCES animals(id) ON DELETE CASCADE
);

-- -------------------------------------------------
-- 4. Health records table (linked to animals)
-- -------------------------------------------------
CREATE TABLE IF NOT EXISTS health_records (
    id INT AUTO_INCREMENT PRIMARY KEY,
    animal_id INT NOT NULL,
    date DATE NOT NULL,
    issue VARCHAR(255),
    treatment VARCHAR(255),
    vet_name VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (animal_id) REFERENCES animals(id) ON DELETE CASCADE
);

-- -------------------------------------------------
-- 5. Employees table
-- -------------------------------------------------
CREATE TABLE IF NOT EXISTS employees (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    role VARCHAR(100),
    contact VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- -------------------------------------------------
-- 6. Assignments table (to link employees with animals)
-- -------------------------------------------------
CREATE TABLE IF NOT EXISTS assignments (
    id INT AUTO_INCREMENT PRIMARY KEY,
    employee_id INT NOT NULL,
    animal_id INT NOT NULL,
    task VARCHAR(255),
    date DATE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (employee_id) REFERENCES employees(id) ON DELETE CASCADE,
    FOREIGN KEY (animal_id) REFERENCES animals(id) ON DELETE CASCADE
);

-- -------------------------------------------------
-- Sample Data (Indian context)
-- -------------------------------------------------

-- 🐄 Animals
INSERT INTO animals (name, species, breed, age, gender) VALUES
('Gauri', 'Cow', 'Gir', 5, 'Female'),
('Lakshmi', 'Cow', 'Sahiwal', 4, 'Female'),
('Rani', 'Buffalo', 'Murrah', 6, 'Female'),
('Kaveri', 'Goat', 'Jamunapari', 3, 'Female'),
('Meena', 'Cow', 'Red Sindhi', 2, 'Female'),
('Radha', 'Goat', 'Beetal', 4, 'Female'),
('Gopal', 'Bull', 'Ongole', 7, 'Male');

-- 👨‍🌾 Employees
INSERT INTO employees (name, role, contact) VALUES
('Ramesh Kumar', 'Milker', '9876543210'),
('Priya Sharma', 'Vet', '9876501234'),
('Anil Singh', 'Farm Manager', '9123456780'),
('Kavita Das', 'Cleaner', '9988776655'),
('Manoj Patel', 'Feeder', '9001122334'),
('Sneha Iyer', 'Assistant Vet', '9784561230'),
('Rahul Verma', 'Technician', '9898989898');

-- 🥛 Milk Production
INSERT INTO milk_production (animal_id, date, quantity_liters) VALUES
(1, '2025-10-14', 14.5),
(2, '2025-10-14', 12.8),
(3, '2025-10-14', 18.3),
(5, '2025-10-14', 10.2),
(1, '2025-10-15', 15.0),
(2, '2025-10-15', 13.1),
(3, '2025-10-15', 19.0);

-- 🌾 Feed Records
INSERT INTO feed_records (animal_id, feed_type, quantity_kg, date) VALUES
(1, 'Dry Grass', 5.0, '2025-10-14'),
(2, 'Green Fodder', 6.5, '2025-10-14'),
(3, 'Cotton Cake', 4.2, '2025-10-14'),
(4, 'Maize', 3.0, '2025-10-14'),
(5, 'Soybean Meal', 4.8, '2025-10-14'),
(6, 'Dry Grass', 3.5, '2025-10-14'),
(7, 'Mixed Fodder', 6.0, '2025-10-14');

-- 🏥 Health Records
INSERT INTO health_records (animal_id, date, issue, treatment, vet_name) VALUES
(1, '2025-09-30', 'Minor cold', 'Vitamin supplement', 'Priya Sharma'),
(2, '2025-10-01', 'Mastitis', 'Antibiotic course', 'Sneha Iyer'),
(3, '2025-10-05', 'Foot rot', 'Footbath treatment', 'Priya Sharma'),
(4, '2025-10-07', 'Dehydration', 'ORS & fluids', 'Priya Sharma'),
(5, '2025-10-10', 'Fever', 'Paracetamol injection', 'Sneha Iyer'),
(6, '2025-10-11', 'Worm infection', 'Deworming syrup', 'Priya Sharma'),
(7, '2025-10-12', 'None', 'Routine check', 'Sneha Iyer');

-- 🧾 Assignments
INSERT INTO assignments (employee_id, animal_id, task, date) VALUES
(1, 1, 'Morning milking', '2025-10-14'),
(1, 2, 'Evening milking', '2025-10-14'),
(5, 3, 'Feed preparation', '2025-10-14'),
(4, 4, 'Cleaning goat shed', '2025-10-14'),
(2, 5, 'Routine health check', '2025-10-14'),
(6, 6, 'Vaccination', '2025-10-14'),
(3, 7, 'Farm supervision', '2025-10-14');
