import time
import lgpio

class UltrasonicSensor:
    def __init__(self, trig_pin, echo_pin, trigger_distance=15, callback=None):
        """
        Initializes the ultrasonic sensor.
        :param trig_pin: GPIO pin for the trigger signal.
        :param echo_pin: GPIO pin for receiving the echo signal.
        :param trigger_distance: Distance (in cm) at which to trigger a response.
        :param callback: Function to call when an object is detected.
        """
        if not isinstance(trig_pin, int) or not isinstance(echo_pin, int):
            raise ValueError("GPIO pins must be integers.")
        
        self.trig_pin = trig_pin
        self.echo_pin = echo_pin
        self.trigger_distance = trigger_distance
        self.callback = callback

        # Initialize GPIO chip
        self.chip = lgpio.gpiochip_open(0)

        # Setup GPIO
        lgpio.gpio_claim_output(self.chip, self.trig_pin)  # Trig as OUTPUT
        lgpio.gpio_claim_input(self.chip, self.echo_pin)   # Echo as INPUT

    def get_distance(self):
        """
        Measures the distance to the nearest object using the ultrasonic sensor.
        :return: Distance in cm.
        """
        # Send trigger pulse
        lgpio.gpio_write(self.chip, self.trig_pin, 1)
        time.sleep(0.00001)  # 10µs pulse
        lgpio.gpio_write(self.chip, self.trig_pin, 0)

        start_time = time.time()
        stop_time = time.time()

        # Wait for echo to start
        while lgpio.gpio_read(self.chip, self.echo_pin) == 0:
            start_time = time.time()

        # Wait for echo to stop
        while lgpio.gpio_read(self.chip, self.echo_pin) == 1:
            stop_time = time.time()

        # Calculate time difference
        elapsed_time = stop_time - start_time

        # Convert to distance (speed of sound is ~343m/s)
        distance = (elapsed_time * 34300) / 2  # Convert to cm

        return round(distance, 2)  # Return rounded distance

    def start_monitoring(self, check_interval=0.5):
        """
        Continuously monitors distance and triggers the callback when an object is detected.
        :param check_interval: Time (in seconds) between distance checks.
        """
        try:
            while True:
                distance = self.get_distance()
                if distance < self.trigger_distance and self.callback:
                    if self.callback(distance):
                        return
                time.sleep(check_interval)  # Wait before next measurement
        except KeyboardInterrupt:
            pass  # Allow clean exit

    def cleanup(self):
        """
        Cleans up GPIO resources.
        """
        lgpio.gpiochip_close(self.chip)


if __name__ == "__main__":
    def object_detected(distance):
        print(f"Object detected at {distance} cm!")

    sensor = UltrasonicSensor(trig_pin=23, echo_pin=24, trigger_distance=10, callback=object_detected)
    sensor.start_monitoring()
