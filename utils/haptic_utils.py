import matplotlib.pyplot as plt
import librosa
import time

'''
    return: array of the audio time series and the audio sample rate

    librosa.load loads an audio file and returns the time series
    It accepts keyword arguments such as sr (sample rate) and mono (whether or not to convert to mono)
    sr defaults to 22050
    mono defaults to True
    https://librosa.org/doc/latest/generated/librosa.load.html
'''
def get_audio_and_audio_samplerate(file_location: str, save_plot: bool=False):
    start_time = time.time()
    print(f"Generating Audio Time Series for {file_location}...")
    audio , audio_sr = librosa.load(file_location)
    end_time = time.time()
    print(f"Audio Time Series Generated in {end_time - start_time} seconds")
    if save_plot:
        plt.figure(figsize=(30, 10))
        librosa.display.waveshow(audio, sr=audio_sr)
        saved_file_location = file_location.replace('.wav', '') + '_audio.png'
        plt.savefig(saved_file_location)
        print(f"Saved audio time series plot to {saved_file_location}")
    return audio, audio_sr

def get_audio_duration(audio: list[float], audio_sr: int):
    return len(audio) / audio_sr

'''
    audioLength: integer of the length of the audio in seconds
    sampleRatePerSecond: integer of the number of samples per second
    return: array of floats of the timestamps of each sample

    example: generateTimeStampsArray(1, 5) returns [0, 0.2, 0.4, 0.6, 0.8, 1.0]
'''
def get_time_stamps(audio_duration: float, sr: int):
    increment = (1/sr) * 1.0
    num_time_stamps = int(audio_duration * sr) + 1
    return [i * increment for i in range(0, num_time_stamps)]

'''
    hpps: harmonic-percussive source separation
    this method will seperate the audio into harmonic and percussive components
    https://librosa.org/doc/latest/generated/librosa.effects.hpss.html
'''
def get_harmonics_and_percussive(audio: list[float]):
    harmonic, percussive = librosa.effects.hpss(audio)
    return harmonic, percussive
