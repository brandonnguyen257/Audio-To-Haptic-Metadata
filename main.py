from utils.haptic_utils import get_audio_duration, get_audio_and_audio_samplerate, get_time_stamps
from utils.parser_utils import get_input_sr_and_file_name
import time

start_time = time.time()

input_sr, file_name = get_input_sr_and_file_name()

audio, audio_sr = get_audio_and_audio_samplerate(file_name, save_plot=True)
audio_duration = get_audio_duration(audio, audio_sr)
print(f'{audio_duration=}')

time_stamps = get_time_stamps(audio_duration, input_sr)
print(time_stamps)
end_time = time.time()
print(f'Done in {end_time - start_time} seconds')