import pytest
import sys
sys.path.append('..')
from Utils import generateTimeStampsArray

TOLERACE = 0.000001

def test_generateTimeStampsArray():
    expectedOutput = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
    assert generateTimeStampsArray(1, 10) == pytest.approx(expectedOutput, abs = TOLERACE)