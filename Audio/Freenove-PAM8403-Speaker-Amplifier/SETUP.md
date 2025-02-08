# Pin layout
1. Plug a cable from `OUT L (+)` (Left Speaker Red) to the left speaker positive terminal.
2. Plug a cable from `OUT L (-)` (Left Speaker Black) to the left speaker negative terminal.
3. Plug a cable from `OUT R (+)` (Right Speaker Red) to the right speaker positive terminal.
4. Plug a cable from `OUT R (-)` (Right Speaker Black) to the right speaker negative terminal.
5. Plug a cable from `L (Audio In)` (GPIO 23, Pin 16) to the left audio PWM signal input.
6. Plug a cable from `G (Audio In)` (Pin 14) to the ground for the audio input.
7. Plug a cable from `R (Audio In)` (GPIO 24, Pin 18) to the right audio PWM signal input.
8. Plug a cable from `5V` (Pin 2) to the power supply's 5V pin.
9. Plug a cable from `GND` (Pin 9) to the ground pin for power.

# Libraries
1. Install `gpiozero` a library that simplifies GPIO usage
    ```bash
    pip install gpiozero
    ```