
## **Nivel 1: Sintaxis y Control de Flujo**

### Qué repasar:
- Tipos de datos (`int`, `float`, `char`, etc.)
- Operadores (aritméticos, lógicos, relacionales)
- Estructuras de control: `if/else`, `switch`, `for`, `while`, `do-while`
- Funciones básicas y paso de parámetros por valor
- Arrays unidimensionales básicos

### Recursos:
- **Libro**: *"The C Programming Language"* (Kernighan & Ritchie) - Capítulos 1-4
- **Online**: [Learn-C.org](https://www.learn-c.org/) - Secciones básicas
- **Documentación**: `man printf`, `man scanf` en tu terminal
- **Práctica**: Resuelve problemas en papel antes de programar

---

## **Nivel 2: Arrays y Strings**

### Qué repasar:
- Arrays multidimensionales
- Strings como arrays de `char` terminados en `\0`
- Diferencia entre `char str[]` y `char *str`
- Recorrido de arrays con índices
- Algoritmos de ordenamiento simples

### Recursos:
- **Libro**: K&R - Capítulo 5 (Punteros y Arrays)
- **Referencia**: `man string` para entender las funciones estándar (pero impleméntalas tú)
- **Visualización**: [VisuAlgo](https://visualgo.net/en/sorting) para algoritmos de ordenamiento
- **Ejercicios**: [HackerRank - C Arrays](https://www.hackerrank.com/domains/c)

---

## **Nivel 3: Punteros**

### Qué repasar:
- Concepto de dirección de memoria
- Operadores `&` (dirección) y `*` (desreferencia)
- Aritmética de punteros
- Relación entre punteros y arrays
- Punteros a punteros

### Recursos:
- **Libro**: K&R - Capítulo 5 completo
- **Artículo clave**: [Pointer Basics](http://cslibrary.stanford.edu/106/) (Stanford)
- **Visualizador**: [PythonTutor para C](http://pythontutor.com/c.html) - visualiza memoria
- **Práctica**: Dibuja en papel las direcciones de memoria

---

## **Nivel 4: Memoria Dinámica**

### Qué repasar:
- `malloc()`, `calloc()`, `realloc()`, `free()`
- Diferencia entre stack y heap
- Memory leaks y double free
- Valgrind básico

### Recursos:
- **Libro**: K&R - Capítulo 8 (UNIX System Interface)
- **Manual**: `man malloc`, `man free`
- **Herramienta**: [Valgrind Quick Start](https://valgrind.org/docs/manual/quick-start.html)
- **Tutorial**: [Beej's Guide to C](https://beej.us/guide/bgc/) - Sección de memoria dinámica

---

## **Nivel 5: Estructuras de Datos Clásicas**

### Qué repasar:
- `struct` y `typedef`
- Punteros a estructuras (`->` operator)
- Recursión avanzada
- Complejidad algorítmica (Big O)

### Recursos:
- **Libro**: *"Data Structures Using C"* (Reema Thareja)
- **Curso online**: [CS50 - Week 5](https://cs50.harvard.edu/x/) (Data Structures)
- **Visualización**: [VisuAlgo](https://visualgo.net/) - Árboles, heaps, etc.
- **Referencia**: [GeeksforGeeks C Data Structures](https://www.geeksforgeeks.org/data-structures/) (solo teoría, no copies código)

---

## **Nivel 6: Manejo de Archivos**

### Qué repasar:
- `fopen()`, `fclose()`, `fread()`, `fwrite()`
- Modos de apertura (`r`, `w`, `a`, `rb`, `wb`)
- `fgets()`, `fputs()`, `fscanf()`, `fprintf()`
- Manejo de errores con `errno` y `perror()`

### Recursos:
- **Libro**: K&R - Capítulo 7 (Input/Output)
- **Manual**: `man fopen`, `man fread`, `man ferror`
- **Tutorial**: [Programiz - C File I/O](https://www.programiz.com/c-programming/c-file-input-output)

---

## **Nivel 7: Bits y Bajo Nivel**

### Qué repasar:
- Operadores bitwise: `&`, `|`, `^`, `~`, `<<`, `>>`
- Representación binaria de números
- Máscaras de bits
- Complemento a 2

### Recursos:
- **Libro**: K&R - Apéndice A (Operadores)
- **Herramienta**: Calculadora binaria (Windows calc en modo programador)
- **Tutoriales**: [Bitwise Operators in C](https://www.geeksforgeeks.org/bitwise-operators-in-c-cpp/) (solo teoría)
- **Práctica**: Resuelve en papel primero

---

## **Nivel 8: Proyectos Integradores**

### Qué repasar:
- Llamadas al sistema: `fork()`, `exec()`, `pipe()` (para el shell)
- Sockets básicos (para servidor TCP)
- Gestión de memoria a bajo nivel (para allocator)

### Recursos:
- **Libro**: *"Advanced Programming in the UNIX Environment"* (Stevens) - Capítulos de procesos y sockets
- **Manual**: `man 2 fork`, `man 2 socket`, `man 7 pipe`
- **Tutorial shell**: [Write a Shell in C](https://brennan.io/2015/01/16/write-a-shell-in-c/)
- **Tutorial sockets**: [Beej's Guide to Network Programming](https://beej.us/guide/bgnet/)

---

## **Herramientas Esenciales**

1. **Compilador**: GCC con flags `-Wall -Wextra -Werror -std=c99 -pedantic`
2. **Debugger**: GDB - `man gdb` o [GDB Tutorial](https://www.cs.cmu.edu/~gilpin/tutorial/)
3. **Valgrind**: Para detectar leaks - `valgrind --leak-check=full ./programa`
4. **Make**: Para automatizar compilación - [GNU Make Manual](https://www.gnu.org/software/make/manual/)

---

## **Consejos de Estudio**

- **Lee el manual**: `man` es tu mejor amigo
- **Dibuja memoria**: Papel y lápiz para punteros y estructuras
- **Compila a menudo**: No escribas 100 líneas sin compilar
- **Testing manual**: Crea casos de prueba en un archivo `.txt`
- **Repositories**: Sube tu código a GitHub para ver tu progreso

