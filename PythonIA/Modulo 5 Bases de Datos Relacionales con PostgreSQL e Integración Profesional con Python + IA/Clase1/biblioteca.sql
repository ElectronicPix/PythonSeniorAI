-- Sentencia para crear la tabla 'autor' si no existe.
CREATE TABLE IF NOT EXISTS autor( -- IF NOT EXISTS: Evita un error si la tabla ya existe, verificando antes de la creación.
    -- 'id' es la clave primaria de la tabla, de tipo bigserial, lo que significa que es un entero de 8 bytes que se autoincrementa.
    id bigserial primary key,  -- bigserial: Tipo de dato entero de 8 bytes, se autoincrementa para generar un identificador único.
    -- 'nombre' almacena el nombre del autor, no puede ser nulo.
    nombre varchar(150) not null,
    -- 'nacionalidad' almacena la nacionalidad del autor.
    nacionalidad varchar(150),
    -- 'uq_autor_nombre_nacionalidad' es una restricción de unicidad que asegura que no haya dos autores con el mismo nombre y nacionalidad.
    constraint uq_autor_nombre_nacionalidad unique(nombre, nacionalidad) -- constraint: Define una regla para los datos de la tabla.
);

-- Sentencia para crear la extensión 'uuid-ossp' si no existe.
-- Esta extensión proporciona funciones para generar identificadores únicos universales (UUIDs).
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- Sentencia para crear la tabla 'usuarios' si no existe.
create table if not exists usuarios(
    -- 'id' es la clave primaria de la tabla, de tipo UUID, que se genera automáticamente con la función uuid_generate_v4().
    id UUID primary key default uuid_generate_v4(),
    -- 'nombre' almacena el nombre del usuario, no puede ser nulo.
    nombre varchar(150) not null,
    -- 'email' almacena el correo electrónico del usuario, no puede ser nulo.
    email varchar(255) not null,
    -- 'uq_usuario_email' es una restricción de unicidad que asegura que no haya dos usuarios con el mismo correo electrónico.
    constraint uq_usuario_email UNIQUE(email),
    -- 'ck_usuario_email_formato' es una restricción de verificación que asegura que el correo electrónico contenga el carácter '@'.
    constraint ck_usuario_email_formato check (position('@' in email) > 1)
);