import can
from time import sleep
import signal
import sys

class CANHandler:
    def __init__(self,channel, bitrate=500000):
        """
        Initialize the CAN handler for a SocketCAN interface
        
        :param channel: The CAN interface(e.g., 'can0')
        :param bitrate: The bitrate of the CAN bus (default:500000)
        """
        self.channel = channel
        self.bitrate = bitrate
        self.bus = None

    def setup(self):
        """
        Set up the CAN bus interface
        """
        try:
            self.bus = can.Bus(interface="socketcan", channel=self.channel, bitrate=self.bitrate)
            print(f"Initialized CAN bus on {self.channel} with bitrate {self.bitrate}")
        except OSError as e:
            print(f"Error initializing CAN bus on {self.channel}:{e}")
            raise
    
    def cleanup(self):
        """
        Properly clean up and shut down the CAN interface
        """
        if self.bus is not None:
            self.bus.shutdown()
            print(f"Cleaned up CAN bus on {self.channel}")

    def send_message(self, arbitration_id, data, ):
        """
        Send CAN messages

        :param arbitration_id: The CAN message ID
        :param data: A list of data bytes (max 8bytes)
        """
        if self.bus is None:
            print("CAN bus is not initialized. Call setup() first.")
            return
        
        
        message = can.Message(
            arbitration_id= arbitration_id,
            data=data,
            is_extended_id=False
        )

        try:
            # Send the message
            self.bus.send(message)
            print(f"Message sent: ID={arbitration_id}, data={data}")
            
        except can.CanError as e:
            print(f"Failed to send message: {e}")

    def receive_message(self, timeout=1.0):
        """
        Receive a CAN message.

        :param timeout: Timeout in seconds for receiving a message
        :return: The received CAN message or None if no message is recived
        """
        if self.bus is None:
            print("CAN bus is not initialized. Call setup() first.")
            return None
        
        try:
            message=self.bus.recv(timeout)
            if message:
                print(f"message received: ID={hex(message.arbitration_id)}, data={list(message.data)}")
                return message
        except Exception as e:
            print(f"Error receiveing message: {e}")
            return None


if __name__ == "__main__":
    def signal_handler(sig, frame):
        """
        Signal handler to clean up resources on script termination
        """
        print("\nExiting gracefully...")
        can_handler.cleanup()
        sys.exit(0)

    signal.signal(signal.SIGINT, signal_handler)

    can_handler = CANHandler(channel="can0")
    try:
        can_handler.setup()

        while True:
            can_handler.send_message(arbitration_id=0x123, data=[0x01,0x02,0x03])
            sleep(2)

    except Exception as e:
        print(f"Fatal error:{e}")
    finally:
        can_handler.cleanup()