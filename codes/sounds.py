import numpy as np
import pygame
import random
import math
import soundService


shootSound = soundService.createTone(700, 0.1, 0.25)
hitSound = soundService.createTone(100, 0.1, 0.25)
killSound = soundService.createTone(50, 0.2, 0.3)


def playSound(which):
    which.play()