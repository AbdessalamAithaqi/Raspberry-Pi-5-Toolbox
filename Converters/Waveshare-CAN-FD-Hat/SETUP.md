Follow these steps to be able to send and receive CAN message via the MCP2515 hat.
1. Enable SPI on Raspberry Pi
    - The MCP2515 communicates via SPI, so we need to enable SPI
    ```bash
    sudo nano /boot/Firmware/config.txt
    ```
    - replace the lines of dtparam=spi and dtoverlay with these
    ```
    dtparam=spi=on
    dtoverlay=spi1-3cs
    dtoverlay=mcp251xfd,spi0-0,interrupt=25
    ```
    - Reboot the machine
    ```bash
    sudo reboot
    ```

2. Bring Up the CAN Interface and set the bitrate (500 kbps)
    ```bash
    sudo ip link set can0 up type can bitrate 500000
    ```

3. Install python-can library
    ```bash
    pip install python-can
    ```
