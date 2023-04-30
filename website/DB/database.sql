CREATE DATABASE IF NOT EXISTS `farmaciasguadalajara` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `farmaciasguadalajara`;

CREATE TABLE IF NOT EXISTS `accounts` (
    `id` int(11) NOT NULL AUTO_INCREMENT,
    `username` varchar(50) NOT NULL,
    `password` varchar(255) NOT NULL,
    `email` varchar(100) NOT NULL ,
    PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS `appointments` (
    `id` int(11) NOT NULL AUTO_INCREMENT,
    `username` varchar(50) NOT NULL,
    `email` varchar(100) NOT NULL,
    `name` varchar(100) NOT NULL,
    `address` varchar(255) NOT NULL,
    `phonenumber` varchar(20) NOT NULL,
    `reasonofthevisit` varchar(100) NOT NULL,
    `dateandtime` varchar(100) NOT NULL,
    PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;












--BASE CHIDA--
CREATE DATABASE test04;

USE test04;
CREATE TABLE accounts (
  `id` INT PRIMARY KEY AUTO_INCREMENT,
  `username` varchar(255) NOT NULL,
  `password` VARCHAR(255) NOT NULL,
  `email` varchar(255) NOT NULL
);

CREATE TABLE patients (
  `id` INT PRIMARY KEY AUTO_INCREMENT,
  `full_name` VARCHAR(255) NOT NULL,
  `date_of_birth` varchar(255) NOT NULL,
  `address` VARCHAR(255) NOT NULL,
  `phone_number` VARCHAR(255) NOT NULL,
  `account_id` INT NOT NULL,
  FOREIGN KEY (`account_id`) REFERENCES accounts(`id`)
);

CREATE TABLE doctors (
  `id` INT PRIMARY KEY AUTO_INCREMENT,
  `first_name` VARCHAR(255) NOT NULL,
  `last_name` VARCHAR(255) NOT NULL,
  `specialty` VARCHAR(255) NOT NULL
);

CREATE TABLE appointments (
  `id` INT PRIMARY KEY AUTO_INCREMENT,
  `patient_id` INT NOT NULL,
  `doctor_id` INT NOT NULL,
  `date` DATE NOT NULL,
  `time` TIME NOT NULL,
  FOREIGN KEY (`patient_id`) REFERENCES patients(`id`),
  FOREIGN KEY (`doctor_id`) REFERENCES doctors(`id`)
);
