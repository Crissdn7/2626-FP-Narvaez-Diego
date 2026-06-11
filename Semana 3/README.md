# Tarea: Comparación entre Programación Tradicional y POO

**Estudiante:** Diego Cristofer Narváez Alvarado  
**Asignatura:** Programación Orientada a Objetos  

##  De qué trata el proyecto
En este proyecto desarrollé un sistema básico para la gestión y el reporte de datos de mascotas utilizando dos paradigmas de programación distintos en Python para analizar cómo cambia la estructura del código:

1. **Enfoque Tradicional (`programacion_tradicional/`):** Una solución estructurada mediante funciones independientes y variables locales. Este programa interactúa de forma secuencial pidiéndole los datos al usuario por teclado (`input()`) y los agrupa de manera sencilla usando un diccionario.
2. **Enfoque Orientado a Objetos (`programacion_poo/`):** Una solución modular dividida en dos partes. En `mascota.py` creé la clase `Mascota` que funciona como un molde abstracto con sus propios atributos y métodos (`mostrar_informacion` y `hacer_sonido`). En `main.py` se realiza la ejecución principal, importando el molde para crear y controlar las mascotas como objetos reales.

##  Reflexión:
Después de construir y probar los dos programas, estas son las diferencias clave que identifiqué entre la Programación Tradicional y la Programación Orientada a Objetos:

* **Organización del código y acoplamiento:** En el código tradicional, los datos (el diccionario) van completamente separados de las funciones que los imprimen. Si en el futuro cambio la estructura de esos datos, tengo que reescribir las funciones porque se romperían. En cambio, en la POO los datos (atributos) y los comportamientos (métodos) viven juntos dentro del mismo objeto, lo que mantiene todo mucho más ordenado y protegido.
* **Mantenimiento y modularidad:** Al separar el plano de construcción (`mascota.py`) de la ejecución (`main.py`), el proyecto es más fácil de escalar. Si quisiera agregar nuevas características a las mascotas (como el peso o el historial de vacunas), solo modifico el archivo de la clase y el flujo de ejecución principal en `main.py` sigue funcionando sin desordenar nada.
* **Reutilización y limpieza:** En el enfoque tradicional, para registrar múltiples mascotas de forma consecutiva tendría que duplicar bloques de código o estructurar bucles complejos. Con la POO, crear nuevas instancias de mascotas con datos diferentes requiere apenas una sola línea de código llamando a la clase, lo que ahorra tiempo y evita repetir código innecesario.