# python import
import shutil
import os

BASE_PATH = os.path.join("dev_scripts", "servers")

def cleanup():
    if not os.path.exists(BASE_PATH):
        print("No hay carpetas de servidores para eliminar.")
        return

    confirm = input(f"¿Estás seguro de que deseas eliminar TODOS los servidores en '{BASE_PATH}'? (s/n): ")
    if confirm.lower() != 's':
        print("Operación cancelada.")
        return

    shutil.rmtree(BASE_PATH)
    print(f"✅ Todos los servidores en '{BASE_PATH}' han sido eliminados.")

if __name__ == "__main__":
    cleanup()
