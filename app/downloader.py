# python import
import os
import subprocess
from pathlib import Path

# third-party import
import requests

VANILLA_MANIFEST_URL = "https://launchermeta.mojang.com/mc/game/version_manifest_v2.json"
FORGE_PROMO_JSON = "https://files.minecraftforge.net/net/minecraftforge/forge/promotions_slim.json"
FORGE_MAVEN_URL = "https://maven.minecraftforge.net/net/minecraftforge/forge/"

def get_vanilla_versions():
    response = requests.get(VANILLA_MANIFEST_URL)
    data = response.json()["versions"]
    versions = set()

    for v in data:
        if v["type"] == "release":
            parsed = parse_version_tuple(v["id"])
            if parsed:
                versions.add((parsed, v["id"], v["url"]))
    return [{"id": v, "url": url} for _, v, url in sorted(versions, reverse=True)]

def download_vanilla_server(version_id, url, dest_dir):
    print(f"Obteniendo JAR para versión Vanilla {version_id}...")
    version_info = requests.get(url).json()
    server_url = version_info["downloads"]["server"]["url"]

    os.makedirs(dest_dir, exist_ok=True)
    jar_path = os.path.join(dest_dir, f"{version_id}.jar")

    with requests.get(server_url, stream=True) as r:
        with open(jar_path, "wb") as f:
            for chunk in r.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)
    print(f"Versión {version_id} descargada en {jar_path}")
    return jar_path

def parse_version_tuple(version_str):
    if all(part.isdigit() for part in version_str.split(".")):
        return tuple(map(int, version_str.split(".")))

def get_forge_versions():
    response = requests.get(FORGE_PROMO_JSON)
    data = response.json()["promos"]
    versions = set()

    for key, forge_version in data.items():
        if key.endswith("-recommended") or key.endswith("-latest"):
            mc_version = key.split("-")[0]
            mc_part = parse_version_tuple(mc_version)
            forge_part = parse_version_tuple(forge_version)
            if mc_part and forge_part:
              version_id = mc_version + "-" + forge_version
              versions.add(((mc_part, forge_part), version_id))
    return [{"id": v} for _, v in sorted(versions, reverse=True)]

def download_forge_server(forge_version, dest_dir):
    print(f"Descargando Forge {forge_version}...")

    installer_filename = f"forge-{forge_version}-installer.jar"
    installer_url = f"{FORGE_MAVEN_URL}{forge_version}/{installer_filename}"

    os.makedirs(dest_dir, exist_ok=True)
    installer_path = os.path.join(dest_dir, installer_filename)

    # Descargar el instalador
    with requests.get(installer_url, stream=True) as r:
        with open(installer_path, "wb") as f:
            for chunk in r.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)

    print("Instalador descargado. Ejecutando instalación del servidor...")

    # Convertir la ruta a una absoluta con formato correcto
    installer_path = str(Path(installer_path).resolve())

    result = subprocess.run(["java", "-jar", installer_path, "--installServer"], cwd=os.path.abspath(dest_dir))

    if result.returncode == 0:
        os.remove(installer_path)
        installer_log = installer_path + ".log"
        if os.path.exists(installer_log):
            os.remove(installer_log)
        print(f"Servidor Forge {forge_version} instalado en {dest_dir}")
    else:
        print("❌ Hubo un error al ejecutar el instalador de Forge.")
