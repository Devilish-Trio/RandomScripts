import os
import subprocess
import tkinter as tk
from tkinter import filedialog

# Create a tkinter root window
root = tk.Tk()

# Hide the root window
root.withdraw()

# Prompt the user to select the input files
input_files = filedialog.askopenfilenames(title="Select the input files")

# Determine the input file's format
input_format = os.path.splitext(input_files[0])[1]

# Set the output file's extension based on the input file's format
output_ext = input_format

# Set the output file's path
output_folder = "C:/Users/USER/Desktop/Output"
output_file = os.path.join(output_folder, "output" + output_ext)

# Set the path to the ffmpeg executable
ffmpeg_path = "C:/ffmpeg-2022-12-25-git-eeb280f351-full_build/bin/ffmpeg.exe"

# Create a list file containing the paths of the input audio files
list_file_path = "input_list.txt"
with open(list_file_path, "w") as list_file:
    for input_file in input_files:
        list_file.write("file '" + input_file + "'\n")

# Convert all the audio files to .m4a format and merge them into a single output file
subprocess.run([ffmpeg_path, "-f", "concat", "-safe", "0", "-i", list_file_path, "-vn", "-c:a", "libmp3lame", "-q:a", "1", "-b:a", "128k", output_file])

# Delete the input list file
os.remove(list_file_path)

# Print a success message
print(f"Successfully merged {input_files} into {output_file}")
