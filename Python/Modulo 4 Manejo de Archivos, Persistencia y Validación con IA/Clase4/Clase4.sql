-- Crear una base de datos
CREATE DATABASE tienda; 

USE tienda; -- Usar la base de datos

-- Crear tabla
CREATE TABLE clientes( 
	id int auto_increment primary key,
    nombre varchar(100) not null, 
    correo varchar(100) unique, 
    edad int
);

-- Insertar datos
insert into clientes (nombre, correo, edad)
values('Joel', 'joel@gmail.com', 40);

-- Consultar la información 
select nombre from clientes;
select nombre, correo, edad from clientes; -- Traer toda la información
select * from clientes; -- * Llamar todo

-- Editar la información
update clientes set edad = 20 where id = 2; -- solo el id 2
update clientes set nombre  = lower(nombre); -- nombre en minusculas - quitar seguridad

-- Delete 
delete from clientes; -- No permitido
delete from clientes where id = 4;
delete from clientes where correo is null; -- Eliminar los correos vacios


-- Desabilitar seguridad
start transaction; -- control + Z hacer antes de la prueba, devolverme en casa de que requiera
set SQL_SAFE_UPDATES=0; -- deshabilitar seguridad 
rollback; -- devolver la información, desacer los cambios
set SQL_SAFE_UPDATES=1; -- habilitar seguridad
commit; -- Si todo está bien 

-- Filtros
select * from clientes where id = 1;
select * from clientes where edad > 25;
select * from clientes where nombre like 'j%';



-- Muchos datos 
insert into clientes (nombre, correo, edad) values('Carlos', 'carlos.g@gmail.com', 28);
insert into clientes (nombre, correo, edad) values('Ana', 'ana.martinez@hotmail.com', 34);
insert into clientes (nombre, correo, edad) values('Juan', 'juan.perez@yahoo.com', 45);
insert into clientes (nombre, correo, edad) values('Maria', 'maria_r@gmail.com', 22);
insert into clientes (nombre, correo, edad) values('Luis', 'luis.fernandez@outlook.com', 51);
insert into clientes (nombre, correo, edad) values('Laura', 'laura.gomez@gmail.com', 30);
insert into clientes (nombre, correo, edad) values('Jose', 'jose.d@yahoo.com', 42);
insert into clientes (nombre, correo, edad) values('Sofia', 'sofia.lopez@hotmail.com', 29);
insert into clientes (nombre, correo, edad) values('Miguel', 'miguel.angel@gmail.com', 38);
insert into clientes (nombre, correo, edad) values('Elena', 'elena.sanchez@outlook.com', 25);
insert into clientes (nombre, correo, edad) values('David', 'david.romero@gmail.com', 33);
insert into clientes (nombre, correo, edad) values('Carmen', 'carmen.sosa@yahoo.com', 48);
insert into clientes (nombre, correo, edad) values('Francisco', 'f.torres@hotmail.com', 55);
insert into clientes (nombre, correo, edad) values('Isabel', 'isabel.diaz@gmail.com', 26);
insert into clientes (nombre, correo, edad) values('Antonio', 'antonio.ruiz@outlook.com', 41);
insert into clientes (nombre, correo, edad) values('Patricia', 'patricia.v@gmail.com', 37);
insert into clientes (nombre, correo, edad) values('Javier', 'javier.m@hotmail.com', 29);
insert into clientes (nombre, correo, edad) values('Lucia', 'lucia.gimenez@yahoo.com', 24);
insert into clientes (nombre, correo, edad) values('Daniel', 'daniel.moreno@gmail.com', 39);
insert into clientes (nombre, correo, edad) values('Marta', 'marta.h@outlook.com', 31);
insert into clientes (nombre, correo, edad) values('Manuel', 'manuel.alonso@gmail.com', 46);
insert into clientes (nombre, correo, edad) values('Cristina', 'cristina.p@hotmail.com', 27);
insert into clientes (nombre, correo, edad) values('Alejandro', 'alejandro.gutierrez@yahoo.com', 53);
insert into clientes (nombre, correo, edad) values('Paula', 'paula.navarro@gmail.com', 23);
insert into clientes (nombre, correo, edad) values('Sergio', 'sergio.iglesias@outlook.com', 36);
insert into clientes (nombre, correo, edad) values('Sara', 'sara.blanco@gmail.com', 32);
insert into clientes (nombre, correo, edad) values('Jorge', 'jorge.molina@hotmail.com', 49);
insert into clientes (nombre, correo, edad) values('Andrea', 'andrea.c@yahoo.com', 28);
insert into clientes (nombre, correo, edad) values('Fernando', 'fernando.castro@gmail.com', 58);
insert into clientes (nombre, correo, edad) values('Alba', 'alba.ortega@outlook.com', 21);
insert into clientes (nombre, correo, edad) values('Ricardo', 'ricardo.serrano@gmail.com', 44);
insert into clientes (nombre, correo, edad) values('Natalia', 'natalia.reyes@hotmail.com', 35);
insert into clientes (nombre, correo, edad) values('Roberto', 'roberto.gallego@yahoo.com', 50);
insert into clientes (nombre, correo, edad) values('Irene', 'irene.saez@gmail.com', 29);
insert into clientes (nombre, correo, edad) values('Eduardo', 'eduardo.vazquez@outlook.com', 43);
insert into clientes (nombre, correo, edad) values('Rocio', 'rocio.cano@gmail.com', 30);
insert into clientes (nombre, correo, edad) values('Oscar', 'oscar.campos@hotmail.com', 47);
insert into clientes (nombre, correo, edad) values('Monica', 'monica.vega@yahoo.com', 52);
insert into clientes (nombre, correo, edad) values('Victor', 'victor.santos@gmail.com', 26);
insert into clientes (nombre, correo, edad) values('Julia', 'julia.rios@outlook.com', 39);