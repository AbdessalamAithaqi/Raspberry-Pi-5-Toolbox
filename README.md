# Enable UART on Raspberry Pi
1. Open Raspberry Pi configuration tool:
```bash
sudo raspi-config
```

2. Activate Serial options
    Select `3 Interface Options Configure connections to peripherals`>`I6 Serial Port Enable/disable shell messages on the serial connection`
    When prompted with `Would you like a login shell to be accessible over serial?` select `No`
    When prompted with `Would you like the serial port hardware to be enabled?` select `Yes`
    Once you get the ` The serial login shell is disabled. The serial interface is enabled` select `Ok`
    Once back in the main menu select `Finish`
    When out of the menu reboot your machine
```bash
sudo reboot
```

3. Plug in the RS485/RS422 hat

4. Connect the serial cable where appropriate

5. Check the serial devices available
```bash
ls /dev/serial*
```
You should see 
```bash
/dev/serial0
/dev/serial1
```

6. Verify the Mappings
```bash
ls -l /dev/serial*
```
At the end of the lines you should see something like 
```bash
/dev/serial0 -> ttyAMA0
/dev/serial1 -> ttyS0
```
If that is what you see you can move on. If your mapping is different you will want to look into changing the mapping by disabling the bluetooth.
```bash
sudo nano /boot/firmware/config.txt
```
Modify the last lines to match
```
enable_uart=1
dtoverlay=disable-bt
```
Save with a `Ctrl+O`, `Enter` then `Ctrl+X` and reboot
