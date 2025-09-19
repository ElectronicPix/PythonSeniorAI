-- Crear una base de datos
CREATE DATABASE tienda; 

USE tienda; -- Usar la base de datos

CREATE TABLE clientes( -- Crear tabla
	id int auto_increment primary key,
    nombre varchar(100) not null, 
    correo varchar(100) unique, 
    edad int
);

-- Insertar datos
insert into clientes (nombre, correo, edad)
values('Rubén', 'Ruben@gmail.com', 25);

-- Consultar la información 
select nombre from clientes;
select nombre, correo, edad from clientes; -- Traer toda la información
select * from clientes; -- * Llamar todo

-- Editar la información
