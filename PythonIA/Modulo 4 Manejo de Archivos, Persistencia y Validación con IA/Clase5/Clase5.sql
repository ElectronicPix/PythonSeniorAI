create database relaciones;

use relaciones;

create table estudiantes(
	id int auto_increment primary key, 
    tipo_documento varchar(50), 
    documento varchar(50) unique, -- unique por que no se puede repetir
    ultimo_ingreso datetime, 
    -- cuando la tabla fue creada
    date_create datetime default current_timestamp, -- cuando el dato sea creado establecer fecha automaticamente
    date_update datetime default current_timestamp on update current_timestamp -- actualizar
);

create table informacion(
	id int auto_increment primary key, 
    id_estudiante int unique, -- Para que el estudiante solo salga una vez inique
    nombre varchar(100) not null, 
    apellido varchar(100) not null, 
    pais varchar(100), 
    ciudad varchar(100), 
    fecha_nacimiento date,
    date_create datetime default current_timestamp, -- cuando el dato sea creado establecer fecha automaticamente
    date_update datetime default current_timestamp on update current_timestamp, -- actualizar
    foreign key(id_estudiante) references estudiantes(id) -- apuntar a un campo unico
);
create table contacto(
	id int auto_increment primary key, 
    id_estudiante int unique, 
    numero_telefono varchar(20) not null, 
    correo varchar(100) unique not null,
    date_create datetime default current_timestamp, -- cuando el dato sea creado establecer fecha automaticamente
    date_update datetime default current_timestamp on update current_timestamp, -- actualizar
    foreign key(id_estudiante) references estudiantes(id) -- apuntar a un campo unico
);


insert into estudiantes(tipo_documento, documento, ultimo_ingreso)
values('tarjeta', '10024', now());

insert into informacion(id_estudiante, nombre, apellido, pais, ciudad, fecha_nacimiento)
value(2, 'Luis', 'Parra', 'Colombia', 'Bogotá', '1998-06-23');

insert into contacto(id_estudiante, numero_telefono, correo)
value(2,'3154567890', 'luis@gmail.com');

select * from estudiantes;

update estudiantes set tipo_documento = "tarjeta" where documento = "1002";

-- Consultas avanzadas
-- select *
select  e.id, e.tipo_documento, e.documento, e.ultimo_ingreso, 
		i.nombre, i.apellido, i.pais, i.ciudad, i.fecha_nacimiento,
        c.correo, c.numero_telefono
from estudiantes e -- from llama la table princial
inner join informacion i -- unir dos tablas por llave foranea
on e.id = i.id_estudiante

inner join contacto c on e.id = c.id_estudiante;

