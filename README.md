# 🔐 Key Generator

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)
[![GitHub Stars](https://img.shields.io/github/stars/createrman-system/key-generator?style=social)](https://github.com/createrman-system/key-generator)
[![GitHub Forks](https://img.shields.io/github/forks/createrman-system/key-generator?style=social)](https://github.com/createrman-system/key-generator)
[![Latest Release](https://img.shields.io/github/v/release/createrman-system/key-generator)](https://github.com/createrman-system/key-generator/releases)

A powerful and secure tool for generating cryptographically strong random keys with flexible character sets, safe file handling, and both **CLI** and **GUI** interfaces.

---

## ✨ Overview

**Key Generator** is designed for developers, security enthusiasts, and anyone needing strong random keys.  
It offers:

* Cryptographically secure key generation using Python's `secrets` module.
* Entropy calculation to evaluate key strength.
* Modern GUI for easy use without a terminal.

---

## 🚀 Features

### 🔹 CLI Version

* **Secure & Flexible:** Choose letters, numbers, or both (`abc`, `123`, `abc123`).
* **Safe File Writing:** Writes to a temporary file first and restricts permissions.
* **Entropy Display:** Shows bits of entropy and classifies key strength.
* **Professional Terminal UI:** Styled output with colored bars, headings, and warnings.

### 🔹 GUI Version

* **Modern Interface:** Dark mode, animated buttons, cards, and input fields.
* **Drag & Drop / File Picker:** Easily select output file locations.
* **Automatic `main.py` Check & Download:** Ensures required script exists.
* **Live Output Console:** Shows CLI output, errors, and status messages in real-time.
* **Friendly Charset Options:** `numbers`, `words`, `words+numbers`.

---

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/createrman-system/key-generator.git
cd key-generator
```

### Dependencies

**CLI only:** None (uses Python standard library).  

**GUI:** Install dependencies via pip:

```bash
pip install customtkinter requests
```

---

## ▶️ Usage

### CLI

```bash
python main.py <length> <charset> [filename]
```

**Arguments:**

| Argument   | Description                                 |
| ---------- | ------------------------------------------- |
| `length`   | Number of characters in the key             |
| `charset`  | `abc` (letters), `123` (digits), `abc123` (alphanumeric) |
| `filename` | (Optional) Output file (default: `key.txt`) |

**Examples:**

```bash
# Letters only, 32 chars
python main.py 32 abc

# Numeric key, 64 chars, custom file
python main.py 64 123 numbers.txt

# Strong alphanumeric key, 128 chars
python main.py 128 abc123 secure_key.txt
```

---

### GUI

Run the GUI with:

```bash
python gui.py
```

**Steps:**

1. Enter the key length.
2. Select character set: `numbers`, `words`, `words+numbers`.
3. Optionally choose an output file or leave default.
4. Click **Generate Key**.
5. View the generated key and status in the output console.

---

## 📊 Entropy & Strength

Entropy formula:

```python
entropy = log2(pool_size) × key_length
```

| Entropy    | Strength       |
| ---------- | -------------- |
| < 128 bits | Standard       |
| ≥ 128 bits | Military-Grade |

---

## ⚠️ Notes

* Keep generated keys secure.
* Do not share sensitive keys publicly.
* GUI requires `main.py` to exist in the folder (automatic download supported).

---

## 🛠️ Roadmap

* [x] CLI version
* [x] GUI version
* [ ] Multi-language support

---

## 📄 License

MIT License – see [LICENSE](LICENSE) for details.

---

## 👨‍💻 Author

Created by **createrman-system** 🚀

