import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from pytube import YouTube

def show_alert(alert):
    messagebox.showinfo(alert, "This is a simple alert!")

def open_file():
    filepath = filedialog.askdirectory()
    if filepath:
        pass
    else:
        show_alert("Select a file")
    return filepath

def submit_com():
    SAVE_PATH = open_file()
    link = search_var.get()
    
    try:
        yt = YouTube(link)
    except:
        show_alert("Connection Error")

    # Create a list of available streams and their quality
    streams = yt.streams.filter(progressive=True, file_extension='mp4')
    quality_options = [f"{stream.resolution} - {stream.mime_type}" for stream in streams]

    # Create radio buttons for each quality option
    for i, option in enumerate(quality_options):
        tk.Radiobutton(r, text=option, variable=selected_quality, value=i).pack()

    def download_selected_quality():
        selected_index = selected_quality.get()
        if selected_index < len(streams):
            selected_stream = streams[selected_index]
            try:
                selected_stream.download(output_path=SAVE_PATH)
                show_alert('Task Completed!')
            except Exception as e:
                show_alert(f"Error: {e}")

    download_button = tk.Button(r, text='Download Selected Quality', width=25, command=download_selected_quality)
    download_button.pack()

r = tk.Tk()
r.title('YouTube Video Downloader')

search_var = tk.StringVar()
selected_quality = tk.IntVar()

tk.Label(r, text="Enter the YouTube URL:").pack()
tk.Entry(r, textvariable=search_var, width=75).pack()

download_button = tk.Button(r, text='Get Available Qualities', width=25, command=submit_com)
download_button.pack()

r.mainloop()
