import numpy as np

import hand_tracker


def getCordinate(inputImage):
    hoge, landmarks = hand_tracker.HandTracker(1,1,1).draw(inputImage)

    return landmarks

