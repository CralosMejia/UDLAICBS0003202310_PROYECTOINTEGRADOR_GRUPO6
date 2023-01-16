DROP DATABASE IF EXISTS stg;
CREATE DATABASE stg;
USE stg;


DROP TABLE IF EXISTS asignatura_ext;
create table asignatura_ext(
id  int primary key not null,
nombre varchar(250) not null,
area_academica varchar(250) not null
);


DROP TABLE IF EXISTS estudiante_ext;
create table estudiante_ext(
id  int primary key not null,
nombre varchar(250) not null,
genero varchar(250) not null,
segundo_nombre varchar(250) not null,
apellido_paterno varchar(250) not null,
apellido_materno varchar(250) not null,
direccion varchar(250) not null,
telefono_rep varchar(10) not null, 
cedula_rep varchar(10) not null
);

DROP TABLE IF EXISTS calificacion_ext;
create table calificacion_ext(
id  int primary key not null,
nombre varchar(250) not null,
calificacion varchar(250) not null,
quimestre varchar(250) not null,
asignaturaId int not null,
estudianteId int not null
);

DROP TABLE IF exists profesor_ext;
CREATE table profesor_ext(
id int primary key not null, 
nombre varchar(250) not null,
segundo_nombre varchar(250),
apellido_paterno varchar(250) not null,
genero varchar(250) not null,
apellido_materno varchar(250) ,
direccion varchar(250) not null,
telefono varchar(10) not null,
cedula varchar(10) not null,
sueldo varchar(250) not null
);

drop table if exists asignatura_profesor_ext;
create table asignatura_profesor_ext(
id int primary key not null, 
asignaturaId int not null,
profesorId int not null);

drop table if exists area_acad_ext;
create table area_acad_ext(
id int primary key not null,
nombre varchar(250) not null);

/*
---------------------
TRANSFORMATION tables
*/
-- Etl process table
DROP TABLE IF EXISTS etl_proc;
CREATE TABLE etl_proc(
	cod_etl bigint auto_increment primary key,
    created_at date not null
);

DROP TABLE IF EXISTS asignatura_tra;
create table asignatura_tra(
surrogate_key  int primary key auto_increment,
id int not null,
nombre varchar(150) not null,
area_academica int,
cod_etl bigint
);


DROP TABLE IF EXISTS estudiante_tra;
create table estudiante_tra(
surrogate_key  int primary key auto_increment,
id  int not null,
nombre_completo varchar(250) not null,
genero varchar(20) not null,
direccion varchar(250) not null,
telefono_rep varchar(10) not null, 
cedula_rep varchar(10) not null,
cod_etl bigint
);

DROP TABLE IF EXISTS calificacion_tra;
create table calificacion_tra(
surrogate_key  int primary key auto_increment,
id  int  not null,
nombre varchar(250) not null,
calificacion decimal(10,2)  not null,
quimestre smallint not null,
asignaturaId int not null,
estudianteId int not null,
cod_etl bigint
);

DROP TABLE IF exists profesor_tra;
CREATE table profesor_tra(
surrogate_key  int primary key auto_increment,
id int not null, 
nombre_completo varchar(250) not null,
genero varchar(20) not null,
direccion varchar(100) not null,
telefono varchar(10) not null,
cedula varchar(10) not null,
sueldo decimal(10,2)  not null,
cod_etl bigint
);

drop table if exists asignatura_profesor_tra;
create table asignatura_profesor_tra(
surrogate_key  int primary key auto_increment,
id int not null, 
asignaturaId int not null,
profesorId int not null,
cod_etl bigint);

drop table if exists area_acad_tra;
create table area_acad_tra(
surrogate_key  int primary key auto_increment,
id int not null,
nombre varchar(50) not null,
cod_etl bigint)




