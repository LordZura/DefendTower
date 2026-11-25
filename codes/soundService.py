import numpy as np
import pygame
import random
import math

pygame.mixer.init(
    frequency=22050,
    size=16,
    channels=1
)

def createTone(frequency, duration, volume = 0.5):
    samples = int(22050 * duration)
    t = np.arange(samples) / 22050
    sound = np.sign(np.sin(2 * np.pi * frequency * t))
    audio = (sound * volume * 32767).astype(np.int16)
    return pygame.sndarray.make_sound(audio)