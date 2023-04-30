import pytest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from haptic_utils import *
TOLERACE = 0.000001

def test_generateTimeStampsArray():
    expectedOutput = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
    assert generateTimeStampsArray(1, 10) == pytest.approx(expectedOutput, abs = TOLERACE)