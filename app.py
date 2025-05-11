import cv2
import numpy as np
import streamlit as st


class ColorDetector:
    """
    A class to detect and segment specific colors in an image using HSV color space.

    Attributes:
        lower_bounds (dict): Dictionary of lower bounds for different colors.
        upper_bounds (dict): Dictionary of upper bounds for different colors.
    """

    def __init__(self):
        """
        Initialize the color detector with predefined HSV bounds for red, green, and blue.
        """
        self.lower_bounds = {
            "Red": np.array([0, 100, 80]),
            "Green": np.array([35, 100, 80]),
            "Blue": np.array([100, 100, 80])
        }
        self.upper_bounds = {
            "Red": np.array([10, 256, 256]),
            "Green": np.array([85, 256, 256]),
            "Blue": np.array([145, 256, 256])
        }

    def detect_color(self, image, lower_bound=None, upper_bound=None):
        """
        Detects and segments a specific color range from an image using OpenCV.

        Args:
            image (np.ndarray): The input image in BGR format.
            lower_bound (np.ndarray, optional): Lower bound of the HSV color range. Defaults to predefined.
            upper_bound (np.ndarray, optional): Upper bound of the HSV color range. Defaults to predefined.

        Returns:
            tuple: A tuple containing:
                - segmented_image (np.ndarray): The image with the detected color segmented.
                - mask (np.ndarray): A binary mask indicating where the color is present.
        """
        if lower_bound is None:
            lower_bound = self.lower_bounds["Red"]  # Default to red
        if upper_bound is None:
            upper_bound = self.upper_bounds["Red"]  # Default to red

        hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv_image, lower_bound, upper_bound)
        segmented_image = cv2.bitwise_and(image, image, mask=mask)

        return segmented_image, mask


class ColorSegmentationApp:
    """
    A Streamlit app for detecting and displaying color segments in an uploaded image.
    """

    def __init__(self):
        """
        Initialize the Streamlit app with a title and file uploader.
        """
        self.title = "Color Segmenter App"
        self.file_uploader_label = "Choose an image (JPG, JPEG, PNG)"
        self.supported_types = ["jpg", "jpeg", "png"]
        self.color_detector = ColorDetector()

    def run(self):
        """
        Run the Streamlit app.
        """
        st.title(self.title)
        uploaded_file = st.file_uploader(
            self.file_uploader_label, type=self.supported_types)

        if uploaded_file is not None:
            image = self._read_image(uploaded_file)
            color_ranges = {
                "Red": (self.color_detector.lower_bounds["Red"], self.color_detector.upper_bounds["Red"]),
                "Green": (self.color_detector.lower_bounds["Green"], self.color_detector.upper_bounds["Green"]),
                "Blue": (self.color_detector.lower_bounds["Blue"], self.color_detector.upper_bounds["Blue"])
            }

            segmented_images = {}
            masks = {}

            for color, (lower, upper) in color_ranges.items():
                segmented_image, mask = self.color_detector.detect_color(
                    image=image, lower_bound=lower, upper_bound=upper)
                segmented_images[color] = segmented_image
                masks[color] = mask

            self._display_results(
                image=image, segmented_images=segmented_images)

    def _read_image(self, uploaded_file):
        """
        Read the uploaded image using OpenCV.

        Args:
            uploaded_file (UploadedFile): The file object from Streamlit's file uploader.

        Returns:
            np.ndarray: The image in BGR format.
        """
        bytes_data = uploaded_file.read()
        np_array = np.frombuffer(bytes_data, dtype=np.uint8)
        image = cv2.imdecode(np_array, 1)  # 1 means color image
        return image

    def _display_results(self, image, segmented_images):
        """
        Display the original and segmented images.

        Args:
            image (np.ndarray): The original image.
            segmented_images (dict): Dictionary of segmented images by color.
        """
        st.subheader("Color Detection Results")
        st.image(cv2.cvtColor(image, cv2.COLOR_BGR2RGB),
                 caption="Original Image", use_container_width=True)

        for color in segmented_images:
            st.image(
                segmented_images[color], caption=f"{color} Segmented Image", use_container_width=True)


if __name__ == "__main__":
    app = ColorSegmentationApp()
    app.run()
