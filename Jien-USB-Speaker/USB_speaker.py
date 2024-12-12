import pygame
import numpy as np

class Speaker:
    def __init__(self):
        """
        Initialize the Speaker instance.
        """
        pygame.mixer.init()
        self.channel = pygame.mixer.Channel(1)
        self.volume = 1.0

    def play(self, filename: str):
        """
        Play the sound file.
        :param sound: The pygame.mixer.Sound object.
        """
        sound = self._make_sound(filename, self.volume)
        self.channel.play(sound)
        while self.channel.get_busy():
            self.channel.queue(sound)

    def set_volume(self, volume: float):
        """
        Set the volume of the speaker.
        :param volume: The volume of the speaker.
        """
        self.volume = volume

    def _make_sound(self, filename: str, factor: float)->pygame.mixer.Sound: 
        """
        Make a sound object from the file and amplify it by the factor.

        :param filename: The filename of the sound file.
        :param factor: The factor to amplify the sound by.
        """
        sound = pygame.mixer.Sound(filename)
        samples = pygame.sndarray.array(sound)
        amplified_samples = np.clip(samples * factor, -32768, 32767).astype(np.int16)
        amplified_sound = pygame.sndarray.make_sound(amplified_samples)
        return amplified_sound

if __name__ == "__main__":
    speaker = Speaker()
    speaker.set_volume(5.0)
    speaker.play('/usr/share/sounds/alsa/Front_Center.wav')