from utils.haptic_utils import get_audio_duration, get_audio_and_audio_samplerate, get_haptic_samples, get_harmonics_and_percussive, get_time_stamp_indicies, get_time_stamps
from utils.parser_utils import get_input_sr_and_file_name
import time

start_time = time.time()

input_sr, file_name = get_input_sr_and_file_name()

audio, audio_sr = get_audio_and_audio_samplerate(file_name, save_plot=True)
audio_duration = get_audio_duration(audio, audio_sr)

time_stamps = get_time_stamps(audio_duration, input_sr)

#TODO: look into if using harmonic or percussive components results in a better haptic experience
#harmonic, percussive = get_harmonics_and_percussive(audio)
haptic_samples = get_haptic_samples(audio, audio_sr, time_stamps)

#TODO: convert haptic_samples to JSON

#debug statements
print(f'{audio_duration=}')
print(f'{input_sr=}')
print(f'{audio_duration*input_sr=}')
print(len(haptic_samples))

end_time = time.time()
print(f'Done in {end_time - start_time} seconds')


