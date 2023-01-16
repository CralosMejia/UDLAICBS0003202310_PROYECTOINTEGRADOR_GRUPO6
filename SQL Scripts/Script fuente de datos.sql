DROP DATABASE IF EXISTS datasource;
CREATE DATABASE datasource;

USE datasource;


DROP TABLE IF EXISTS asignatura;
create table asignatura(
id  int primary key auto_increment,
nombre varchar(250),
area_academica varchar(250)
);


DROP TABLE IF EXISTS estudiante;
create table estudiante(
id  int primary key auto_increment,
nombre varchar(250),
genero varchar(250),
segundo_nombre varchar(250),
apellido_paterno varchar(250),
apellido_materno varchar(250),
direccion varchar(250),
telefono_rep varchar(10),
cedula_rep varchar(10)
);

DROP TABLE IF EXISTS calificacion;
create table calificacion(
id  int primary key auto_increment,
nombre varchar(250),
calificacion varchar(250),
quimestre varchar(250),
asignaturaId int,
estudianteId int,
-- relacion asignatura y estudiante
constraint fk_asignatura_calificacion foreign key (asignaturaId) references asignatura(id),
constraint fk_estudiante foreign key (estudianteId) references estudiante(id)
);

DROP TABLE IF exists profesor;
CREATE table profesor(
id int primary key auto_increment, 
nombre varchar(250),
segundo_nombre varchar(250),
apellido_paterno varchar(250),
genero varchar(250),
apellido_materno varchar(250),
direccion varchar(250),
telefono varchar(10),
cedula varchar(10),
sueldo varchar(250)
);

drop table if exists asignatura_profesor;
create table asignatura_profesor(
id int primary key auto_increment, 
asignaturaId int,
profesorId int,
constraint fk_asignatura foreign key (asignaturaId) references asignatura(id),
constraint fk_profesor foreign key (profesorId) references profesor(id)
);



