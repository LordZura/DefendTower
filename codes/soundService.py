
import numpy as np
import pygame


if not pygame.mixer.get_init():
    pygame.mixer.init(
        frequency=22050,
        size=-16,
        channels=1
    )

def createTone(frequency, duration, volume=0.5):

    mixerInfo = pygame.mixer.get_init()

    if mixerInfo is None:
        raise RuntimeError("Mixer not initialized!")

    sampleRate = mixerInfo[0]
    channels = mixerInfo[2]

    samples = int(sampleRate * duration)

    t = np.arange(samples) / sampleRate

    sound = np.sin(2 * np.pi * frequency * t)

    envelope = np.ones(samples)

    fadeLength = min(int(sampleRate * 0.01), samples // 2)

    envelope[:fadeLength] = np.linspace(0, 1, fadeLength)
    envelope[-fadeLength:] = np.linspace(1, 0, fadeLength)

    audio = (sound * envelope * volume * 32767).astype(np.int16)

    if channels == 2:
        audio = np.column_stack((audio, audio))

    return pygame.sndarray.make_sound(audio)