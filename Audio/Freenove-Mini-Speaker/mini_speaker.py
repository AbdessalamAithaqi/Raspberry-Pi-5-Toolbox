from gpiozero import PWMOutputDevice
from time import sleep


class Speaker:
    def __init__(self, pin):
        """
        Initialize the Speaker instance with the specified GPIO pin.
        :param pin: GPIO pin number to which the speaker is connected.
        """
        self.speaker = PWMOutputDevice(pin)
        self.default_volume = 0.5  # Default 50% duty cycle for sound

    def play_tone(self, frequency, duration):
        """
        Play a single tone on the speaker.
        :param frequency: Frequency of the tone in Hz.
        :param duration: Duration to play the tone in seconds.
        """
        print(f"Playing tone: {frequency} Hz for {duration} seconds")
        self.speaker.frequency = frequency
        self.speaker.value = self.default_volume  # Set volume
        sleep(duration)
        self.speaker.off()  # Turn off the speaker after the tone

    def play_melody(self, melody):
        """
        Play a sequence of tones (a melody).
        :param melody: List of tuples [(frequency, duration), ...]
        """
        print("Playing melody...")
        for frequency, duration in melody:
            self.play_tone(frequency, duration)

    def set_volume(self, volume):
        """
        Adjust the speaker volume.
        :param volume: Duty cycle value (0.0 to 1.0).
        """
        if 0.0 <= volume <= 1.0:
            self.default_volume = volume
            print(f"Volume set to {volume * 100}%")
        else:
            print("Volume must be between 0.0 and 1.0")

    def cleanup(self):
        """
        Clean up the speaker resources.
        """
        print("Cleaning up speaker...")
        self.speaker.off()

if __name__ == "__main__":
    # Initialize the speaker on GPIO 23
    speaker = Speaker(pin=23)

    try:
        # Play a single tone
        speaker.play_tone(440, 1)  # A4 for 1 second

        # Play a melody
        melody = [
            (440, 0.5),  # A4
            (494, 0.5),  # B4
            (523, 0.5),  # C5
            (440, 0.5),  # A4
        ]
        speaker.play_melody(melody)

        # Adjust the volume
        speaker.set_volume(0.3)  # Lower volume to 30%
        speaker.play_tone(440, 1)

    finally:
        # Clean up the GPIO
        speaker.cleanup()
