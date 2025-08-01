# Introducción a Diagramas de Flujo y Ciclos

## ¿Qué es un diagrama de flujo?

Un diagrama de flujo es una representación gráfica de un proceso o algoritmo. Utiliza **símbolos estandarizados** para mostrar cada paso del proceso y las decisiones que se toman.

### Principales elementos de un diagrama de flujo

| **Símbolo**            | **Nombre técnico**           | **Función**                                                  |
|------------------------|------------------------------|--------------------------------------------------------------|
| 🔷 Rombos              | **Decisión**                 | Representa una pregunta o condición con dos o más salidas.   |
| ⬛ Rectángulos         | **Proceso o Acción**         | Representa una instrucción o paso del proceso.               |
| 🟠 Elipses             | **Inicio / Fin (Terminal)**  | Indica el punto de inicio o fin del diagrama.                |
| 🔲 Paralelepípedo      | **Entrada/Salida**           | Representa una operación de entrada o salida de datos.       |
| 🔀 Flechas             | **Líneas de flujo**          | Indican la dirección del proceso de un paso a otro.          |

---

## ¿Por qué son necesarios los ciclos en los procesos?

Los **ciclos** son necesarios porque permiten repetir una acción o conjunto de acciones **hasta que se cumpla una condición específica**. Esto es útil para:

- Repetir intentos (como validar una contraseña).
- Acumular datos hasta lograr un objetivo.
- Procesar múltiples elementos (como registrar estudiantes).
- Optimizar código evitando repeticiones manuales.

Los ciclos hacen que los programas y procesos sean **más eficientes, flexibles y reutilizables**.

---

# Ejercicios con Ciclos – Enunciados

## Ejercicio 1: Suma acumulada hasta alcanzar un límite

Una persona quiere guardar dinero para comprar una laptop que cuesta **$1000**. Cada vez que tiene dinero disponible, lo deposita en su cuenta de ahorros.

El sistema debe:

1. Pedir al usuario cuánto dinero va a depositar.
2. Sumar ese depósito al total acumulado.
3. Mostrar cuánto lleva ahorrado.
4. Repetir el proceso hasta que el total ahorrado sea **mayor o igual a $1000**.
5. Al alcanzar o superar los $1000, mostrar un mensaje de felicitación y finalizar.


## Ejercicio 2: Sistema de inscripción a un curso gratuito

Un centro educativo está ofreciendo un curso gratuito de programación, pero solo pueden inscribirse estudiantes que:

1. Sean mayores de 15 años.
2. Tengan acceso a internet.
3. No estén ya inscritos (se valida con una lista de nombres ya registrados).

El sistema debe:

1. Preguntar el nombre del estudiante.
2. Preguntar su edad.
3. Preguntar si tiene acceso a internet (sí o no).
4. Verificar si ya está inscrito.
5. Si cumple todas las condiciones, agregarlo a la lista de inscritos y mostrar un mensaje de confirmación.
6. Si no cumple alguna, mostrarle el motivo por el cual no fue aceptado.

El proceso se repite hasta que el usuario (administrador) diga que no desea registrar a más estudiantes.


## Ejercicio 3: Verificación de contraseña segura

Un sistema de registro en una plataforma educativa requiere que cada usuario elija una contraseña segura.  
La contraseña debe cumplir las siguientes condiciones:

1. Tener al menos 8 caracteres.
2. Incluir al menos una letra mayúscula.
3. Incluir al menos un número.

El sistema debe:

1. Pedir al usuario que escriba una contraseña.
2. Verificar si cumple con los requisitos.
3. Si no cumple, mostrar los errores específicos y volver a pedir una nueva contraseña.
4. Si cumple, registrar la contraseña y finalizar el proceso.

---

## Ejercicios prácticos adicionales

### Ejercicio 4: Encuentra el número secreto

El sistema tiene un número secreto guardado. El usuario debe adivinarlo.

1. Pedir al usuario que adivine el número.
2. Si el número es incorrecto, indicar si el número secreto es mayor o menor.
3. Repetir hasta que adivine el número correctamente.
4. Al acertar, mostrar un mensaje de felicitación.

### Ejercicio 5: Registro de temperaturas

Un sistema debe registrar las temperaturas diarias hasta que el usuario escriba la palabra "fin".

1. Pedir una temperatura.
2. Guardar la temperatura en una lista.
3. Repetir mientras el valor ingresado no sea "fin".
4. Al finalizar, mostrar cuántas temperaturas se registraron y su promedio.

### Ejercicio 6: Repetición de mensaje motivacional

Un profesor quiere imprimir un mensaje motivador 10 veces en pantalla.

1. Repetir 10 veces el mensaje: “¡Tú puedes lograrlo!”.
2. Mostrar un número al lado de cada repetición.

### Ejercicio 7: Suma de números positivos

Un usuario debe ingresar números. El sistema suma todos los positivos y se detiene si se escribe un número negativo.

1. Pedir un número.
2. Si es positivo, sumarlo al total.
3. Si es negativo, terminar el proceso y mostrar el total acumulado.

### Ejercicio 8: Lista de compras

El sistema permite ingresar productos a una lista de compras.

1. Preguntar al usuario el nombre de un producto.
2. Agregarlo a la lista.
3. Preguntar: “¿Deseas ingresar otro producto?”
4. Si responde “sí”, repetir.
5. Si responde “no”, mostrar la lista completa.

---
