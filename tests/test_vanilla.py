# python imort
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# local import
from app.downloader import get_vanilla_versions, download_vanilla_server

def main():
    print("Obteniendo lista de versiones Vanilla disponibles...")
    versions = get_vanilla_versions()
    for i, v in enumerate(versions):
        print(f"{i + 1}. {v['id']}")

    choice = int(input("\nEscribe el número de la versión que deseas descargar: "))
    
    try:
        index = choice - 1
        if index < 0 or index >= len(versions):
            raise ValueError("Número fuera de rango.")
    except ValueError as e:
        print(f"Entrada inválida: {e}")
        return

    version = versions[index]
    dest_dir = os.path.join("dev_scripts", "servers", "vanilla", version["id"])

    print(f"version: {version['id']} dest_dir: {dest_dir}")
    
    download_vanilla_server(version["id"], version["url"], dest_dir)

if __name__ == "__main__":
    main()
