-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Oct 07, 2024 at 04:46 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `MyPhysio`
--

-- --------------------------------------------------------

--
-- Table structure for table `Agenda Medica`
--

CREATE TABLE `Agenda Medica` (
  `ID Consulta` int(20) NOT NULL,
  `ID Doctor` int(20) NOT NULL,
  `ID Paciente` int(20) NOT NULL,
  `Fecha` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `Citas Medicas`
--

CREATE TABLE `Citas Medicas` (
  `ID Consulta` int(20) NOT NULL,
  `ID Doctor` int(20) NOT NULL,
  `ID Paciente` int(20) NOT NULL,
  `ID Receta` int(20) NOT NULL,
  `Fecha` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `Fisioterapeutas`
--

CREATE TABLE `Fisioterapeutas` (
  `ID Doctor` int(20) NOT NULL,
  `Nombre` varchar(70) NOT NULL,
  `Especialidad` varchar(50) NOT NULL,
  `Telefono` int(15) NOT NULL,
  `Correo` varchar(30) NOT NULL,
  `ID Paciente` int(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `Pacientes`
--

CREATE TABLE `Pacientes` (
  `ID Paciente` int(20) NOT NULL,
  `Nombre` varchar(70) NOT NULL,
  `Edad` int(3) NOT NULL,
  `Telefono` varchar(15) NOT NULL,
  `Correo` varchar(30) NOT NULL,
  `Historial Clinico` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `Receta Medica`
--

CREATE TABLE `Receta Medica` (
  `ID Receta` int(20) NOT NULL,
  `ID Doctor` int(20) NOT NULL,
  `ID Paciente` int(20) NOT NULL,
  `ID Consulta` int(20) NOT NULL,
  `Receta Medica` varchar(100) NOT NULL,
  `Fecha` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `Reportes Medicos`
--

CREATE TABLE `Reportes Medicos` (
  `ID Reporte` int(20) NOT NULL,
  `ID Doctor` int(20) NOT NULL,
  `ID Paciente` int(20) NOT NULL,
  `ID Consulta` int(20) NOT NULL,
  `ID Receta` int(20) NOT NULL,
  `Fecha` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `Agenda Medica`
--
ALTER TABLE `Agenda Medica`
  ADD KEY `ID Consulta` (`ID Consulta`),
  ADD KEY `ID Doctor` (`ID Doctor`),
  ADD KEY `ID Paciente` (`ID Paciente`);

--
-- Indexes for table `Citas Medicas`
--
ALTER TABLE `Citas Medicas`
  ADD PRIMARY KEY (`ID Consulta`),
  ADD KEY `ID Doctor` (`ID Doctor`),
  ADD KEY `ID Paciente` (`ID Paciente`),
  ADD KEY `ID Receta` (`ID Receta`);

--
-- Indexes for table `Fisioterapeutas`
--
ALTER TABLE `Fisioterapeutas`
  ADD PRIMARY KEY (`ID Doctor`),
  ADD KEY `ID Paciente` (`ID Paciente`);

--
-- Indexes for table `Pacientes`
--
ALTER TABLE `Pacientes`
  ADD PRIMARY KEY (`ID Paciente`);

--
-- Indexes for table `Receta Medica`
--
ALTER TABLE `Receta Medica`
  ADD PRIMARY KEY (`ID Receta`),
  ADD KEY `ID Doctor` (`ID Doctor`),
  ADD KEY `ID Paciente` (`ID Paciente`),
  ADD KEY `ID Consulta` (`ID Consulta`);

--
-- Indexes for table `Reportes Medicos`
--
ALTER TABLE `Reportes Medicos`
  ADD PRIMARY KEY (`ID Reporte`),
  ADD KEY `ID Doctor` (`ID Doctor`),
  ADD KEY `ID Paciente` (`ID Paciente`),
  ADD KEY `ID Consulta` (`ID Consulta`),
  ADD KEY `ID Receta` (`ID Receta`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `Fisioterapeutas`
--
ALTER TABLE `Fisioterapeutas`
  MODIFY `ID Doctor` int(20) NOT NULL AUTO_INCREMENT;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `Fisioterapeutas`
--
ALTER TABLE `Fisioterapeutas`
  ADD CONSTRAINT `Fisioterapeutas_ibfk_1` FOREIGN KEY (`ID Paciente`) REFERENCES `Pacientes` (`ID Paciente`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
