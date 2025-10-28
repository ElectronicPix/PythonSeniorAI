
create table if not exists autor(
	id UUID primary key default uuid_generate_v4(), -- bigserial
	nombre varchar(150) not null, 
	nacionalidad varchar(150),
	constraint uq_autor_nombre_nacionalidad unique (nombre, nacionalidad)
);

insert into autor (nombre, nacionalidad) values
	('Gabriel gaarcía Marquez', 'Colombia'),
	('Jorge Luis Borges', 'Argentina'),
	('Isabel Allende', 'Chile');

select * from autor;

-- Activar la extención para generar UUIDs
create extension if not exists "uuid-ossp";

create table if not exists usuario(
	id UUID primary key default uuid_generate_v4(),
	nombre varchar(150) no null, 
	email varchar(255) not null,
	constraint ck_usuario_email_formato che
);

insert into usuario (nombre, email) values 
	('Daniela Aldana', 'd.aldana@gmail.com');

select * from usuario;

create table if not exists libro(
	id UUID primary key default uuid_generate_v4(),
	titulo varchar(200) not null, 
	anio int check (anio >= 0 and anio <= extract (year from current_date)::int),
	id_autor UUID not null, 
	constraint fk_libro_autor foreign key (id_autor) references autor(id)
);
