# EG10-21 Twinkle Twinkle printer

import time
import snaps

class Note:
    def __init__(self, note, duration):
        self.__note = note
        self.__duration = duration

    def play(self):
        snaps.play_note(self.__note)
        time.sleep(self.__duration)

def __str__(self):
    template = 'Note: {0} Duration: {1}'
    return template.format(self.__note, self.__duration)

tune = [Note(note=0, duration=0.4), Note(note=0, duration=0.4),
        Note(note=7, duration=0.4), Note(note=7, duration=0.4),
        Note(note=9, duration=0.4), Note(note=9, duration=0.4),
        Note(note=7, duration=0.8), Note(note=5, duration=0.4),
        Note(note=5, duration=0.4), Note(note=4, duration=0.4),
        Note(note=4, duration=0.4), Note(note=2, duration=0.4),
        Note(note=2, duration=0.4), Note(note=0, duration=0.8)]

for note in tune:
    note.play()

tune_strings = map(str,tune)
print('\n'.join(tune_strings))
