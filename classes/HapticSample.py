class HapticSample:
    MIN_HAPTIC_VALUE = -1.0
    MAX_HAPTIC_VALUE = 1.0
    MIN_TIMESTAMP = 0.0

    def __init__(self, time_stamp: float, haptic_value: float):
        self.time_stamp = time_stamp
        self.haptic_value = haptic_value

    @property
    def time_stamp(self):
        return self._time_stamp

    @time_stamp.setter
    def time_stamp(self, value):
        if value < HapticSample.MIN_TIMESTAMP:
            raise ValueError("Time stamp cannot be negative")
        self._time_stamp = value

    @property
    def haptic_value(self):
        return self._haptic_value

    @haptic_value.setter
    def haptic_value(self, value):
        if not HapticSample.MIN_HAPTIC_VALUE <= value <= HapticSample.MAX_HAPTIC_VALUE:
            raise ValueError("Haptic value must be between -1.0 and 1.0")
        self._haptic_value = value

    def __str__(self):
        return f'HapticSample({self.time_stamp}, {self.haptic_value})'

    def __repr__(self):
        return f'HapticSample({self.time_stamp}, {self.haptic_value})'

    def __eq__(self, other):
        if isinstance(other, HapticSample):
            return self.time_stamp == other.time_stamp and self.haptic_value == other.haptic_value
        return False

    def __hash__(self):
        return hash((self.time_stamp, self.haptic_value))
    
    def __dict__(self):
        return {'time_stamp': self.time_stamp, 'haptic_value': self.haptic_value}