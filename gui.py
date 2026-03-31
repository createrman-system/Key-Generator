import customtkinter as ctk
import subprocess
import threading
import sys
import os
import requests
from tkinter import filedialog

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# ===== CONFIG =====
MAIN_URL = "https://raw.githubusercontent.com/createrman-system/Key-Generator/refs/heads/main/main.py"
MAIN_FILE = "main.py"

# Friendly charset mapping
CHARSET_MAP = {
    "numbers": "123",
    "words": "abc",
    "words+numbers": "abc123"
}


class KeyGeneratorGUI(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("🔐 Key Generator Pro")
        self.geometry("720x520")
        self.resizable(False, False)

        # ===== TITLE =====
        self.title_label = ctk.CTkLabel(
            self, text="🔐 Key Generator Pro",
            font=("Segoe UI", 28, "bold")
        )
        self.title_label.pack(pady=15)

        # ===== MAIN CARD =====
        self.card = ctk.CTkFrame(self, corner_radius=15)
        self.card.pack(padx=20, pady=10, fill="both")

        # ===== INPUTS =====
        self.length_entry = ctk.CTkEntry(
            self.card,
            placeholder_text="Key Length (e.g. 32)",
            height=40
        )
        self.length_entry.pack(pady=10, padx=20, fill="x")

        self.charset_option = ctk.CTkOptionMenu(
            self.card,
            values=list(CHARSET_MAP.keys()),
            height=35
        )
        self.charset_option.set("words+numbers")  # default
        self.charset_option.pack(pady=10, padx=20, fill="x")

        # ===== FILE PICKER =====
        file_frame = ctk.CTkFrame(self.card, fg_color="transparent")
        file_frame.pack(pady=10, padx=20, fill="x")

        self.file_entry = ctk.CTkEntry(
            file_frame,
            placeholder_text="Output file (optional)",
            height=35
        )
        self.file_entry.pack(side="left", fill="x", expand=True, padx=(0, 10))

        self.browse_btn = ctk.CTkButton(
            file_frame,
            text="Browse",
            width=100,
            command=self.pick_file
        )
        self.browse_btn.pack(side="right")

        # ===== GENERATE BUTTON =====
        self.generate_btn = ctk.CTkButton(
            self.card,
            text="Generate Key",
            height=45,
            font=("Segoe UI", 14, "bold"),
            command=self.start_generation
        )
        self.generate_btn.pack(pady=15, padx=20, fill="x")

        # ===== STATUS =====
        self.status_label = ctk.CTkLabel(
            self.card,
            text="Checking main.py...",
            text_color="gray"
        )
        self.status_label.pack(pady=(0, 10))

        # ===== OUTPUT =====
        self.output_card = ctk.CTkFrame(self, corner_radius=15)
        self.output_card.pack(padx=20, pady=10, fill="both", expand=True)

        self.output_box = ctk.CTkTextbox(self.output_card)
        self.output_box.pack(padx=10, pady=10, fill="both", expand=True)

        # ===== CHECK FILE =====
        self.check_main_file()

    # ===== AUTO DOWNLOAD =====
    def check_main_file(self):
        if not os.path.exists(MAIN_FILE):
            self.status_label.configure(text="⬇️ Downloading main.py...", text_color="yellow")
            threading.Thread(target=self.download_main).start()
        else:
            self.status_label.configure(text="✅ main.py found", text_color="green")

    def download_main(self):
        try:
            r = requests.get(MAIN_URL, timeout=10)
            if r.status_code == 200:
                with open(MAIN_FILE, "w", encoding="utf-8") as f:
                    f.write(r.text)
                self.status_label.configure(text="✅ main.py downloaded", text_color="green")
                self.log("✔ main.py downloaded successfully")
            else:
                self.status_label.configure(text="❌ Download failed", text_color="red")
                self.log("❌ Failed to download main.py")

        except Exception as e:
            self.status_label.configure(text="❌ Network error", text_color="red")
            self.log(f"❌ Error: {e}")

    # ===== FILE PICKER =====
    def pick_file(self):
        file_path = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
        )
        if file_path:
            self.file_entry.delete(0, "end")
            self.file_entry.insert(0, file_path)

    # ===== LOG =====
    def log(self, text):
        self.output_box.insert("end", text + "\n")
        self.output_box.see("end")

    # ===== START =====
    def start_generation(self):
        threading.Thread(target=self.run_generator).start()
        self.animate_button()

    # ===== ANIMATION =====
    def animate_button(self):
        self.generate_btn.configure(text="Generating...")
        self.after(1200, lambda: self.generate_btn.configure(text="Generate Key"))

    # ===== RUN CLI =====
    def run_generator(self):
        if not os.path.exists(MAIN_FILE):
            self.log("❌ main.py not found")
            return

        length = self.length_entry.get()
        charset_key = self.charset_option.get()
        charset_value = CHARSET_MAP.get(charset_key, "abc123")
        filename = self.file_entry.get()

        if not length.isdigit():
            self.status_label.configure(text="❌ Length must be number", text_color="red")
            return

        cmd = [sys.executable, MAIN_FILE, length, charset_value]
        if filename.strip():
            cmd.append(filename)

        try:
            self.status_label.configure(text="⚙️ Running...", text_color="yellow")

            result = subprocess.run(cmd, capture_output=True, text=True)

            if result.stdout:
                self.log(result.stdout)

            if result.stderr:
                self.log("❌ ERROR:")
                self.log(result.stderr)
                self.status_label.configure(text="Error occurred", text_color="red")
                return

            self.status_label.configure(text="✅ Done", text_color="green")

        except Exception as e:
            self.log(f"❌ Failed: {e}")
            self.status_label.configure(text="Execution failed", text_color="red")


if __name__ == "__main__":
    app = KeyGeneratorGUI()
    app.mainloop()