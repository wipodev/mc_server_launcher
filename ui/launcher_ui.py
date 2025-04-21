# third-party import
import tkinter as tk
from tkinter import ttk, messagebox

# local imports
from app import downloader
from i18n.i18n import load_locale, t

load_locale("en")

class LauncherUI:
    def __init__(self, root):
        self.root = root
        self.root.title(t("title"))

        # Estilo básico
        self.root.geometry("400x250")
        self.root.resizable(False, False)

        self.version_type = tk.StringVar(value="vanilla")
        self.selected_version = tk.StringVar()
        self.search_text = tk.StringVar()

        # Tipo de servidor
        type_frame = ttk.LabelFrame(root, text=t("select_server_type"))
        type_frame.pack(padx=10, pady=10, fill="x")

        ttk.Radiobutton(type_frame, text=t("vanilla"), variable=self.version_type, value="vanilla", command=self.update_versions).pack(side="left", padx=10)
        ttk.Radiobutton(type_frame, text=t("forge"), variable=self.version_type, value="forge", command=self.update_versions).pack(side="left", padx=10)

        # Campo de búsqueda
        search_frame = ttk.Frame(root)
        search_frame.pack(pady=5)

        ttk.Label(search_frame, text=t("search_version")).pack()
        search_entry = ttk.Entry(search_frame, textvariable=self.search_text, width=25)
        search_entry.pack()
        self.search_text.trace_add("write", self.filter_versions)

        # Selector de versión
        ttk.Label(root, text=t("select_version")).pack()
        self.version_combobox = ttk.Combobox(root, textvariable=self.selected_version, state="readonly")
        self.version_combobox.pack(pady=5)

        # Botón de descarga
        ttk.Button(root, text=t("download_server"), command=self.download_selected).pack(pady=10)

        # Estado
        self.status_label = ttk.Label(root, text="")
        self.status_label.pack()

        self.all_versions = []
        self.version_data = {}
        self.update_versions()

    def update_versions(self):
        tipo = self.version_type.get()
        self.status_label.config(text=t("getting_versions"))
        self.root.update()

        try:
            if tipo == "vanilla":
                versions = downloader.get_vanilla_versions()
            else:
                versions = downloader.get_forge_versions()
            self.all_versions = versions
            self.version_data = {v["id"]: v for v in versions}
            self.filter_versions()
            self.status_label.config(text=t("status_ready"))
        except Exception as e:
            messagebox.showerror("Error", f"{t('error_fetch_versions')} {e}")
            self.status_label.config(text=f"Error: {t('status_error')} {e}")

    def filter_versions(self, *_):
        query = self.search_text.get().lower()
        filtered = [v["id"] for v in self.all_versions if query in v["id"].lower()]
        self.version_combobox["values"] = filtered

        if filtered:
            self.version_combobox.set(filtered[0])
        else:
            self.version_combobox.set("")

    def download_selected(self):
        version_id = self.selected_version.get()
        tipo = self.version_type.get()
        self.status_label.config(text=t("status_downloading"))
        self.root.update()

        try:
            if tipo == "vanilla":
                url = self.version_data[version_id]["url"]
                downloader.download_vanilla_server(version_id, url, f"servers/vanilla/{version_id}")
            else:
                downloader.download_forge_server(version_id, f"servers/forge/{version_id}")

            messagebox.showinfo("Completado", t("download_success").format(version=version_id))
            self.status_label.config(text=t("status_ready"))
        except Exception as e:
            messagebox.showerror("Error", f"{t('download_fail')} {e}")
            self.status_label.config(text=t('status_error'))

