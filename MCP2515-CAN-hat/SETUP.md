Follow these steps to be able to send and receive CAN message via the MCP2515 hat.
1. Enable SPI on Raspberry Pi
    - The MCP2515 communicates via SPI, so we need to enable SPI
    ```bash
    sudo nano /boot/Firmware/config.txt
    ```
    - Add these lines
    ```
    dtoverlay=mcp2515-can0,oscillatore=16000000,interrupt=25
    dtoverlay=spi0-hw-cs
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
