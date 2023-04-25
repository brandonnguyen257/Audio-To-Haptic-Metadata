'''
    audioLength: integer of the length of the audio in seconds
    sampleRatePerSecond: integer of the number of samples per second
    return: array of floats of the timestamps of each sample

    example: generateTimeStampsArray(1, 5) returns [0, 0.2, 0.4, 0.6, 0.8, 1.0]
'''
def generateTimeStampsArray(audioLength, sampleRatePerSecond):
    increment = (1/sampleRatePerSecond)*1.0
    numberOfTimeStamps = (audioLength * sampleRatePerSecond) + 1
    return [i*increment for i in range(0, numberOfTimeStamps)]

