import matplotlib.pyplot as plt
import librosa
import time

'''
    audioLength: integer of the length of the audio in seconds
    sampleRatePerSecond: integer of the number of samples per second
    return: array of floats of the timestamps of each sample

    example: generateTimeStampsArray(1, 5) returns [0, 0.2, 0.4, 0.6, 0.8, 1.0]
'''
def get_time_stamps_array(audioLength, sampleRatePerSecond):
    increment = (1/sampleRatePerSecond) * 1.0
    numberOfTimeStamps = (audioLength * sampleRatePerSecond) + 1
    return [i * increment for i in range(0, numberOfTimeStamps)]

def get_audio_time_series_and_audio_samplerate(file_location, save_plot=False):

    start_time = time.time()
    print(f"Generating Audio Time Series for {file_location}...")
    audio_time_series , audio_samplerate = librosa.load(file_location)
    end_time = time.time()
    print(f"Audio Time Series Generated in {end_time - start_time} seconds")
    if save_plot:
        plt.figure(figsize=(30, 10))
        librosa.display.waveshow(audio_time_series, sr=audio_samplerate)
        saved_file_location = file_location.replace('.wav', '') + '_audio_time_series.png'
        plt.savefig(saved_file_location)
        print(f"Saved audio time series plot to {saved_file_location}")

    return audio_time_series, audio_samplerate

