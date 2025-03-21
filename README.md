# Remote Access Tool (Python)

## 📌 Description

This Python script simulates a **remote access tool**.
It establishes a connection to a server and responds to various commands sent remotely.

![image](https://github.com/user-attachments/assets/8c1b7c04-f5fe-4647-948c-32c0de6703c2)

---

## 🛠 Features

- `infos` – Returns OS version and current working directory.
- `cd <path>` – Changes the current directory on the client.
- `dl <filename>` – Sends the specified file from the client machine to the server.
- `capture <name>` – Takes a screenshot and sends it as a `.png` file.
- `password` – Extracts saved passwords from Google Chrome using `chromepass`.
- Any other string is executed as a **shell command** (e.g., `ls`, `ipconfig`, etc.).

## 📦 Requirements

- Python 3.x
- [`Pillow`](https://pypi.org/project/Pillow/): `pip install pillow`
- [`chromepass`](https://pypi.org/project/chromepass/) – Only works on **Windows** with Chrome installed

---

## ⚙️ Usage Instructions (Local Test Only)

1. Set up a listener server to receive connections (not included in this repo).
2. Run this script on a test machine (preferably in a VM).
3. Send commands from the server and receive responses or files accordingly.

---
