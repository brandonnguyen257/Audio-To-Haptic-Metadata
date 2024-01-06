import matplotlib.pyplot as plt
import librosa
import time

from classes.HapticSample import HapticSample

'''
    return: array of the audio time series and the audio sample rate

    librosa.load loads an audio file and returns the time series
    It accepts keyword arguments such as sr (sample rate) and mono (whether or not to convert to mono)
    sr defaults to 22050
    mono defaults to True
    https://librosa.org/doc/latest/generated/librosa.load.html
'''
def get_audio_and_audio_samplerate(file_location: str, save_plot: bool=False):
    print(f"Generating Audio Time Series for {file_location}...")
    audio , audio_sr = librosa.load(file_location)
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
    print("Generating Harmonics and Percussive Components")
    harmonic, percussive = librosa.effects.hpss(audio)
    return harmonic, percussive



def get_haptic_samples(audio, audio_sr, time_stamps):
    time_stamp_indices = get_time_stamp_indicies(time_stamps, audio_sr)
    num_audio_sample = len(audio)

    #TODO: optimize to use 1 for loop
    haptic_values = []
    for index in time_stamp_indices:
        if index < 0 or index >= len(audio):
            haptic_values.append(audio[min(max(index, 0), num_audio_sample-1)])
        else:
            haptic_values.append((audio[index -1 ] + audio[index] + audio[index+1])/3.0 )
    
    haptic_samples = []
    for i in range(len(time_stamps)):
        sample = HapticSample(time_stamps[i], haptic_values[i])
        haptic_samples.append(sample)
    return haptic_samples

'''
Grabs the corresponding indices for the time stamps
'''
def get_time_stamp_indicies(time_stamps, audio_sr):
    return [int(time_stamp * audio_sr) for time_stamp in time_stamps]
