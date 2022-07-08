create database tabelagastos;
use tabelagastos;

create table mes(
codigo int primary key auto_increment not null,
mesAno varchar(100) not null,
ganho varchar(100) not null
) Engine = InnoDB;

create table gastos(
codigo int primary key auto_increment not null,
dia int not null,
periodo varchar(100) not null,
item varchar(150) not null,
valor varchar(100) not null,
onde varchar(100) not null,
forma varchar(100) not null
) Engine = InnoDB;