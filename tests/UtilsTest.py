# import sys
# import os
# sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# from utils.haptic_utils import *
# import pytest

# def test_get_time_stamp_indicies():
#     time_stamps = [0.5*x for x in range(1, 11)]
#     print(time_stamps)
#     sr = 4
#     expected = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
#     assert get_time_stamp_indicies(time_stamps, sr) == expected