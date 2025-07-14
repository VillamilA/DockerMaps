CREATE DATABASE IF NOT EXISTS ecuador;
USE ecuador;

CREATE TABLE provincias (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100),
    capital VARCHAR(100),
    area FLOAT,
    poblacion INT
);

INSERT INTO provincias (nombre, capital, area, poblacion) VALUES
('Pichincha', 'Quito', 9496.91, 2818000),
('Guayas', 'Guayaquil', 15300, 3913000),
('Azuay', 'Cuenca', 8309, 881000);
