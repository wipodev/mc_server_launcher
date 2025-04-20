# python imort
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# local import
from utils.downloader import get_vanilla_versions, download_vanilla_server

def main():
    print("Obteniendo lista de versiones Vanilla disponibles...")
    versions = get_vanilla_versions()

    for idx, v in enumerate(versions):
        print(f"{idx + 1}. {v['id']}")

    choice = input("\nEscribe el número de la versión que deseas descargar: ")
    
    try:
        index = int(choice) - 1
        if index < 0 or index >= len(versions):
            raise ValueError("Número fuera de rango.")
    except ValueError as e:
        print(f"Entrada inválida: {e}")
        return

    version = versions[index]
    dest_dir = os.path.join("servers", "vanilla", version["id"])

    jar_path = download_vanilla_server(version["id"], version["url"], dest_dir)
    print(f"\n¡Servidor Vanilla descargado correctamente en: {jar_path}")

if __name__ == "__main__":
    main()
