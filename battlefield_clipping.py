# https://ffmpeg.org/ffmpeg.html
# cmd version roughly: ffmpeg [-ss Input_start -t Input_duration -i Input_file] [-fpsmax Output_fps Output_file]
# example: ffmpeg -ss 00:15 -t 00:30 -i "...\Battlefield 2042.mp4" -fpsmax 40  "...\Battlefield 2042 MAV on board.webm"

# features to add
#   drag'n'drop - https://stackoverflow.com/questions/142844/drag-and-drop-onto-python-script-in-windows-explorer

# pip install ffmpeg-python
import ffmpeg

Input = input("Video filepath:  ")
Start = input("Seek to start time (MM:SS):  ")
Duration = input("Duration (MM:SS):  ")
Stream = ffmpeg.input(Input, ss=Start, t=Duration)
Fps = int(input("Output fps:  "))
Format = input("Output format (like webm):  ")
Out = ffmpeg.output(Stream, input("Output filepath:  "),  fpsmax=Fps, format=Format)

print('processing...')
Out.run()
print('done!')
