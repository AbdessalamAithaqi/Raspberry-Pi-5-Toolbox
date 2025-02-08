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
1. Enable I2C on your Raspberry Pi
   ```sh
   sudo raspi-config
   ```
   - Navigate to `3 Interface Options > P5 I2C`
   - Reboot
     ```sh
     sudo reboot
     ```
	 
2. Find the `i2c` address
    ```bash
    sudo i2cdetect -y 1
    ```

3. Set the address at the one found in the previous step
