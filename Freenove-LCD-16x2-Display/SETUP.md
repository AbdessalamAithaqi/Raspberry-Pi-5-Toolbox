# Pin layout
Top to bottom
1.  Plug a cable from `GND` to a `GND` pin
2.  Plug a cable from `VDD` to a `5V` pin
3.  Plug a cable from `SDA` to a `I2C` pin
4.  Plug a cable from `SCL` to a `I2C` pin

# Libraries
1. Install `smbus2` a library for interfacing with I²C devices via the SMBus
    ```bash
    pip install smbus2 

    ```

2. Install `RPLCD` a library for controlling character LCDs
    ```bash
    pip install RPLCD
    ```

# Code
1. Find the `i2c` address
    ```bash
    sudo i2cdetect -y 1
    ```

2. Set the address at the one found in the previous step
    ```python