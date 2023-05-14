import argparse
import os

def audio_file_type(file_path):
    if not os.path.isfile(file_path):
        raise argparse.ArgumentTypeError(f"{file_path} is not a valid file path")
    if not file_path.lower().endswith((".wav", ".mp3", ".flac")):
        raise argparse.ArgumentTypeError("Only WAV, MP3, and FLAC files are supported")
    return file_path

def get_input_sr_and_file_name():
    # Parse arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("input_sr", type=int)
    parser.add_argument("file_name", type=audio_file_type)
    args = parser.parse_args()
    input_sr, file_name = args.input_sr, args.file_name
    return input_sr, file_name