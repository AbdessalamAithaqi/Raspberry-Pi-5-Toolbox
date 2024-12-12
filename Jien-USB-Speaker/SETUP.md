1. Plug in the USB speaker and identify its name 
    ```sh
    lsusb
    ```

2. identify the card number of the usb device
    ```sh
    aplay -l
    ```

3. Edit or create the asoundrc file to set that device as default audio
    ```sh
    nano ~/.asoundrc
    ```

    ```
    defaults.pcm.card <card number here>
    defaults.ctl.card <card number here>
    ```