CREATE DATABASE IF NOT EXISTS pertanian_db;

USE pertanian_db;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    role ENUM('petani', 'admin') NOT NULL
);