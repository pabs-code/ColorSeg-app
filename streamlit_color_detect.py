import cv2
import numpy as np
import streamlit as st

# --- Constants ---
DEFAULT_LOWER_RED = np.array([0, 100, 80])
DEFAULT_UPPER_RED = np.array([10, 256, 256])
DEFAULT_LOWER_GREEN = np.array([35, 100, 80])
DEFAULT_UPPER_GREEN = np.array([85, 256, 256])
DEFAULT_LOWER_BLUE = np.array([100, 100, 80])
DEFAULT_UPPER_BLUE = np.array([145, 256, 256])


# --- Color Detection Function ---
def detect_color(image, lower_bound, upper_bound):
    """
    Detects and segments a specific color range from an image using OpenCV.

    Args:
        image (np.ndarray): The input image in BGR format.
        lower_bound (np.ndarray): Lower bound of the HSV color range.
        upper_bound (np.ndarray): Upper bound of the HSV color range.

    Returns:
        tuple: A tuple containing:
            - segmented_image (np.ndarray): The image with the detected color segmented.
            - mask (np.ndarray):  A binary mask indicating where the color is present.
    """
    # Convert the image from BGR to HSV color space
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Create a mask based on the provided HSV range
    mask = cv2.inRange(hsv_image, lower_bound, upper_bound)

    # Apply the mask to the original image to isolate the detected color
    segmented_image = cv2.bitwise_and(image, image, mask=mask)

    return segmented_image, mask


# --- Streamlit App ---
st.title("Color Detection App")

# File Uploader
uploaded_file = st.file_uploader("Choose an image (JPG, JPEG, PNG)", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Read the Image
    image = cv2.imdecode(np.frombuffer(uploaded_file.read(), np.uint8), 1)

    # Define Color Ranges (Can be adjusted for different color detection needs)
    color_ranges = {
        "Red": (DEFAULT_LOWER_RED, DEFAULT_UPPER_RED),
        "Green": (DEFAULT_LOWER_GREEN, DEFAULT_UPPER_GREEN),
        "Blue": (DEFAULT_LOWER_BLUE, DEFAULT_UPPER_BLUE)
    }

    # Detect and Segment Colors
    segmented_images = {}
    masks = {}
    for color, (lower, upper) in color_ranges.items():
        segmented_image, mask = detect_color(image, lower, upper)
        segmented_images[color] = segmented_image
        masks[color] = mask

    # Display Results
    st.subheader("Color Detection Results")

    st.image(cv2.cvtColor(image, cv2.COLOR_BGR2RGB), caption="Original Image", use_container_width=True)

    for color in segmented_images:
        st.image(segmented_images[color], caption=f"{color} Segmented Image", use_container_width=True)
