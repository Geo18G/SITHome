-- phpMyAdmin SQL Dump
-- version 4.9.7
-- https://www.phpmyadmin.net/
--
-- Servidor: localhost:3306
-- Tiempo de generación: 07-11-2022 a las 21:30:46
-- Versión del servidor: 5.7.33
-- Versión de PHP: 7.4.20

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `sithome`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `dispositivos`
--

CREATE TABLE `dispositivos` (
  `iddispositivos` int(11) NOT NULL,
  `nombre` varchar(45) DEFAULT NULL,
  `estado` varchar(1) DEFAULT '0',
  `habitaciones_idhabitaciones` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Volcado de datos para la tabla `dispositivos`
--

INSERT INTO `dispositivos` (`iddispositivos`, `nombre`, `estado`, `habitaciones_idhabitaciones`) VALUES
(1, 'foco', '0', 1),
(2, 'tele', '0', 2);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `habitaciones`
--

CREATE TABLE `habitaciones` (
  `idhabitaciones` int(11) NOT NULL,
  `nombre` varchar(45) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Volcado de datos para la tabla `habitaciones`
--

INSERT INTO `habitaciones` (`idhabitaciones`, `nombre`) VALUES
(1, 'sala'),
(2, 'cocina');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `permisos`
--

CREATE TABLE `permisos` (
  `usuarios_idusuarios` int(11) NOT NULL,
  `habitaciones_idhabitaciones` int(11) NOT NULL,
  `permiso` int(1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Volcado de datos para la tabla `permisos`
--

INSERT INTO `permisos` (`usuarios_idusuarios`, `habitaciones_idhabitaciones`, `permiso`) VALUES
(1, 1, 1),
(1, 2, 0),
(4, 1, 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `roles`
--

CREATE TABLE `roles` (
  `idroles` int(11) NOT NULL,
  `tipo` varchar(45) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Volcado de datos para la tabla `roles`
--

INSERT INTO `roles` (`idroles`, `tipo`) VALUES
(1, 'Administrador'),
(2, 'Usuario');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuarios`
--

CREATE TABLE `usuarios` (
  `idusuarios` int(11) NOT NULL,
  `nombreUsuario` varchar(45) NOT NULL,
  `contrasena` varchar(45) DEFAULT NULL,
  `roles_idroles` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Volcado de datos para la tabla `usuarios`
--

INSERT INTO `usuarios` (`idusuarios`, `nombreUsuario`, `contrasena`, `roles_idroles`) VALUES
(1, 'Geo', '111', 1),
(4, 'nacho', '123', 1);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `dispositivos`
--
ALTER TABLE `dispositivos`
  ADD PRIMARY KEY (`iddispositivos`),
  ADD KEY `fk_dispositivos_habitaciones1_idx` (`habitaciones_idhabitaciones`);

--
-- Indices de la tabla `habitaciones`
--
ALTER TABLE `habitaciones`
  ADD PRIMARY KEY (`idhabitaciones`);

--
-- Indices de la tabla `permisos`
--
ALTER TABLE `permisos`
  ADD PRIMARY KEY (`usuarios_idusuarios`,`habitaciones_idhabitaciones`),
  ADD KEY `fk_usuarios_has_habitaciones_habitaciones1_idx` (`habitaciones_idhabitaciones`),
  ADD KEY `fk_usuarios_has_habitaciones_usuarios1_idx` (`usuarios_idusuarios`);

--
-- Indices de la tabla `roles`
--
ALTER TABLE `roles`
  ADD PRIMARY KEY (`idroles`);

--
-- Indices de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  ADD PRIMARY KEY (`idusuarios`),
  ADD UNIQUE KEY `nombre_UNIQUE` (`nombreUsuario`),
  ADD KEY `fk_usuarios_roles1_idx` (`roles_idroles`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `dispositivos`
--
ALTER TABLE `dispositivos`
  MODIFY `iddispositivos` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `habitaciones`
--
ALTER TABLE `habitaciones`
  MODIFY `idhabitaciones` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `roles`
--
ALTER TABLE `roles`
  MODIFY `idroles` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  MODIFY `idusuarios` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `dispositivos`
--
ALTER TABLE `dispositivos`
  ADD CONSTRAINT `fk_dispositivos_habitaciones1` FOREIGN KEY (`habitaciones_idhabitaciones`) REFERENCES `habitaciones` (`idhabitaciones`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Filtros para la tabla `permisos`
--
ALTER TABLE `permisos`
  ADD CONSTRAINT `fk_usuarios_has_habitaciones_habitaciones1` FOREIGN KEY (`habitaciones_idhabitaciones`) REFERENCES `habitaciones` (`idhabitaciones`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `fk_usuarios_has_habitaciones_usuarios1` FOREIGN KEY (`usuarios_idusuarios`) REFERENCES `usuarios` (`idusuarios`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Filtros para la tabla `usuarios`
--
ALTER TABLE `usuarios`
  ADD CONSTRAINT `fk_usuarios_roles1` FOREIGN KEY (`roles_idroles`) REFERENCES `roles` (`idroles`) ON DELETE NO ACTION ON UPDATE NO ACTION;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
