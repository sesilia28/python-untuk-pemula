# Konfigurasi IDE

Catatan ini mengikuti materi Pycharm dan Instalasi Pycharm pada seri artikel #10.

## Fitur Pycharm

- Intelligent Coding Assistance: syntax highlighting, autocomplete, deteksi dan koreksi syntax error secara langsung
- Built-in Developer Tools: debugging, menjalankan script Python, membuat virtual environment, Python console
- VCS Support: mengunggah project ke repository GitHub

## Edisi Pycharm

- Professional: berbayar, fitur paling lengkap
- Community dan Edu: gratis, fitur lebih sedikit

## Cara instalasi

- Windows: unduh installer lalu jalankan sampai selesai
- Linux: ekstrak dengan `sudo tar xzf pycharm-*.tar.gz -C /opt/`, lalu jalankan `sh pycharm.sh` dari folder `bin`
- Ubuntu: `sudo snap install pycharm-community --classic`

## Lingkungan yang saya pakai

- Sistem: Arch Linux pada WSL2
- Python: 3.14 dengan virtual environment `venv`
- Editor: Neovim, pengaturan indentasi 4 spasi pada `.vscode/settings.json`
