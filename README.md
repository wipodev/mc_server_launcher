# MC Server Launcher

MC Server Launcher is a desktop application developed in Python using Tkinter that allows users to quickly download Minecraft servers, either in their Vanilla (official) or Forge (modded) versions. The main goal is to provide a simple and visual tool for users unfamiliar with the manual download and setup process of servers.

This tool aims to reduce the download process to just a few clicks, offering an intuitive interface with server type selection, version selection, and quick search capability.

## Structure

```
MC-Server-Launcher/
│
├── app/                          # Contendrá la lógica de la aplicación
│   ├── __init__.py               # Indica que la carpeta es un paquete
│   ├── downloader.py             # Código para manejar las descargas de servidores Vanilla/Forge
│   └── settings.py               # Configuraciones de la app (e.g., idioma seleccionado, preferencias)
│
├── docs/                         # Archivos de documentacion
│   ├── PROJECT_OVERVIEW_EN.json
│   └── PROJECT_OVERVIEW_ES.json
│
├── i18n/                         # Lógica de internacionalización
│   ├── locales/                  # Archivos de traducciones
│   │   ├── en.json
│   │   └── es.json
│   ├── __init__.py
│   └── i18n.py                   # Funciones para cargar y manejar las traducciones
│
├── tests/                        # Pruebas unitarias y de integración
│   ├── clear.py
│   ├── test_forge.py
│   └── test_vanilla.py
│
├── ui/                           # Contendrá la lógica de la interfaz
│   ├── __init__.py
│   └── launcher_ui.py            # Código para la interfaz de usuario con Tkinter
│
├── resources/                    # Archivos estáticos si es necesario (imágenes, iconos, etc.)
│   └── icon.png                  # Ejemplo de archivo estático (puede ser un ícono de la app)
│
├── .gitignore                    # Archivo para ignorar archivos en Git
├── LICENSE                       # Licencia del proyecto
├── main.py                       # Archivo principal que ejecuta la app
├── README.md                     # Documentación del proyecto
└── requirements.txt              # Dependencias del proyecto
```
