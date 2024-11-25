import tkinter as tk
from tkinter import ttk
import win32gui
import win32process
import psutil
from config import Config

# Function to get a list of window titles and process names
def get_window_titles_and_processes():
    def enum_windows_callback(hwnd, results):
        if win32gui.IsWindowVisible(hwnd) and win32gui.GetWindowText(hwnd):
            _, pid = win32process.GetWindowThreadProcessId(hwnd)
            process_name = psutil.Process(pid).name()
            window_title = win32gui.GetWindowText(hwnd)
            results.append((window_title, process_name))
    results = []
    win32gui.EnumWindows(enum_windows_callback, results)
    return results

# Function to display the popup window and handle the selection
def show_window_selection_popup():
    window_titles_and_processes = get_window_titles_and_processes()

    def connect():
        selected_index = listbox.curselection()[0]
        selected_title, selected_process = window_titles_and_processes[selected_index]
        Config().advanced_options["hwnd_window_title"] = selected_title
        Config().advanced_options["hwnd_window_process"] = selected_process
        root.destroy()

    root = tk.Tk()
    root.title("Select Window and Process")

    frame = ttk.Frame(root, padding="10")
    frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

    listbox = tk.Listbox(frame, height=20, width=50)
    for title, process in window_titles_and_processes:
        listbox.insert(tk.END, f"{title} - {process}")
    listbox.grid(row=0, column=0, columnspan=2, sticky=(tk.W, tk.E))

    connect_button = ttk.Button(frame, text="Connect", command=connect)
    connect_button.grid(row=1, column=0, columnspan=2, pady=10)

    root.mainloop()

# Call the function to show the popup window
show_window_selection_popup()