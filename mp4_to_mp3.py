import tkinter as tk
from tkinter import filedialog
from moviepy.editor import VideoFileClip

def mp4_to_mp3(mp4_file, mp3_file):
    # Load the video clip
    video_clip = VideoFileClip(mp4_file)
    
    # Extract audio
    audio_clip = video_clip.audio
    
    # Write audio to a new file
    audio_clip.write_audiofile(mp3_file)
    
    # Close the clips
    audio_clip.close()
    video_clip.close()

def browse_mp4_file():
    filename = filedialog.askopenfilename(filetypes=[("MP4 files", "*.mp4")])
    if filename:
        mp4_entry.delete(0, tk.END)
        mp4_entry.insert(0, filename)

def browse_mp3_file():
    filename = filedialog.asksaveasfilename(defaultextension=".mp3", filetypes=[("MP3 files", "*.mp3")])
    if filename:
        mp3_entry.delete(0, tk.END)
        mp3_entry.insert(0, filename)

def convert():
    mp4_file = mp4_entry.get()
    mp3_file = mp3_entry.get()
    if mp4_file and mp3_file:
        mp4_to_mp3(mp4_file, mp3_file)
        status_label.config(text="Conversion completed!")
    else:
        status_label.config(text="Please select input and output files.")

# Create the main window
root = tk.Tk()
root.title("MP4 to MP3 Converter")

# Frame for input file
frame1 = tk.Frame(root)
frame1.pack(pady=10)

mp4_label = tk.Label(frame1, text="Select MP4 File:")
mp4_label.grid(row=0, column=0, padx=5, pady=5)

mp4_entry = tk.Entry(frame1, width=40)
mp4_entry.grid(row=0, column=1, padx=5, pady=5)

mp4_button = tk.Button(frame1, text="Browse", command=browse_mp4_file)
mp4_button.grid(row=0, column=2, padx=5, pady=5)

# Frame for output file
frame2 = tk.Frame(root)
frame2.pack(pady=10)

mp3_label = tk.Label(frame2, text="Save MP3 File As:")
mp3_label.grid(row=0, column=0, padx=5, pady=5)

mp3_entry = tk.Entry(frame2, width=40)
mp3_entry.grid(row=0, column=1, padx=5, pady=5)

mp3_button = tk.Button(frame2, text="Browse", command=browse_mp3_file)
mp3_button.grid(row=0, column=2, padx=5, pady=5)

# Convert button
convert_button = tk.Button(root, text="Convert", command=convert)
convert_button.pack(pady=10)

# Status label
status_label = tk.Label(root, text="")
status_label.pack()

# Run the GUI
root.mainloop()
