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
* Soporte para caracteres unicode
* Cifrado basado en semillas creadas por una contraseña de cifrado inicial

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
git clone https://github.com/CatorceDev/MaquinaEnigma
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
--------------------------------------------------------------

SIMULADOR DE LA MAQUINA ENIGMA

ETAPA DE CONFIGURACION DE LA MÁQUINA
Ingresa tu contraseña de cifrado: ContraseñaSuperSecreta123
Nombra tus rotores :)

Nombre de tu rotor 1: Contraseña_rotor_1
Nombre de tu rotor 2: Contraseña_rotor_2
Nombre de tu rotor 3: Contraseña_rotor_3

Ingrese 1 para cifrar un mensaje, 2 para descifrar un mensaje o enter para configurar de nuevo los rotores: 1
Ingrese el mensaje a cifrar: Mensaje a cifrar con Enigma
Mensaje original:  Mensaje a cifrar con Enigma
Mensaje cifrado:  󢙜򐬯󠣘𞀘ᜍ󟷅񼘄󠨆𥥼󃚲𴁘󶋺􌏢󤻬󟷅񣊣񀉡󶋺񣊣񣊣񊰜񿀹􇳗񫷎󤻬񭈟󒦽
```

### Ejemplo de descifrado

```text
--------------------------------------------------------------

SIMULADOR DE LA MAQUINA ENIGMA

ETAPA DE CONFIGURACION DE LA MÁQUINA
Ingresa tu contraseña de cifrado: ContraseñaSuperSecreta123
Nombra tus rotores :)

Nombre de tu rotor 1: Contraseña_rotor_1
Nombre de tu rotor 2: Contraseña_rotor_2
Nombre de tu rotor 3: Contraseña_rotor_3

Ingrese 1 para cifrar un mensaje, 2 para descifrar un mensaje o enter para configurar de nuevo los rotores: 2
Ingrese el mensaje a descifrar: 󢙜򐬯󠣘𞀘ᜍ󟷅񼘄󠨆𥥼󃚲𴁘󶋺􌏢󤻬󟷅񣊣񀉡󶋺񣊣񣊣񊰜񿀹􇳗񫷎󤻬񭈟󒦽
Mensaje original:  󢙜򐬯󠣘𞀘ᜍ󟷅񼘄󠨆𥥼󃚲𴁘󶋺􌏢󤻬󟷅񣊣񀉡󶋺񣊣񣊣񊰜񿀹􇳗񫷎󤻬񭈟󒦽
Mensaje descifrado:  Mensaje a cifrar con Enigma
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
|   ├── cableado.py         # Funciones para crear el cableado de los rotores
|   ├── config.py           # Clase para crear las semillas, posiciones inciales y el cablado de los rotores
|   ├── exceptions.py       # Clase en proceso para manejar todas las excepciones
│   ├── machine.py          # Clase para crear la maquina enigma
|   ├── reflector.py        # Clase en proceso para separar las tareas de la maquina enigma y el cifrado/descifrado
│   └── rotor.py            # Clase para la implementación de los rotores
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
* Implementar un panel de conexiones (*plugboard*).
* Experimentar con mejoras modernas inspiradas en el diseño original.
* Integrar la herramienta con una API de mensajería.
* Desarrollar una interfaz gráfica.
* Sustituir el reinicio de los rotores por un sistema de avance continuo.
* Investigar mecanismos de sincronización entre emisor y receptor sin transmitir el estado actual de la máquina-
* Optimizar el algoritmo de cifrado/descifrado.
* Implementar un sistema de intercambio seguro de semillas maestras.
* Implementar el cifrado de imagenes, videos y demás archivos multimedia.

---

## ⚠️ Aviso

Este proyecto tiene fines educativos y de investigación.

No debe considerarse un sistema criptográfico seguro para proteger información sensible o comunicaciones reales.

---
