# 🔐 Key Generator

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)
[![GitHub Stars](https://img.shields.io/github/stars/createrman-system/key-generator?style=social)](https://github.com/createrman-system/key-generator)
[![GitHub Forks](https://img.shields.io/github/forks/createrman-system/key-generator?style=social)](https://github.com/createrman-system/key-generator)
[![Downloads](https://img.shields.io/github/downloads/createrman-system/key-generator/total)](https://github.com/createrman-system/key-generator/releases)
[![Latest Release](https://img.shields.io/github/v/release/createrman-system/key-generator)](https://github.com/createrman-system/key-generator/releases)

A powerful and secure command-line tool for generating cryptographically strong random keys with customizable character sets and safe file handling.

---

## ✨ Overview

**Key Generator** is a lightweight yet professional CLI utility designed for developers, security enthusiasts, and anyone who needs strong random keys.

Built with Python’s secure `secrets` module, it ensures high-quality randomness suitable for cryptographic use cases.

---

## 🚀 Features

* 🔒 **Cryptographically Secure** — powered by `secrets`
* 🎯 **Flexible Character Sets**

  * `abc` → letters (A–Z, a–z)
  * `123` → digits (0–9)
  * `abc123` → alphanumeric
* 📁 **Safe File Writing**



  * File access restricted to owner only
* 📊 **Entropy Calculation**

  * Displays key strength in bits
* 🎨 **Professional CLI Output**

  * Styled terminal interface

---

## 📦 Installation

No external dependencies required.

```bash
git clone https://github.com/createrman-system/key-generator.git
cd key-generator
```

---

## ▶️ Usage

```bash
python main.py <length> <charset> [filename]
```

### Arguments

| Argument   | Description                                 |
| ---------- | ------------------------------------------- |
| `length`   | Number of characters in the key             |
| `charset`  | `abc`, `123`, or `abc123`                   |
| `filename` | (Optional) Output file (default: `key.txt`) |

---

## 📌 Examples

### Generate a 32-character key (letters only)

```bash
python main.py 32 abc
```

### Generate a numeric key

```bash
python main.py 64 123 numbers.txt
```

### Generate a strong alphanumeric key

```bash
python main.py 128 abc123 secure_key.txt
```

---



## 📊 Entropy & Strength

Entropy is calculated using:

```
entropy = log2(pool_size) × key_length
```

| Entropy    | Strength       |
| ---------- | -------------- |
| < 128 bits | Standard       |
| ≥ 128 bits | Military-Grade |

---

## ⚠️ Notes

* Always store generated keys securely
* Never share sensitive keys publicly

---

## 🛠️ Roadmap

* [ ] GUI version

---

## 📄 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

Created by **createrman-system** 🚀
