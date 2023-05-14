import os
import sys 
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from classes.HapticSample import HapticSample
import pytest

def test_time_stamp_setter():
    hapticSample = HapticSample(1.0, 0.3)
    assert hapticSample.time_stamp == 1.0
    hapticSample.time_stamp = 3.1
    assert hapticSample.time_stamp == 3.1

def test_under_MIN_TIMESTAMP_error():
    hapticSample = HapticSample(1.0, 0.3)
    with pytest.raises(ValueError):
        hapticSample.time_stamp = -1.0

def test_time_stamp_error_non_float():
    hapticSample = HapticSample(1.0, 0.3)
    with pytest.raises(TypeError):
        hapticSample.time_stamp = 'a'

def test_time_stamp_constructor_error():
    with pytest.raises(ValueError):
        HapticSample(-1.0, 0.3)

def test_haptic_value_setter():
    hapticSample = HapticSample(1.0, 0.3)
    assert hapticSample.haptic_value == 0.3
    hapticSample.haptic_value = 0.5
    assert hapticSample.haptic_value == 0.5

def test_over_MAX_HAPTIC_VALUE_error():
    hapticSample = HapticSample(1.0, 0.3)
    with pytest.raises(ValueError):
        hapticSample.haptic_value = 1.1

def test_under_MIN_HAPTIC_VALUE_error():
    hapticSample = HapticSample(1.0, 0.3)
    with pytest.raises(ValueError):
        hapticSample.haptic_value = -3.4

def test_haptic_value_error_non_float():
    hapticSample = HapticSample(1.0, 0.3)
    with pytest.raises(TypeError):
        hapticSample.haptic_value = 'a'

def test_haptic_value_constructor_error():
    with pytest.raises(ValueError):
        HapticSample(1.0, -1.1)

def test_str():
    hapticSample = HapticSample(1.0, 0.3)
    assert str(hapticSample) == 'HapticSample(1.0, 0.3)'

def test_repr():
    hapticSample = HapticSample(1.0, 0.3)
    assert repr(hapticSample) == 'HapticSample(1.0, 0.3)'

def test_eq():
    hapticSample1 = HapticSample(1.0, 0.3)
    hapticSample2 = HapticSample(1.0, 0.3)
    assert hapticSample1 == hapticSample2

def test_eq_different_haptic_value():
    hapticSample1 = HapticSample(1.0, 0.3)
    hapticSample2 = HapticSample(1.0, 0.5)
    assert hapticSample1 != hapticSample2

def test_eq_different_time_stamp():
    hapticSample1 = HapticSample(1.0, 0.5)
    hapticSample2 = HapticSample(1.4, 0.5)
    assert hapticSample1 != hapticSample2

def test_eq_error_non_HapticSample_object():
    hapticSample1 = HapticSample(1.0, 0.3)
    hapticSample2 = 1.0
    assert hapticSample1 != hapticSample2

def test_hash():
    hapticSample1 = HapticSample(1.0, 0.3)
    hapticSample2 = HapticSample(1.0, 0.3)
    assert hash(hapticSample1) == hash(hapticSample2)

def test_hash_error():
    hapticSample1 = HapticSample(1.0, 0.3)
    hapticSample2 = HapticSample(1.0, 0.5)
    assert hash(hapticSample1) != hash(hapticSample2)

def test_hash_error_non_HapticSample_object():
    hapticSample1 = HapticSample(1.0, 0.3)
    hapticSample2 = 1.0
    assert hash(hapticSample1) != hash(hapticSample2)

def test_haptic_sample_dict():
    sample = HapticSample(0.5, 0.7)
    expected_dict = {'time_stamp': 0.5, 'haptic_value': 0.7}
    assert sample.__dict__() == expected_dict