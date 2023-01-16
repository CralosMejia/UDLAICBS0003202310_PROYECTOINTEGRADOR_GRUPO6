drop database if exists sor;
create database sor;

use sor;


DROP TABLE IF EXISTS asignatura_dim;
create table asignatura_dim(
surrogate_key  int primary key auto_increment,
id int not null,
nombre varchar(150) not null,
area_academica int,
cod_etl bigint
);


DROP TABLE IF EXISTS estudiante_dim;
create table estudiante_dim(
surrogate_key  int primary key auto_increment,
id  int not null,
nombre_completo varchar(250) not null,
genero varchar(20) not null,
direccion varchar(250) not null,
telefono_rep varchar(10) not null, 
cedula_rep varchar(10) not null,
cod_etl bigint
);

DROP TABLE IF EXISTS calificacion_fact;
create table calificacion_fact(
surrogate_key  int primary key auto_increment,
id  int  not null,
nombre varchar(250) not null,
calificacion decimal(10,2) not null,
quimestre smallint not null,
asignaturaId int not null,
estudianteId int not null,
profesorId int not null,
loadedAt datetime not null,
cod_etl bigint
);

DROP TABLE IF exists profesor_dim;
CREATE table profesor_dim(
surrogate_key  int primary key auto_increment,
id int not null, 
nombre_completo varchar(250) not null,
genero varchar(20) not null,
direccion varchar(100) not null,
telefono varchar(10) not null,
cedula varchar(10) not null,
sueldo decimal(10,2) not null,
cod_etl bigint
);

drop table if exists area_acad_dim;
create table area_acad_dim(
surrogate_key  int primary key auto_increment,
id int not null,
nombre varchar(50) not null,
cod_etl bigint);


-- CONSTRAINTS
ALTER TABLE `sor`.`asignatura_dim` 
ADD INDEX `asignatura_area_acad_fk_idx` (`area_academica` ASC)
;
ALTER TABLE `sor`.`asignatura_dim` 
ADD CONSTRAINT `asignatura_area_acad_fk`
  FOREIGN KEY (`area_academica`)
  REFERENCES `sor`.`area_acad_dim` (`surrogate_key`)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION;


ALTER TABLE `sor`.`calificacion_fact` 
ADD INDEX `fact_asignatura_fk_idx` (`asignaturaId` ASC) ,
ADD INDEX `fact_estudiante_fk_idx` (`estudianteId` ASC) ,
ADD INDEX `fact_profesor_fk_idx` (`profesorId` ASC) ;
ALTER TABLE `sor`.`calificacion_fact` 
ADD CONSTRAINT `fact_asignatura_fk`
  FOREIGN KEY (`asignaturaId`)
  REFERENCES `sor`.`asignatura_dim` (`surrogate_key`)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION,
ADD CONSTRAINT `fact_estudiante_fk`
  FOREIGN KEY (`estudianteId`)
  REFERENCES `sor`.`estudiante_dim` (`surrogate_key`)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION,
ADD CONSTRAINT `fact_profesor_fk`
  FOREIGN KEY (`profesorId`)
  REFERENCES `sor`.`profesor_dim` (`surrogate_key`)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION;

