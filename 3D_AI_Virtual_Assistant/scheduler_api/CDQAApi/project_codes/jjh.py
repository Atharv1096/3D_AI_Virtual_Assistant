import os
def slow_down_audio(input_file: str, output_file: str, factor: float):
    # Construct the ffmpeg command
    # Set the path to the bin folder of the FFmpeg folder
    ffmpeg_path = r"F:\ffmpeg\bin"

    # Add the FFmpeg path to the PATH environment variable
    os.environ["PATH"] += os.pathsep + ffmpeg_path

    cmd = f"ffmpeg -i {input_file} -filter:a atempo={factor} {output_file}"

    # Run the ffmpeg command
    os.system(cmd)


slow_down_audio("F:\\file.mp3", "F:\\slowed_file.mp3", 0.7)
