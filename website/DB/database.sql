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

INSERT INTO accounts (username, password, email) VALUES
('juanperez', 'abc123', 'juanperez@example.com'),
('mgarci89', '123456', 'maria.garcia@example.com'),
('jlopez22', 'pass123', 'jlopez@example.com'),
('carlos95', 'qwerty', 'carlos@example.com'),
('lauram', 'secret12', 'laura@example.com'),
('alejandro77', 'p4ssw0rd', 'alejandro@example.com'),
('ana2010', '987654', 'ana@example.com'),
('pablo23', '54321', 'pablo@example.com'),
('sofia8', 'mypass', 'sofia@example.com');


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

INSERT INTO patients (fullname, dateofbirth, address, phonenumber) VALUES
('Juan Pérez', '1990-05-15', 'Calle Mayor 123, Madrid', '1234567890'),
('María García', '1985-12-10', 'Avenida Principal 456, Barcelona', '9876543210'),
('Pedro López', '1992-09-20', 'Calle Secundaria 789, Valencia', '5555555555'),
('Laura Martínez', '1998-03-25', 'Carrera Central 789, Sevilla', '9999999999'),
('Carlos Rodríguez', '1975-07-02', 'Plaza Principal 456, Zaragoza', '1111111111'),
('Ana Sánchez', '1980-11-18', 'Avenida Secundaria 789, Málaga', '2222222222'),
('Luis Torres', '1995-08-07', 'Calle Central 123, Bilbao', '3333333333'),
('Sofía Ramírez', '1993-01-30', 'Carrera Principal 456, Palma de Mallorca', '4444444444'),
('Diego Castro', '1987-06-12', 'Plaza Secundaria 789, Granada', '6666666666'),
('Elena Vargas', '1991-04-28', 'Avenida Central 123, Alicante', '7777777777');


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

INSERT INTO doctors (fullname, speciality, address, email, phonenumber) VALUES
('Dr. Juan Pérez', 'Cardiología', 'Calle Mayor 123, Madrid', 'juanperez@example.com', '1234567890'),
('Dra. María García', 'Pediatría', 'Avenida Principal 456, Barcelona', 'mariagarcia@example.com', '9876543210'),
('Dr. Pedro López', 'Cirugía General', 'Calle Secundaria 789, Valencia', 'pedrolopez@example.com', '5555555555'),
('Dra. Laura Martínez', 'Ginecología', 'Carrera Central 789, Sevilla', 'lauramartinez@example.com', '9999999999'),
('Dr. Carlos Rodríguez', 'Dermatología', 'Plaza Principal 456, Zaragoza', 'carlosrodriguez@example.com', '1111111111'),
('Dra. Ana Sánchez', 'Oftalmología', 'Avenida Secundaria 789, Málaga', 'anasanchez@example.com', '2222222222'),
('Dr. Luis Torres', 'Ortopedia', 'Calle Central 123, Bilbao', 'luistorres@example.com', '3333333333'),
('Dra. Sofía Ramírez', 'Endocrinología', 'Carrera Principal 456, Palma de Mallorca', 'sofiaramirez@example.com', '4444444444'),
('Dr. Diego Castro', 'Psiquiatría', 'Plaza Secundaria 789, Granada', 'diegocastro@example.com', '6666666666'),
('Dra. Elena Vargas', 'Neurología', 'Avenida Central 123, Alicante', 'elenavargas@example.com', '7777777777');


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

INSERT INTO appointments (patientname, dateandtime, reasonofthevisit, fullnameandspecialitydoctor) VALUES
('Juan Pérez', '2023-05-15 10:00', 'Examen de rutina', 'Dr. Juan Pérez - Cardiología'),
('María García', '2023-05-16 15:30', 'Control de vacunación', 'Dra. María García - Pediatría'),
('Pedro López', '2023-05-17 11:45', 'Consulta preoperatoria', 'Dr. Pedro López - Cirugía General'),
('Laura Martínez', '2023-05-18 09:15', 'Seguimiento de embarazo', 'Dra. Laura Martínez - Ginecología'),
('Carlos Rodríguez', '2023-05-19 14:00', 'Dermatitis crónica', 'Dr. Carlos Rodríguez - Dermatología'),
('Ana Sánchez', '2023-05-20 16:30', 'Revisión de la vista', 'Dra. Ana Sánchez - Oftalmología'),
('Luis Torres', '2023-05-21 10:30', 'Consulta por dolor de rodilla', 'Dr. Luis Torres - Ortopedia'),
('Sofía Ramírez', '2023-05-22 12:45', 'Control de tiroides', 'Dra. Sofía Ramírez - Endocrinología'),
('Diego Castro', '2023-05-23 14:30', 'Seguimiento de tratamiento', 'Dr. Diego Castro - Psiquiatría'),
('Elena Vargas', '2023-05-24 11:15', 'Evaluación neurológica', 'Dra. Elena Vargas - Neurología');


