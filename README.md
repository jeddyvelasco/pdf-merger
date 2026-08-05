# 📄 Offline PDF Merger (CustomTkinter + PyPDF)

A clean, modern, and privacy-focused desktop application to merge multiple PDF files locally on your machine. Built with Python, **CustomTkinter**, **TkinterDnD**, and **PyPDF**.

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)
![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey)

---

## ✨ Features

* **🔒 100% Offline & Private:** Your sensitive documents never leave your computer. No web servers or data collection.
* **🖱️ Drag & Drop Support:** Effortlessly drop your PDF files directly into the app window.
* **📂 Batch File Selector:** Prefer traditional browsing? Select multiple files at once using the file manager button.
* **🎨 Modern UI:** Built using `CustomTkinter` with native system light/dark mode adaptation.
* **⚡ Light & Fast:** Minimal dependencies, under 160 lines of code, and instantaneous file merging.

---

## 🛠️ Installation & Setup

### 1. Prerequisites
Ensure you have **Python 3.8+** installed on your system.

### 2. Clone the Repository
```bash
git clone https://github.com/jeddyvelasco/pdf-merger.git
cd pdf-merger
```

### 3. Create a Virtual Environment (Recommended)
```bash
# Windows
python -m venv .venv
.venv\Scripts\activate

# macOS / Linux
python3 -m venv .venv
source .venv/bin/activate
```

### 4. Install Dependencies
```bash
pip install customtkinter tkinterdnd2 pypdf
```

---

## 🚀 Running the App

Simply execute the main Python script:

```bash
python pdf_merger.py
```

---

## 💻 How It Works

1. Launch the application.
2. **Drag & Drop** your PDF files into the drop area, or click **Add PDFs** to select files from your computer.
3. Click **Merge & Save PDF**.
4. Choose a destination folder and file name for your merged PDF document.
5. Hit **Save** — done!

---

## 📦 Project Structure

```text
pdf-merger/
├── pdf_merger.py      # Main application script
├── README.md          # Project documentation
├── .gitignore         # Git ignore configuration
└── requirements.txt   # Python dependencies
```

---

## 📄 License

This project is open-source under the [MIT License](LICENSE). Feel free to modify and adapt it for personal or commercial projects.
