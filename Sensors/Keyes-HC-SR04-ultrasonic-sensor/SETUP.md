# Pin layout
Connect the ultrasonic sensor as follows:
1. Plug a cable from GND to a GND pin
2. Plug a cable from VCC to a 5V pin
3. Plug a cable from TRIG to a GPIO pin (default: GPIO23)
4. Plug a cable from ECHO to a GPIO pin (default: GPIO24)

# Libraries
To use the ultrasonic sensor module, install the required lgpio library:
```bash
pip install lgpio
```
# Code
1. Ensure GPIO access is enabled on your Raspberry Pi.
    ```bash
    sudo apt install lg
    ```

2. Run the example script to test the sensor:
    ```bash
    python ultrasonic_module.py
    ```
    The script will continuously measure distances and print them to the console.

3. Modify the script to change the GPIO pins or trigger distance:
    ```python
    sensor = UltrasonicSensor(trig_pin=23, echo_pin=24, trigger_distance=10)
    ```
4. To stop the script, use CTRL + C and clean up GPIO resources:
    ```python
    sensor.cleanup()
    ```
