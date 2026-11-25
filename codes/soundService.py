import numpy as np
import pygame


if not pygame.mixer.get_init():
    pygame.mixer.init(
        frequency=22050,
        size=-16,
        channels=1
    )

def createTone(frequency, duration, volume=0.5, waveform="square", endFrequency=None):

    mixerInfo = pygame.mixer.get_init()

    if mixerInfo is None:
        raise RuntimeError("Mixer not initialized!")

    if duration <= 0:
        raise ValueError("Duration must be greater than 0!")

    sampleRate = mixerInfo[0]
    channels = mixerInfo[2]

    samples = int(sampleRate * duration)

    if samples < 2:
        raise ValueError("Duration is too short!")

    t = np.arange(samples) / sampleRate

    if endFrequency is None:
        endFrequency = frequency

    frequencyChange = endFrequency - frequency

    phase = 2 * np.pi * (
        frequency * t +
        frequencyChange * (t ** 2) / (2 * duration)
    )

    if waveform == "square":
        sound = np.where(np.sin(phase) >= 0, 1, -1)

    elif waveform == "pulse":
        sound = np.where((phase % (2 * np.pi)) < np.pi * 0.5, 1, -1)

    elif waveform == "triangle":
        sound = (2 / np.pi) * np.arcsin(np.sin(phase))

    elif waveform == "sawtooth":
        sound = 2 * ((phase / (2 * np.pi)) % 1) - 1

    elif waveform == "sine":
        sound = np.sin(phase)

    elif waveform == "noise":
        sound = np.random.uniform(-1, 1, samples)

    else:
        raise ValueError("Unknown waveform!")

    volume = np.clip(volume, 0, 1)

    envelope = np.ones(samples)

    fadeLength = min(int(sampleRate * 0.005), samples // 2)

    if fadeLength > 1:
        envelope[:fadeLength] = np.linspace(0, 1, fadeLength)
        envelope[-fadeLength:] = np.linspace(1, 0, fadeLength)

    audio = (sound * envelope * volume * 32767).astype(np.int16)

    if channels == 2:
        audio = np.column_stack((audio, audio))

    return pygame.sndarray.make_sound(audio)


def createSequence(notes, volume=0.5, waveform="square"):

    audioParts = []

    for note in notes:
        frequency = note[0]
        duration = note[1]
        endFrequency = note[2] if len(note) > 2 else None

        sound = createTone(frequency, duration, volume, waveform, endFrequency)

        audioParts.append(pygame.sndarray.array(sound))

    audio = np.concatenate(audioParts, axis=0)

    return pygame.sndarray.make_sound(audio)