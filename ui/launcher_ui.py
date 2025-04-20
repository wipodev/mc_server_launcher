# third-party import
import tkinter as tk
from tkinter import ttk, messagebox

# local imports
from utils import downloader

class LauncherUI:
    def __init__(self, root):
        self.root = root
        self.root.title("MC Server Launcher")

        # Estilo básico
        self.root.geometry("400x250")
        self.root.resizable(False, False)

        self.version_type = tk.StringVar(value="vanilla")
        self.selected_version = tk.StringVar()

        # Tipo de servidor
        type_frame = ttk.LabelFrame(root, text="Tipo de servidor")
        type_frame.pack(padx=10, pady=10, fill="x")

        ttk.Radiobutton(type_frame, text="Vanilla", variable=self.version_type, value="vanilla", command=self.update_versions).pack(side="left", padx=10)
        ttk.Radiobutton(type_frame, text="Forge", variable=self.version_type, value="forge", command=self.update_versions).pack(side="left", padx=10)

        # Selector de versión
        ttk.Label(root, text="Selecciona una versión:").pack()
        self.version_combobox = ttk.Combobox(root, textvariable=self.selected_version, state="readonly")
        self.version_combobox.pack(pady=5)

        # Botón de descarga
        ttk.Button(root, text="Descargar servidor", command=self.download_selected).pack(pady=10)

        # Estado
        self.status_label = ttk.Label(root, text="")
        self.status_label.pack()

        self.update_versions()

    def update_versions(self):
        tipo = self.version_type.get()
        self.status_label.config(text="Obteniendo versiones...")
        self.root.update()

        try:
            if tipo == "vanilla":
                versions = downloader.get_vanilla_versions()
            else:
                versions = downloader.get_forge_versions()
            self.version_combobox["values"] = [v["id"] for v in versions]
            self.version_combobox.set(versions[0]["id"])
            self.version_data = {v["id"]: v for v in versions}
            self.status_label.config(text="Listo.")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo obtener versiones: {e}")
            self.status_label.config(text=f"Error: No se pudo obtener versiones: {e}")

    def download_selected(self):
        version_id = self.selected_version.get()
        tipo = self.version_type.get()
        self.status_label.config(text="Descargando...")
        self.root.update()

        try:
            if tipo == "vanilla":
                url = self.version_data[version_id]["url"]
                downloader.download_vanilla_server(version_id, url, f"servers/vanilla/{version_id}")
            else:
                downloader.download_forge_server(version_id, f"servers/forge/{version_id}")

            messagebox.showinfo("Completado", f"Versión {version_id} descargada con éxito.")
            self.status_label.config(text="Descarga completada.")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo descargar: {e}")
            self.status_label.config(text="Error durante la descarga.")

