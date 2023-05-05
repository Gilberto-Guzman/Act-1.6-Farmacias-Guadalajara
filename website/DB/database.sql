CREATE DATABASE farmaciasguadalajara;

CREATE TABLE accounts (
  `id` INT PRIMARY KEY AUTO_INCREMENT,
  `username` varchar(255) NOT NULL,
  `password` VARCHAR(255) NOT NULL,
  `email` varchar(255) NOT NULL
);

INSERT INTO `accounts` (`id`, `username`, `password`, `email`) VALUES ('-1', 'Administrador', '710b770229a840318f61fa9257a5bf7acc2be3e70001efad', 'adminfarmaciasguadalajara')

INSERT INTO accounts (username, password, email) VALUES 
("juan123", "contraseña123", "juan123@gmail.com"),
("maria456", "abcd1234", "maria456@hotmail.com"),
("pedro789", "qwerty789", "pedro789@yahoo.com"),
("laura012", "asdfg012", "laura012@gmail.com"),
("carlos345", "zxcvb345", "carlos345@hotmail.com"),
("ana678", "contraseña678", "ana678@yahoo.com"),
("roberto901", "roberto123", "roberto901@gmail.com"),
("sofia234", "sofia456", "sofia234@hotmail.com"),
("luisa567", "luisa789", "luisa567@gmail.com"),
("jose890", "jose012", "jose890@yahoo.com");


CREATE TABLE patients (
  `id` INT PRIMARY KEY AUTO_INCREMENT,
  `fullname` VARCHAR(255) NOT NULL,
  `dateofbirth` varchar(255) NOT NULL,
  `address` VARCHAR(255) NOT NULL,
  `phonenumber` VARCHAR(255) NOT NULL
);

INSERT INTO patients (fullname, dateofbirth, address, phonenumber) VALUES 
("Juan Pérez", "1990-06-10", "Calle 123, Ciudad de México", "55-1234-5678"),
("María González", "1985-03-15", "Av. Principal 456, Guadalajara", "33-5678-1234"),
("Pedro García", "1978-11-25", "Colonia San Francisco, Monterrey", "81-2468-1357"),
("Ana Torres", "1995-09-03", "Paseo de la Reforma 789, Ciudad de México", "55-2468-3579"),
("Luisa Gómez", "1980-04-20", "Avenida del Sol 345, Tijuana", "664-1357-2468"),
("Carlos Rodríguez", "1972-12-18", "Calle 1 de Mayo 234, Veracruz", "229-3579-4681"),
("Miguel Fernández", "1988-08-08", "Callejón del Beso 987, Guanajuato", "473-2468-3579"),
("Sofía Sánchez", "1992-05-30", "Avenida Hidalgo 654, Puebla", "222-4681-3579"),
("Jorge Hernández", "1975-02-14", "Calle del Carmen 321, Ciudad de México", "55-1234-3579"),
("Alicia Ramírez", "1997-10-01", "Colonia Juárez 876, Cancún", "998-1357-2468");


CREATE TABLE doctors (
  `id` INT PRIMARY KEY AUTO_INCREMENT,
  `fullname` VARCHAR(255) NOT NULL,
  `speciality` VARCHAR(255) NOT NULL,
  `address` VARCHAR(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `phonenumber` VARCHAR(255) NOT NULL
);

INSERT INTO doctors (fullname, speciality, address, email, phonenumber) VALUES 
("Dr. Alejandro Rodríguez", "Cardiología", "Avenida de los Insurgentes 123, Ciudad de México", "arodriguez@hospital.com", "55-1234-5678"),
("Dra. Ana García", "Oncología", "Colonia del Valle 456, Monterrey", "agarcia@hospital.com", "81-2468-1357"),
("Dr. José González", "Pediatría", "Paseo de la Reforma 789, Ciudad de México", "jgonzalez@hospital.com", "55-2468-3579"),
("Dra. Laura Sánchez", "Ginecología", "Avenida del Sol 345, Tijuana", "lsanchez@hospital.com", "664-1357-2468"),
("Dr. Francisco Pérez", "Neurología", "Calle 1 de Mayo 234, Veracruz", "fperez@hospital.com", "229-3579-4681"),
("Dra. María Hernández", "Dermatología", "Callejón del Beso 987, Guanajuato", "mhernandez@hospital.com", "473-2468-3579"),
("Dr. Carlos Torres", "Traumatología", "Avenida Hidalgo 654, Puebla", "ctorres@hospital.com", "222-4681-3579"),
("Dra. Ana López", "Psiquiatría", "Calle del Carmen 321, Ciudad de México", "alopez@hospital.com", "55-1234-3579"),
("Dr. Juan Ramírez", "Urología", "Colonia Juárez 876, Cancún", "jramirez@hospital.com", "998-1357-2468"),
("Dra. Sofía Gómez", "Endocrinología", "Calle 123, Ciudad de México", "sgomez@hospital.com", "55-1234-5678");


CREATE TABLE appointments (
  `id` INT PRIMARY KEY AUTO_INCREMENT,
  `patientname` varchar(255) NOT NULL,  
  `dateandtime` varchar(255) NOT NULL,
  `reasonofthevisit` varchar(100) NOT NULL,
  `fullnameandspecialitydoctor` varchar(255) NOT NULL
);

INSERT INTO appointments (patientname, dateandtime, reasonofthevisit, fullnameandspecialitydoctor) VALUES 
("María Fernández", "2023-05-10 10:00:00", "Control de embarazo", "Dra. Ana García (Oncología)"),
("Pedro Martínez", "2023-05-15 15:30:00", "Dolor de espalda", "Dr. Carlos Torres (Traumatología)"),
("Luisa González", "2023-05-17 09:00:00", "Revisión anual", "Dr. José González (Pediatría)"),
("Sofía Hernández", "2023-05-20 14:15:00", "Mareos y vértigo", "Dr. Francisco Pérez (Neurología)"),
("Juan Pérez", "2023-05-22 16:00:00", "Dolor de cabeza", "Dra. Laura Sánchez (Ginecología)"),
("María García", "2023-05-25 11:30:00", "Consulta general", "Dr. Alejandro Rodríguez (Cardiología)"),
("Jorge Ramírez", "2023-05-27 08:45:00", "Control de presión arterial", "Dra. Sofía Gómez (Endocrinología)"),
("Ana Torres", "2023-05-30 12:30:00", "Control de diabetes", "Dra. María Hernández (Dermatología)"),
("José Martínez", "2023-06-01 10:45:00", "Revisión de rutina", "Dr. Juan Ramírez (Urología)"),
("Isabel López", "2023-06-05 17:15:00", "Consulta por dolor en articulaciones", "Dr. Carlos Torres (Traumatología)");


