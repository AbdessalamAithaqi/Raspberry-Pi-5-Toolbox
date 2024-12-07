from gpiozero import PWMOutputDevice
from time import sleep

# Define the left and right audio pins
LEFT_SPEAKER_PIN = 23  # GPIO23 (Pin 16)
RIGHT_SPEAKER_PIN = 24  # GPIO24 (Pin 18)

# Initialize the PWM output devices
left_channel = PWMOutputDevice(LEFT_SPEAKER_PIN)
right_channel = PWMOutputDevice(RIGHT_SPEAKER_PIN)

def play_tone(channel:PWMOutputDevice, frequency, duration, volume=0.5):
    """
    Play a tone on a specific channel.
    :param channel: PWMOutputDevice instance (left or right).
    :param frequency: Frequency of the tone in Hz.
    :param duration: Duration of the tone in seconds.
    :param volume: Volume (0.0 to 1.0).
    """
    print(f"Playing tone on channel {channel.pin}: {frequency} Hz for {duration} seconds")
    channel.frequency = frequency
    channel.value = volume  # Set volume (duty cycle)
    sleep(duration)
    channel.off()  # Stop the tone

try:
    # Play a tone on the left channel
    play_tone(left_channel, 440, 1)  # A4 note for 1 second

    # Play a tone on the right channel
    play_tone(right_channel, 523, 1)  # C5 note for 1 second

    # Play a stereo effect (alternating left and right)
    for _ in range(3):
        play_tone(left_channel, 440, 0.5)
        play_tone(right_channel, 523, 0.5)

finally:
    # Clean up GPIO resources
    left_channel.off()
    right_channel.off()
    print("Audio test complete. Cleaning up...")
