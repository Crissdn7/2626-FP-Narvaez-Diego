# Sistema de Gestión de Restaurante
**Estudiante:** Diego Cristofer Narváez Alvarado

# Descripción del proyecto
Este es un sistema sencillo que hice para practicar la Programación Orientada a Objetos en Python. La idea es poder gestionar un restaurante de forma básica, permitiendo registrar productos para el menú y también tener una lista de clientes. El objetivo principal de este trabajo fue aprender a organizar el código en módulos y carpetas para que no todo esté en un solo archivo, lo cual hace que el proyecto sea mucho más ordenado.

# Explicación de la estructura
Para cumplir con lo solicitado, dividí mi proyecto de la siguiente manera:

**Carpeta modelos/:** Aquí guardé las clases producto.py y cliente.py, que sirven para definir cómo son nuestros objetos y qué datos deben tener.

**Carpeta servicios/:** Aquí puse el archivo restaurante.py, que se encarga de la lógica de negocio, como guardar los datos y mostrar las listas en pantalla.

**Archivo main.py:** Es el archivo principal desde donde arranca todo; aquí importo las clases de las otras carpetas y ejecuto el programa para demostrar que funciona.

# Reflexión sobre la modularidad y separación de responsabilidades
Después de trabajar con este ejercicio, me di cuenta de que organizar el código así es muy importante por las siguientes razones:

**Es mucho más fácil corregir errores:** Como cada parte del código tiene su lugar, si algo sale mal, sé exactamente dónde ir a revisar sin tener que leer todo el programa.

**El código es más limpio y profesional:** Al separar las responsabilidades, cada archivo se enfoca en hacer una sola cosa, lo que hace que todo sea más fácil de entender.

**Es más fácil de mejorar:** Si en el futuro quiero agregar más opciones al restaurante, es mucho más sencillo hacerlo porque cada módulo es independiente y no se rompe el resto del sistema.**