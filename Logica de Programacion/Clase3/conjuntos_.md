# Fundamentos de conjuntos y su aplicación en SQL

## 1. ¿Qué es un conjunto?

Un conjunto es una colección bien definida de elementos distintos. En matemáticas, los conjuntos se representan usando llaves `{}` y sus elementos pueden ser cualquier tipo de objeto. Por ejemplo, el conjunto de estudiantes matriculados se puede representar como:

```
A = {Ana, Luis, Marta}
```

Y el conjunto de estudiantes que entregaron la tarea se puede representar como:

```
B = {Luis, Marta, Pedro}
```

## 2. Conceptos clave de conjuntos

| Concepto              | Símbolo | Explicación                                                                 |
|-----------------------|---------|------------------------------------------------------------------------------|
| **Unión**             | A ∪ B   | Todos los elementos que están en A, en B o en ambos.                        |
| **Intersección**      | A ∩ B   | Solo los elementos que están tanto en A como en B.                          |
| **Diferencia**        | A - B   | Elementos que están en A pero no en B.                                      |
| **Diferencia simétrica** | A △ B   | Elementos que están en A o en B, pero no en ambos.                         |
| **Complemento**       | Aᶜ      | Todos los elementos que no están en A, respecto a un universo definido.    |

## 3. Aplicación práctica con SQL

| Descripción del grupo                                                                  | Relación de conjuntos | SQL correspondiente |
|-----------------------------------------------------------------------------------------|------------------------|---------------------|
| Estudiantes que están matriculados y entregaron la tarea.                              | A ∩ B                 | `INNER JOIN`        |
| Estudiantes que están matriculados, o entregaron la tarea, o ambas cosas.              | A ∪ B                 | `FULL JOIN`         |
| Estudiantes que solo están matriculados o solo entregaron la tarea, pero no ambos.     | A △ B                 | `FULL JOIN` + `WHERE A.key IS NULL OR B.key IS NULL` |
| Todos los estudiantes matriculados, hayan o no entregado la tarea.                     | A                     | `LEFT JOIN`         |
| Estudiantes que están matriculados pero no entregaron la tarea.                        | A - B                 | `LEFT JOIN` + `WHERE B.key IS NULL` |
| Estudiantes que entregaron la tarea, estén o no matriculados.                          | B                     | `RIGHT JOIN`        |
| Estudiantes que entregaron la tarea pero no están matriculados.                        | B - A                 | `RIGHT JOIN` + `WHERE A.key IS NULL` |

## 4. Actividad para practicar

Relaciona cada uno de los siguientes grupos con un concepto de conjuntos:


### Ejemplo 1: Clientes y promociones
- **Conjunto A**: Clientes que realizaron una compra.
- **Conjunto B**: Clientes que se inscribieron al boletín promocional.

1. Clientes que realizaron una compra y se inscribieron al boletín promocional.  
2. Clientes que realizaron una compra, o se inscribieron al boletín, o ambas cosas.  
3. Clientes que solo compraron o solo se inscribieron al boletín, pero no ambos.  
4. Todos los clientes que realizaron una compra, se hayan o no inscrito al boletín.  
5. Clientes que realizaron una compra pero no se inscribieron al boletín.  
6. Clientes que se inscribieron al boletín, hayan comprado o no.  
7. Clientes que se inscribieron al boletín pero no realizaron ninguna compra.

### Ejemplo 2: Usuarios y plataforma de streaming
- **Conjunto A**: Usuarios que tienen suscripción activa a la plataforma.
- **Conjunto B**: Usuarios que han calificado o dejado reseñas de contenido.

1. Usuarios suscritos que calificaron contenido.  
2. Usuarios suscritos o que calificaron contenido (o ambos).  
3. Usuarios que solo están suscritos o solo calificaron, pero no ambos.  
4. Todos los usuarios con suscripción activa (califiquen o no).  
5. Usuarios con suscripción activa que no han calificado contenido.  
6. Usuarios que calificaron contenido (tengan o no suscripción).  
7. Usuarios que calificaron sin tener suscripción activa.


## Ejemplo 3: Empleados y capacitaciones
**Conjunto A**: Empleados que asistieron al curso de seguridad laboral.  
**Conjunto B**: Empleados que aprobaron el examen de seguridad.

- Empleados que asistieron al curso y aprobaron el examen.
- Empleados que asistieron al curso o aprobaron el examen, o ambas cosas.
- Empleados que solo asistieron al curso o solo aprobaron el examen, pero no ambos.
- Todos los empleados que asistieron al curso (hayan aprobado o no).
- Empleados que asistieron al curso pero no aprobaron el examen.
- Empleados que aprobaron el examen (hayan asistido al curso o no).
- Empleados que aprobaron sin haber asistido al curso.

---

## Ejemplo 4: Productos y devoluciones
**Conjunto A**: Productos vendidos en el último mes.  
**Conjunto B**: Productos que fueron devueltos por fallas.

- Productos que fueron vendidos y luego devueltos.
- Productos que fueron vendidos, o devueltos, o ambas cosas.
- Productos que solo fueron vendidos o solo fueron devueltos, pero no ambos.
- Todos los productos vendidos (independientemente de si fueron devueltos o no).
- Productos vendidos que no fueron devueltos.
- Productos devueltos (hayan sido vendidos el último mes o no).
- Productos devueltos que no fueron vendidos este último mes.

## Ejemplo 5: Inventario, ventas y productos en promoción

**Conjunto A**: Productos que están actualmente en inventario.  
**Conjunto B**: Productos que han sido vendidos este mes.  
**Conjunto C**: Productos que están en promoción activa.

- Productos que están en inventario, se han vendido este mes y están en promoción.
- Productos que están en al menos uno de los tres conjuntos (inventario, ventas o promoción).
- Productos que están en inventario y en promoción, pero no se han vendido.
- Productos vendidos este mes que no están ni en inventario ni en promoción.
- Productos que están en promoción pero no se han vendido ni están en inventario.
- Productos que están tanto en inventario como en ventas, pero no en promoción.
- Productos que no están en ninguno de los tres conjuntos (es decir, productos antiguos, no disponibles ni en promoción).