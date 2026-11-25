import numpy as np
import pygame
import random
import math
import soundService


shootSound = soundService.createTone(700, 0.1, 0.25)


def playSound(which):
    which.play()