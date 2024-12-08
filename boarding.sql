CREATE DATABASE findmyboarding;

USE findmyboarding;

CREATE TABLE owner (
    id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL
);

CREATE TABLE listings (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255),
    image_path VARCHAR(255),
    address VARCHAR(255),
    distance_from_campus FLOAT,
    price FLOAT,
    facilities TEXT,
    contact VARCHAR(255),
    description TEXT,
    owner_id INT,
    FOREIGN KEY (owner_id) REFERENCES owner(id)
);

