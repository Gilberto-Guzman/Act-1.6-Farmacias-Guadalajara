CREATE DATABASE IF NOT EXISTS `farmaciasguadalajara` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `farmaciasguadalajara`;

CREATE TABLE IF NOT EXISTS `accounts` (
    `id` int(11) NOT NULL AUTO_INCREMENT,
    `username` varchar(50) NOT NULL,
    `password` varchar(255) NOT NULL,
    `email` varchar(100) NOT NULL,
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