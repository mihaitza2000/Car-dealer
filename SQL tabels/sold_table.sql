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
-- Table structure for table `sold_table`
--

CREATE TABLE `sold_table` (
  `Car VIN` varchar(20) NOT NULL,
  `Licence plate` varchar(10) NOT NULL,
  `Manuf. Year` int(3) NOT NULL,
  `Customer ID` int(6) NOT NULL,
  `Date` date NOT NULL,
  `Time` varchar(10) NOT NULL,
  `Verification code` varchar(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `sold_table`
--

INSERT INTO `sold_table` (`Car VIN`, `Licence plate`, `Manuf. Year`, `Customer ID`, `Date`, `Time`, `Verification code`) VALUES
('HXPRS4277659539PD', 'SA 97 SWQ', 2004, 77817, '2022-03-21', '20:25:07', '242263');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
