-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Tempo de geração: 01-Jul-2022 às 00:40
-- Versão do servidor: 10.4.21-MariaDB
-- versão do PHP: 8.0.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Banco de dados: `nork_town`
--

-- --------------------------------------------------------

--
-- Estrutura da tabela `acesso`
--

CREATE TABLE `acesso` (
  `id` int(11) NOT NULL,
  `login` varchar(50) NOT NULL,
  `senha` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Extraindo dados da tabela `acesso`
--

INSERT INTO `acesso` (`id`, `login`, `senha`) VALUES
(1, 'admin', '123456');

-- --------------------------------------------------------

--
-- Estrutura da tabela `carros`
--

CREATE TABLE `carros` (
  `id` int(11) NOT NULL,
  `id_cliente` int(11) NOT NULL,
  `cor` varchar(50) NOT NULL,
  `modelo` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Extraindo dados da tabela `carros`
--

INSERT INTO `carros` (`id`, `id_cliente`, `cor`, `modelo`) VALUES
(3, 2, 'Azul', 'Hatch'),
(12, 1, 'Cinza', 'Hatch'),
(15, 1, 'Amarelo', 'Sedan'),
(19, 11, 'Azul', 'Hatch'),
(20, 11, 'Cinza', 'Sedan');

-- --------------------------------------------------------

--
-- Estrutura da tabela `clientes`
--

CREATE TABLE `clientes` (
  `id` int(11) NOT NULL,
  `nome` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Extraindo dados da tabela `clientes`
--

INSERT INTO `clientes` (`id`, `nome`) VALUES
(1, 'João'),
(2, 'Marcelo'),
(3, 'Lucas'),
(11, 'Rodrigo');

--
-- Índices para tabelas despejadas
--

--
-- Índices para tabela `acesso`
--
ALTER TABLE `acesso`
  ADD PRIMARY KEY (`id`);

--
-- Índices para tabela `carros`
--
ALTER TABLE `carros`
  ADD PRIMARY KEY (`id`),
  ADD KEY `carro_usuario` (`id_cliente`);

--
-- Índices para tabela `clientes`
--
ALTER TABLE `clientes`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de tabelas despejadas
--

--
-- AUTO_INCREMENT de tabela `acesso`
--
ALTER TABLE `acesso`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de tabela `carros`
--
ALTER TABLE `carros`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

--
-- AUTO_INCREMENT de tabela `clientes`
--
ALTER TABLE `clientes`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- Restrições para despejos de tabelas
--

--
-- Limitadores para a tabela `carros`
--
ALTER TABLE `carros`
  ADD CONSTRAINT `carro_usuario` FOREIGN KEY (`id_cliente`) REFERENCES `clientes` (`id`) ON DELETE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
