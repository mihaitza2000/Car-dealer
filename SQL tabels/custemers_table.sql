-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Mar 21, 2022 at 08:13 PM
-- Server version: 10.4.22-MariaDB
-- PHP Version: 8.1.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `car dealer`
--

-- --------------------------------------------------------

--
-- Table structure for table `custemers_table`
--

CREATE TABLE `custemers_table` (
  `Name` varchar(20) NOT NULL,
  `Surname` varchar(20) NOT NULL,
  `ID` varchar(6) NOT NULL,
  `Date` date NOT NULL,
  `Time` varchar(10) NOT NULL,
  `Verification code` int(6) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `custemers_table`
--

INSERT INTO `custemers_table` (`Name`, `Surname`, `ID`, `Date`, `Time`, `Verification code`) VALUES
('Croitoru', 'Vasile', '21256', '2022-03-21', '20:25:07', 242263);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
