from time import sleep
from RPLCD.i2c import CharLCD


class LCDDisplay:
    def __init__(self, address=0x27, bus_type='PCF8574', columns=16, rows=2):
        self.lcd = CharLCD(bus_type, address, cols=columns, rows=rows)
        self.columns = columns
        self.rows = rows
        print(f"LCD initialized at address {hex(address)}")

    def display_message(self, message):
        """
        Display a message on the LCD, formatted for a 16x2 screen.
        :param message: Text to display. Use \n for manual line breaks.
        """
        # Split the message into lines
        lines = message.split("\n")

        # Warn if the message is too long
        if len(lines) > self.rows or any(len(line) > self.columns for line in lines):
            print("WARNING: Message too long to display fully. Some parts will be truncated.")

        # Format each line to fit the display width
        formatted_lines = []
        for line in lines:
            # Truncate or pad the line to fit within the display width
            formatted_lines.append(line[:self.columns].ljust(self.columns))

        # Combine the formatted lines into a single string
        formatted_message = "".join(formatted_lines[:self.rows])

        print(f"Displaying formatted message:\n{formatted_message}")
        self.lcd.write_string(formatted_message)

    def clear(self):
        """
        Clear the LCD screen.
        """
        print("Clearing LCD screen")
        self.lcd.clear()

    def display_timed_message(self, message, duration=5):
        """
        Display a message on the LCD for a specific duration, then clear it.
        :param message: Text to display on the LCD.
        :param duration: Time (in seconds) to display the message (default is 5).
        """
        self.display_message(message)
        sleep(duration)
        self.clear()


if __name__ == "__main__":
    # Initialize the LCD
    lcd = LCDDisplay(address=0x27)

    try:
        # Display a message that fits neatly on the screen
        lcd.display_timed_message("I2C Address 0x27\nHello, World!", 5)

        # Display a longer message with proper formatting
        lcd.display_timed_message("This is a long message that exceeds the capacity\nof a 16x2 display!", 5)

    except Exception as e:
        print(f"Error: {e}")
 
