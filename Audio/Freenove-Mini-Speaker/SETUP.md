# Pin layout
1.  Plug the black cable to any `GND` pin
2.  Pin the red cable on any `GPIO` pin

# Libraries
1. Install `gpiozero` a library that simplifies GPIO usage
    ```bash
    pip install gpiozero
    ```

2. Install `RPi.GPIO` a low-level Python library for controlling GPIO pins
    ```bash
    pip install RPi.GPIO
    ```

3. Install `lgpio` another low-level GPIO library
    ```bash
    pip install lgpio
    ```

4. Install `pigpio` daemon-based library for Raspberry Pi GPIO
    ```bash
    pip install pigpio
    ```

# Code
1. Find the `GPIO` pin number and set it in the code on initalisation (GPIO23 in this example)
    ```python
    speaker = Speaker(pin=23)
    ```