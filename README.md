Haptic Metadata Generation.

This script creates a 

1. User inputs audio file and sample rate
2. Audio file is converted into audio time series (list of audio amplitudes between -1 and 1 where 0 is the "median/average" amplitude)
3. Get the list of time stamps we want to generate haptic samples for
4. Generate haptic samples for each time stamp from the audio time series
5. Return the haptic samples as a JSON response


Set Up Steps

1. Activate venv by running this command in the terminal

source ./venv/bin/activate

2. Install necessary packages in the venv by running this command

pip install -r requirements.txt

3. Generate haptic metadata by running the this command

python main.py {sampleRate} {audioFile}

Examples with .mp3 files provided

ex: python main.py 30 delilah-FredAgain.mp3

ex: python main.py 30 sunSala.mp3

If you want to use your own audiofiles, add your own file in the same directory as the above .mp3 files

4. png file of the audio frequency and .json file of the haptic metadata will be outputted in this format

{audioFile}_audio.png

{audioFile}output.json