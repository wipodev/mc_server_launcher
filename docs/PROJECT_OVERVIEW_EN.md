
# 📝 Project Report: MC Server Launcher

## 📌 Project Description

MC Server Launcher is a desktop application developed in Python using Tkinter that allows users to quickly download Minecraft servers, either in their Vanilla (official) or Forge (modded) versions. The main goal is to provide a simple and visual tool for users unfamiliar with the manual download and setup process of servers.

This tool aims to reduce the download process to just a few clicks, offering an intuitive interface with server type selection, version selection, and quick search capability.

## ✅ Current Status

### 1. Application Structure

- Application developed with Tkinter.
- Separation between UI logic and download logic (`downloader.py`).
- Functional graphical interface: radio buttons for server type selection, combobox to choose version, and download button.

### 2. Implemented Features

- Fetching Vanilla versions from Mojang's official manifest.
- Fetching Forge versions from the official promos JSON.
- Proper version ordering by release date.
- Combobox with updated versions depending on the selected type.
- Search field to filter versions inside the combobox.
- Error handling (failed downloads, connection issues, etc.).
- Automatic download of the selected server `.jar` file into a specific folder (`servers/vanilla` or `servers/forge`).

### 3. User Interface

- Radio buttons to select between “Vanilla” and “Forge”.
- Combobox to choose the version.
- Centered and shorter input field to filter/search versions.
- Status labels to inform progress (loading, downloading, error, completed).

## 🔧 Pending Features / Improvements

| Area            | Task                                                                 |
|-----------------|----------------------------------------------------------------------|
| Downloads       | Verify integrity of the downloaded `.jar` file (optional checksum).  |
| UI              | Improve visual design with themes or dark mode support.              |
| Compatibility   | Add support for Fabric and/or Quilt.                                 |
| Configuration   | Allow configuring and generating the `server.properties` file.       |
| Execution       | Add button to launch the downloaded server.                          |
| History/Logs    | Log download history or errors.                                      |
| Packaging       | Convert the app into an executable (e.g., using PyInstaller).        |
| Internationalization | Support for multiple languages (Spanish, English).             |
| Documentation   | Add in-app help/documentation.                                       |

## 🎯 Final Objective

The objective is to build a stable, cross-platform, and user-friendly tool that helps Minecraft players and server administrators download, prepare, and manage servers in just a few steps, removing the need for manual processes, command lines, or external links.
