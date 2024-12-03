import serial
from utils.custom_logger import get_logger

LOGGER = get_logger(__name__)


class RS485Handler:
    def __init__(self, port, baudrate=9600, timeout=1):
        """
        Initialize the RS485Handler instance.

        Args:
            port (str): The serial port to use (e.g., "COM3" on Windows or "/dev/ttyUSB0" on Linux).
            baudrate (int): The baud rate for RS485 communication.
            timeout (int): Timeout in seconds for read operations.
        """
        self.port = port
        self.baudrate = baudrate
        self.timeout = timeout
        self.serial_connection = None

    def connect(self):
        """
        Establish a connection to the RS485 bus.
        """
        try:
            self.serial_connection = serial.Serial(
                port=self.port,
                baudrate=self.baudrate,
                timeout=self.timeout,
                parity=serial.PARITY_NONE,
                stopbits=serial.STOPBITS_ONE,
                bytesize=serial.EIGHTBITS,
            )
            LOGGER.info(
                f"Connected to RS485 bus on port {self.port} at {self.baudrate} baud."
            )
        except Exception as e:
            LOGGER.error(f"Failed to connect to RS485 bus: {e}")
            self.serial_connection = None

    def disconnect(self):
        """
        Close the connection to the RS485 bus.
        """
        if self.serial_connection:
            try:
                self.serial_connection.close()
                LOGGER.info("Disconnected from RS485 bus.")
            except Exception as e:
                LOGGER.error(f"Failed to disconnect from RS485 bus: {e}")

    def send_message(self, message):
        """
        Send a message over the RS485 bus.

        Args:
            message (str or bytes): The message to send.
        """
        if not self.serial_connection:
            LOGGER.warning("RS485 bus is not connected. Call connect() first.")
            return False

        try:
            if isinstance(message, str):
                message = message.encode()  # Convert string to bytes
            self.serial_connection.write(message)
            LOGGER.info(f"Sent message: {message}")
            return True
        except Exception as e:
            LOGGER.error(f"Failed to send message: {e}")
            return False

    def receive_message(self):
        """
        Receive a message from the RS485 bus.

        Returns:
            str: The received message as a string.
        """
        if not self.serial_connection:
            LOGGER.warning("RS485 bus is not connected. Call connect() first.")
            return None

        try:
            response = self.serial_connection.read(100)  # Read up to 100 bytes
            message = response.decode("utf-8").strip()
            LOGGER.info(f"Received message: {message}")
            return message
        except Exception as e:
            LOGGER.error(f"Failed to receive message: {e}")
            return None

    def flush_buffers(self):
        """
        Flush the input and output buffers.
        """
        if not self.serial_connection:
            LOGGER.warning("RS485 bus is not connected. Call connect() first.")
            return

        try:
            self.serial_connection.reset_input_buffer()
            self.serial_connection.reset_output_buffer()
            LOGGER.info("Flushed RS485 input and output buffers.")
        except Exception as e:
            LOGGER.error(f"Failed to flush buffers: {e}")
