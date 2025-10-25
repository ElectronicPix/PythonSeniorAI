CREATE TABLE `Estudiantes`(
    `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `tipodocumento` BIGINT NOT NULL,
    `docuemento` BIGINT NOT NULL,
    `ultimo_ingreso` BIGINT NOT NULL,
    `fecha_creacion` BIGINT NOT NULL,
    `fecha_actu` BIGINT NOT NULL
);
CREATE TABLE `contacto`(
    `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `id_estudiantes` BIGINT NOT NULL,
    `numero_telefono` BIGINT NOT NULL,
    `correo` BIGINT NOT NULL
);
CREATE TABLE `informacion`(
    `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `id_estudiantes` BIGINT NOT NULL,
    `nombre` BIGINT NOT NULL,
    `apellido` BIGINT NOT NULL,
    `pais` BIGINT NOT NULL,
    `ciudad` BIGINT NOT NULL,
    `fecha_nacimiento` BIGINT NOT NULL
);
ALTER TABLE
    `contacto` ADD CONSTRAINT `contacto_id_estudiantes_foreign` FOREIGN KEY(`id_estudiantes`) REFERENCES `Estudiantes`(`id`);
ALTER TABLE
    `informacion` ADD CONSTRAINT `informacion_id_estudiantes_foreign` FOREIGN KEY(`id_estudiantes`) REFERENCES `Estudiantes`(`id`);