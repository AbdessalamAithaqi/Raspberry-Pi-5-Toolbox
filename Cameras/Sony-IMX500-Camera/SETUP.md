1. Install camera driver
    ```bash
    sudo apt install imx500-all
    ```

2. Reboot
    ```bash
    sudo reboot
    ```

3. Run a test that runs indefinetly on a premade trained model
    ```bash
    rpicam-hello -t 0s --post-process-file /usr/share/rpi-camera-assets/imx500_mobilenet_ssd.json --viewfinder-width 1920 --viewfinder-height 1080 --framerate 30
    ```