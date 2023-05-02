CREATE DATABASE test07;

CREATE TABLE accounts (
  `id` INT PRIMARY KEY AUTO_INCREMENT,
  `username` varchar(255) NOT NULL,
  `password` VARCHAR(255) NOT NULL,
  `email` varchar(255) NOT NULL
);

CREATE TABLE patients (
  `id` INT PRIMARY KEY AUTO_INCREMENT,
  `fullname` VARCHAR(255) NOT NULL,
  `dateofbirth` varchar(255) NOT NULL,
  `address` VARCHAR(255) NOT NULL,
  `phonenumber` VARCHAR(255) NOT NULL
);

CREATE TABLE doctors (
  `id` INT PRIMARY KEY AUTO_INCREMENT,
  `fullname` VARCHAR(255) NOT NULL,
  `speciality` VARCHAR(255) NOT NULL,
  `address` VARCHAR(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `phonenumber` VARCHAR(255) NOT NULL
);

CREATE TABLE appointments (
  `id` INT PRIMARY KEY AUTO_INCREMENT,
  `dateandtime` varchar(255) NOT NULL,
  `reasonofthevisit` varchar(100) NOT NULL,
  `fullnameandspecialtydoctor` varchar(255) NOT NULL
);