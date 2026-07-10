# 🔐 Enigma Simulator
## Current Version 1.1.0
Una implementación en Python inspirada en la máquina **Enigma**, utilizada durante la Segunda Guerra Mundial para el cifrado de comunicaciones militares.

Este proyecto busca recrear el funcionamiento de los rotores y el mecanismo de sustitución dinámica característicos de Enigma, además de servir como una plataforma para experimentar con nuevas ideas y mejoras utilizando tecnologías modernas.

---

## ✨ Características actuales

* Rotación automática de los rotores durante el cifrado.
* Soporte para cifrado y descifrado de mensajes.
* Reinicio de la configuración inicial de los rotores para reproducir resultados.
* Interfaz de línea de comandos (CLI).

---
## ✨ Cambios de la última versión

* Se cambio la configuracion manual de los rotores a una configuracion automatica mediante una contraseña de cifrado inicial
* Se extendio un lenguaje de 27 caracteres aceptados a todo unicode
* Se implementó una arquitectura orientada a objetos para representar la maquina y sus rotores
* Se creo un mecanismo de cifrado basado ens semillas creadas a partir de hashear la contraseña y convertirla a un entero
* Se incorporó la generación de posiciones iniciales de los rotores a partir de las semillas generadas
* Se mejoró la modularidad del proyecto mediante la creación del módulo config

---

## 🚀 Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/tu_usuario/enigma.git
```

### 2. Entrar al directorio del proyecto

```bash
cd enigma
```

### 3. Ejecutar el programa

```bash
python main.py
```

---

## 📖 Uso

Al ejecutar el programa aparecerá un menú interactivo:

```text
SIMULADOR DE LA MAQUINA ENIGMA

Ingrese 1 para cifrar un mensaje.
Ingrese 2 para descifrar un mensaje.
```

### Ejemplo de cifrado

```text
Ingrese 1 para cifrar un mensaje: 1
Ingrese el mensaje a cifrar: HOLA

Mensaje original: HOLA
Mensaje cifrado: QKZV
```

### Ejemplo de descifrado

```text
Ingrese 1 para cifrar un mensaje, 2 para descifrar un mensaje: 2
Ingrese el mensaje a descifrar: QKZV

Mensaje original: QKZV
Mensaje descifrado: HOLA
```

---

## 📁 Estructura del proyecto

```text
Enigma/
│
├── main.py                 # Punto de entrada del programa
│
├── elements/
│   ├── __init__.py
│   ├── rotor.py            # Implementación de los rotores
│   └── machine.py          # Coordinación del cifrado y descifrado
│
└── README.md
```

---

## ⚙️ Funcionamiento

Cada rotor contiene:

* Un abecedario de referencia.
* Un cableado interno que define las sustituciones.
* Una posición actual.
* Una posición inicial para reiniciar la configuración.

Durante el cifrado:

1. El primer rotor avanza.
2. Si completa una vuelta, avanza el siguiente rotor.
3. El carácter atraviesa secuencialmente todos los rotores.
4. Se obtiene el carácter cifrado.

---

## 🛠️ Tecnologías utilizadas

* Python 3
* Programación Orientada a Objetos (POO)

---

## 📚 Objetivos del proyecto

* Implementar un reflector similar al de la Enigma histórica.
* Añadir soporte para configuraciones personalizadas de rotores.
* Implementar un panel de conexiones (*plugboard*).
* Investigar soporte para caracteres Unicode.
* Experimentar con mejoras modernas inspiradas en el diseño original.

---

## ⚠️ Aviso

Este proyecto tiene fines educativos y de investigación.

No debe considerarse un sistema criptográfico seguro para proteger información sensible o comunicaciones reales.

---
