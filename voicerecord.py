import sounddevice as sd
import numpy as np
import wavio as wv
import time
import os
from datetime import datetime
freq = 44100
duration = 20
print("Recording...")
recording = sd.rec(int(duration * freq), samplerate=freq, channels=2)
sd.wait()
print("Recording complete.")
wv.write("recording0.wav", recording, freq, sampwidth=2)
