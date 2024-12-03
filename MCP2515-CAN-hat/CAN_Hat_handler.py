import can
from time import sleep
import signal
import sys


class CANHandler:
    def __init__(self, channel, bitrate=500000):
        """
        Initialize the CAN handler for a SocketCAN interface.
        
        :param channel: The CAN interface (e.g., 'can0')
        :param bitrate: The bitrate of the CAN bus (default: 500000)
        """
        self.channel = channel
        self.bitrate = bitrate
        self.bus = None

    def setup(self):
        """
        Set up the CAN bus interface.
        """
        try:
            self.bus = can.Bus(interface="socketcan", channel=self.channel, bitrate=self.bitrate)
            print(f"Initialized CAN bus on {self.channel} with bitrate {self.bitrate}")
        except OSError as e:
            print(f"Error initializing CAN bus on {self.channel}: {e}")
            raise

    def cleanup(self):
        """
        Properly clean up and shut down the CAN interface.
        """
        if self.bus is not None:
            self.bus.shutdown()
            print(f"Cleaned up CAN bus on {self.channel}")

    def send_message(self, arbitration_id, data):
        """
        Send a CAN message.

        :param arbitration_id: The CAN message ID
        :param data: A list of data bytes (max 8 bytes)
        """
        if self.bus is None:
            print("CAN bus is not initialized. Call setup() first.")
            return

        message = can.Message(
            arbitration_id=arbitration_id,
            data=data,
            is_extended_id=False
        )

        try:
            # Send the message
            self.bus.send(message)
            print(f"Message sent: ID={hex(arbitration_id)}, data={data}")
        except can.CanError as e:
            print(f"Failed to send message: {e}")


if __name__ == "__main__":
    def signal_handler(sig, frame):
        """
        Signal handler to clean up resources on script termination.
        """
        print("\nExiting gracefully...")
        can_handler.cleanup()
        sys.exit(0)

    signal.signal(signal.SIGINT, signal_handler)

    can_handler = CANHandler(channel="can0")
    try:
        can_handler.setup()

        # Define a list of messages to send
        messages = [
            {"id": 0x123, "data": [0x01, 0x02, 0x03]},
            {"id": 0x124, "data": [0x04, 0x05, 0x06]},
            {"id": 0x125, "data": [0x07, 0x08, 0x09]},
            {"id": 0x126, "data": [0x0A, 0x0B, 0x0C]},
        ]

        # Loop through messages continuously
        while True:
            for message in messages:
                can_handler.send_message(arbitration_id=message["id"], data=message["data"])
                sleep(1)  # Wait 1 second between messages

    except Exception as e:
        print(f"Fatal error: {e}")
    finally:
        can_handler.cleanup()
