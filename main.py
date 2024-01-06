from classes.HapticSample import HapticSample
from utils.haptic_utils import get_audio_duration, get_audio_and_audio_samplerate, get_haptic_samples, get_harmonics_and_percussive, get_time_stamp_indicies, get_time_stamps
from utils.parser_utils import get_input_sr_and_file_name
import time
import json

start_time = time.time()

#Step 1
input_sr, file_name = get_input_sr_and_file_name()

#Step 2
audio, audio_sr = get_audio_and_audio_samplerate(file_name, save_plot=True)
audio_duration = get_audio_duration(audio, audio_sr)

#Step 3
time_stamps = get_time_stamps(audio_duration, input_sr)

#Step 4

#TODO: look into if using harmonic or percussive components results in a better haptic experience
#harmonic, percussive = get_harmonics_and_percussive(audio)
haptic_samples = get_haptic_samples(audio, audio_sr, time_stamps)

#Step 5
haptic_samples_list = [sample.__dict__() for sample in haptic_samples]
data = {
    "num_haptic_samples": len(haptic_samples_list),
    "audio_duration_seconds": audio_duration,
    "input_sr": input_sr,
    "haptic_samples": haptic_samples_list
}

jsonResponse = json.dumps(data)
with open(file_name + 'output.json', 'w') as f:
    json.dump(data, f, indent=4)


haptic_generation_time = time.time()- start_time 
print(f'Haptic Generation Completed in {haptic_generation_time} seconds for a {audio_duration} second audio clip with {input_sr} samples per second')