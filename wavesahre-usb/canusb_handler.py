import can
from time import sleep
import signal
import sys


class CANHandler:
    def __init__(self, channel, interface="slcan"):
        """
        Initialize the CAN handler for a Serial Line CAN (slcan) interface

        Args:
            channel (str): The device path (e.g., '/dev/ttyUSB0'.
            interface (str): The CAN interface to use (e.g., "socketcan", "slcan").
        """
        self.interface = interface
        self.channel = channel
        self.bus = None

    def connect(self):
        """
        Connect to the CAN bus.
        """
        try:
            self.bus = can.interface.Bus(bustype=self.interface, channel=self.channel   )
            print(
                f"Connected to CAN bus on channel {self.channel} with {self.interface}"
            )
        except Exception as e:
            print(f"Failed to connect to CAN bus: {e}")
            raise
    
    def disconnect(self):
        """
        Disconnect from the CAN bus.
        """
        if self.bus:
            try:
                self.bus.shutdown()
                print("Disconnected from CAN bus.")
            except Exception as e:
                print(f"Failed to disconnect from CAN bus: {e}")

    def send_message(self, arbitration_id, data):
        """
        Send a message over the CAN bus.

        Args:
            arbitration_id (int): The message's arbitration ID.
            data (list of int): The data payload (1-8 bytes).
        """
        if not self.bus:
            print("CAN bus is not connected. Call connect() first.")
            return False

        try:
            message = can.Message(
                arbitration_id=arbitration_id, data=data, is_extended_id=False
            )
            self.bus.send(message)
            print(f"Sent message with ID {arbitration_id} and data {data}")
            return True
        except Exception as e:
            print(f"Failed to send message: {e}")
            return False

    def listen(self,timeout=1.0):
        """
        Listen for CAN messages.

        Args:
            timeout (float): Timeout in seconds to wait for a message
        """
        try:
            while True:
                message= self.bus.recv(timeout=timeout)
                if message:
                    print(f"Received: ID={hex(message.arbitration_id)}, Data={list(message.data)}")
                else:
                    print("No message received within the timeout period")
        except KeyboardInterrupt:
            print("\nListening interrupted by user.")
        except Exception as e:
            print(f"Error while listening for messages: {e}")

if __name__ == "__main__":
    def signal_handler(sig,frame):
        print("\nExiting gracefully")
        can_handler.disconnect()
        sys.exit(0)

    signal.signal(signal.SIGINT, signal_handler)

    can_handler = CANHandler(channel="/dev/ttyUSB4", interface="slcan")

    try:
        can_handler.connect()
        print("Listening for incoming CAN messages ...")
        can_handler.listen()
    except Exception as e:
        print(f"Fatal error: {e}")
    finally:
        can_handler.disconnect()