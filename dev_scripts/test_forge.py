# python imort
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# local import
from utils.downloader import get_forge_versions, download_forge_server

def main():
    print("Versiones Forge disponibles:")
    versions = get_forge_versions()
    for i, v in enumerate(versions):
        print(f"{i + 1}. {v}")
    
    choice = int(input("Selecciona una versión Forge para descargar: "))
    version = versions[choice - 1]
    dest = f"servers/forge/{version}"
    download_forge_server(version, dest)

if __name__ == "__main__":
    main()
