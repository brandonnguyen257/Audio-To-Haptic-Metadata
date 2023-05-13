
from utils.haptic_utils import get_audio_time_series_and_audio_samplerate
from utils.parser_utils import get_sample_rate_and_file_name
import time

start_time = time.time()

sample_rate, file_name = get_sample_rate_and_file_name()

audio_time_series, audio_samplerate = get_audio_time_series_and_audio_samplerate(file_name, save_plot=True)


end_time = time.time()
print(f'Done in {end_time - start_time} seconds')