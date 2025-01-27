import tkinter as tk
from tkinter import messagebox
import threading
import time
import random

# Global variable for timer thread
timer_running = False

# Fungsi Timer Belajar
def start_timer():
    global timer_running
    try:
        timer_running = True
        minutes = int(timer_input.get())
        seconds = minutes * 60
        while seconds > 0 and timer_running:
            mins, secs = divmod(seconds, 60)
            timer_label.config(text=f"{mins:02}:{secs:02}")
            app.update()
            time.sleep(1)
            seconds -= 1
        if timer_running:
            messagebox.showinfo("Waktu Habis", "Timer selesai!")
    except ValueError:
        messagebox.showwarning("Error", "Masukkan waktu dalam angka.")

def stop_timer():
    global timer_running
    timer_running = False

def clear_timer():
    stop_timer()
    timer_label.config(text="00:00")
    timer_input.delete(0, tk.END)

# Fungsi Catatan Harian
def save_note():
    with open("notes.txt", "w") as file:
        file.write(note_text.get("1.0", tk.END))
    messagebox.showinfo("Berhasil", "Catatan disimpan.")

def load_note():
    try:
        with open("notes.txt", "r") as file:
            note_text.delete("1.0", tk.END)
            note_text.insert(tk.END, file.read())
    except FileNotFoundError:
        messagebox.showwarning("Error", "File catatan tidak ditemukan.")

# Fungsi To-Do List


# Fungsi Kalkulator


# Fungsi Motivational Quote


# Aplikasi Utama
app = tk.Tk()
app.title("Student Productivity Toolkit")
app.geometry("900x600")
app.configure(bg="#f0f4f7")

# Frame Timer Belajar
frame_timer = tk.Frame(app, bg="#ffe0b2", relief="ridge", bd=5)
frame_timer.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
tk.Label(frame_timer, text="Timer Belajar", bg="#ffe0b2", font=("Arial", 16, "bold")).pack()
timer_input = tk.Entry(frame_timer, width=10, font=("Arial", 14))
timer_input.pack(pady=5)
tk.Button(frame_timer, text="Mulai Timer", command=lambda: threading.Thread(target=start_timer).start(), bg="#ff7043", fg="white", font=("Arial", 12)).pack(pady=5)
tk.Button(frame_timer, text="Hentikan Timer", command=stop_timer, bg="#ff7043", fg="white", font=("Arial", 12)).pack(pady=5)
tk.Button(frame_timer, text="Bersihkan Timer", command=clear_timer, bg="#ff7043", fg="white", font=("Arial", 12)).pack(pady=5)
timer_label = tk.Label(frame_timer, text="00:00", bg="#ffe0b2", font=("Arial", 24, "bold"))
timer_label.pack()

# Frame Catatan Harian
frame_notes = tk.Frame(app, bg="#bbdefb", relief="ridge", bd=5)
frame_notes.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)
tk.Label(frame_notes, text="Catatan Harian", bg="#bbdefb", font=("Arial", 16, "bold")).pack()
note_text = tk.Text(frame_notes, height=8, width=30, font=("Arial", 12))
note_text.pack(pady=5)
tk.Button(frame_notes, text="Simpan Catatan", command=save_note, bg="#1e88e5", fg="white", font=("Arial", 12)).pack(pady=5)
tk.Button(frame_notes, text="Buka Catatan", command=load_note, bg="#1e88e5", fg="white", font=("Arial", 12)).pack(pady=5)

# Frame To-Do List


# Frame Kalkulator


# Tombol Kalkulator


# Frame Motivational Quote


# Membuat layout grid responsif
app.grid_columnconfigure((0, 1, 2), weight=1)
app.grid_rowconfigure((0, 1), weight=1)

# Menjalankan aplikasi
app.mainloop()