
# 📝 Informe del Proyecto: MC Server Launcher

## 📌 Descripción del Proyecto
**MC Server Launcher** es una aplicación de escritorio desarrollada en Python con Tkinter que permite al usuario descargar rápidamente servidores de Minecraft, ya sea en su versión **Vanilla** (oficial) o **Forge** (modificada). El objetivo principal es proporcionar una herramienta sencilla y visual para usuarios que no están familiarizados con los procesos manuales de descarga y configuración de servidores.

Esta herramienta busca reducir el proceso de descarga a solo unos clics, ofreciendo una interfaz intuitiva con selección de tipo de servidor, versión y posibilidad de búsqueda rápida.

---

## ✅ Estado Actual

### 1. Estructura de la Aplicación
- Aplicación desarrollada con Tkinter.
- Separación entre lógica de UI y lógica de descarga (`downloader.py`).
- Interfaz gráfica funcional: radio buttons para seleccionar tipo de servidor, combobox para elegir versión y botón para descargar.

### 2. Funciones Implementadas
- Obtención de versiones Vanilla desde el manifiesto oficial de Mojang.
- Obtención de versiones Forge desde el JSON de promos oficial.
- Ordenamiento correcto de versiones por fecha de lanzamiento.
- Combobox con versiones actualizadas según el tipo seleccionado.
- Campo de búsqueda para filtrar versiones dentro del combobox.
- Manejo de errores (descarga fallida, errores de conexión, etc.).
- Descarga automática del archivo `.jar` del servidor seleccionado a una carpeta específica (`servers/vanilla` o `servers/forge`).

### 3. Interfaz de Usuario
- Radio buttons para seleccionar entre “Vanilla” y “Forge”.
- Combobox para elegir la versión.
- Input centrado y más corto para filtrar/buscar versiones.
- Etiquetas de estado que informan el progreso (cargando, descargando, error, completado).

---

## 🔧 Funcionalidades Pendientes / Mejora

| Área             | Tarea                                                                 |
|------------------|------------------------------------------------------------------------|
| Descargas        | Verificar integridad del `.jar` descargado (checksum opcional).        |
| UI               | Mejorar diseño visual con temas o soporte para temas oscuros.          |
| Compatibilidad   | Añadir soporte para Fabric y/o Quilt.                                  |
| Configuración    | Posibilidad de configurar y generar el archivo `server.properties`.    |
| Ejecución directa| Agregar botón para ejecutar el servidor descargado.                   |
| Historial/Logs   | Registrar historial de descargas o errores.                            |
| Empaquetado      | Convertir la app a ejecutable (por ejemplo con PyInstaller).           |
| Internacionalización | Soporte multiidioma (español, inglés).                             |
| Documentación    | Crear ayuda/documentación accesible desde la app.                      |

---

## 🎯 Objetivo Final

El objetivo es construir una herramienta **multiplataforma, estable y fácil de usar** que facilite a jugadores y administradores de servidores Minecraft descargar, preparar y gestionar servidores en pocos pasos, eliminando la necesidad de procesos manuales, líneas de comandos o búsqueda de enlaces externos.
