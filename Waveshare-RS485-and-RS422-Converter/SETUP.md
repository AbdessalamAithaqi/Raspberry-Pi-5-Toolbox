Follow these steps to be able to send and receive RS485/RS422 message via USB using the waveshare RS485/RS422-TO-USB

1. List usb devices
    ```bash
    lsusb
    ```

2. Plug in the USB and see which was added
    ```bash
    lsusb
    ```

3. Find device's `ttyUSB` the USB is mapped to
    ```bash
    sudo dmesg | grep tty
    ```

4. Go to the python code and use that `ttyUSB` as the channel