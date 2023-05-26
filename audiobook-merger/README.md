# Context
**I wrote this script using ChatGPT to merge separate audiobook chapters into a single large file because Pocket Cast's cloud service (Pocket Cast Plus) does not allow users to create folders for individual audiobooks when uploading. So, I created this Python script to work around this limitation.**

**With my system, it takes approximately 2.14 seconds to encode 1MB of data. 27.2 MB per minute**

#
This code is used to merge a list of audio files into a single file using the ffmpeg command-line utility. The code begins by allowing the user to select the input audio files using a file selection dialog. It then sets the output file's extension to be the same as the input file's extension.

Next, the code creates a text file called input_list.txt and writes a list of the input audio file paths to it, with the file directive preceding each file path. This text file is used as input to ffmpeg.

Finally, the code runs the ffmpeg command using the subprocess module, passing in the following arguments:

- "-f": specifies the input format as concat, which allows ffmpeg to read a list of input files from a text file.
- "-safe": sets the safe option to 0, which allows ffmpeg to read input files from paths specified in the input_list.txt file.
- "-i": specifies the input file as input_list.txt.
- "-vn": tells ffmpeg to ignore any video streams in the input files.
- "-c:a": specifies the audio codec to use for the output file as libmp3lame.
- "-q:a": sets the audio quality to 1 (highest quality) for the libmp3lame codec.
- "-b:a": sets the audio bitrate to 128k for the output file.
- output_file: specifies the path to the output file.

After the ffmpeg command has finished running, the code deletes the input_list.txt file and prints a success message.


# Prerequisite
- You need to have ffmpeg installed: https://ffmpeg.org/download.html

# How TO RUN
- Run program with your favourite python gui/command line
- Make sure to point where your **ffmpeg** is installed: ```python ffmpeg_path = "C:/ffmpeg-2022-12-25-git-eeb280f351-full_build/bin/ffmpeg.exe"```
- Change the **output path**: output_folder = ```python "C:/Users/USER/Desktop/Output"```

# How TO USE
- Select multple files in a folder by control+left click or control+A (select all)


