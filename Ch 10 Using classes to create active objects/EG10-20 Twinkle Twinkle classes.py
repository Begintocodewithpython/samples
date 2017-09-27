# EG10-20 Twinkle Twinkle classes

import time
import snaps

class Note:
    def __init__(self, note, duration):
        self.__note = note
        self.__duration = duration

    def play(self):
        snaps.play_note(self.__note)
        time.sleep(self.__duration)

tune = [Note(note=0, duration=0.4), Note(note=0, duration=0.4),
        Note(note=7, duration=0.4), Note(note=7, duration=0.4),
        Note(note=9, duration=0.4), Note(note=9, duration=0.4),
        Note(note=7, duration=0.8), Note(note=5, duration=0.4),
        Note(note=5, duration=0.4), Note(note=4, duration=0.4),
        Note(note=4, duration=0.4), Note(note=2, duration=0.4),
        Note(note=2, duration=0.4), Note(note=0, duration=0.8)]

for note in tune:
    note.play()
