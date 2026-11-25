import soundService


shootSound = soundService.createTone(900, 0.07, 0.18, "square", 350)
hitSound = soundService.createTone(180, 0.06, 0.25, "noise")
killSound = soundService.createTone(650, 0.18, 0.22, "triangle", 120)

purchaseFailed = soundService.createSequence([
    (420, 0.09, 300),
    (260, 0.16, 150)
], 0.22, "square")


def playSound(which):
    which.play()