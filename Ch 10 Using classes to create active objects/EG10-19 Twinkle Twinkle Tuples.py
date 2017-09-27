# EG10-19 Twinkle Twinkle Tuples

import time
import snaps

tune = [(0, 0.4), (0, 0.4), (7, 0.4), (7, 0.4),
        (9, 0.4), (9, 0.4), (7, 0.8), (5, 0.4),
        (5, 0.4), (4, 0.4), (4, 0.4), (2, 0.4),
        (2, 0.4), (0, 0.8)]

for note in tune:
    snaps.play_note(note[0])
    time.sleep(note[1])
