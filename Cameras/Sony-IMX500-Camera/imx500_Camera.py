import os
import time
from PIL import Image
from picamera2 import Picamera2

class IMX500Camera:
    def __init__(self, image_path="captured_images/"):
        """
        Initialize the IMX500 AI Camera.
        :param image_path: Directory where images will be saved.
        """
        if not isinstance(image_path, str):
            raise ValueError("image_path must be a string.")
        
        self.image_path = image_path
        os.makedirs(image_path, exist_ok=True)  # Ensure directory exists

        # Create and configure camera
        self.picam2 = Picamera2()
        self.picam2.configure(self.picam2.create_still_configuration(
            main={"format": 'RGB888', "size": (2028, 1520)}))
        self.picam2.start()

    def capture_image(self, filename="object.jpg"):
        """
        Capture an image and save it.
        :param filename: Name of the image file.
        :return: Full path to the saved image.
        """
        if not isinstance(filename, str):
            raise ValueError("filename must be a string.")
        
        filepath = os.path.join(self.image_path, filename)
        self.picam2.capture_file(filepath)
        return filepath
    
    def capture_image_no_file(self) -> Image.Image:
        """
        Captures an image and returns it as a PIL.Image.Image object.
        """
        return self.picam2.capture_image()

    def cleanup(self):
        """
        Cleanup operations.
        """
        self.picam2.stop()


if __name__ == "__main__":
    cam = IMX500Camera()

    try:
        img_path = cam.capture_image("test_object.jpg")
        print(f"Image saved: {img_path}")
    finally:
        cam.cleanup()
