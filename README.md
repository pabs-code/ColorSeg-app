# Color Detection & Segmentation App

## Overview

This Streamlit app allows you to upload an image and automatically detect and segment different colors within it (Red, Green, and Blue). It uses OpenCV for image processing and color space conversion (HSV) to achieve accurate color detection.

## Key Features

*   **Image Upload:**  Upload images from your computer in JPG, JPEG, or PNG format.
*   **Color Detection:** Automatically detects the presence of Red, Green, and Blue colors within the uploaded image.
*   **Segmentation:** Segments the image to isolate the detected color regions.
*   **Visual Display:** Displays the original image alongside the segmented images for each detected color.

## How to Use

1.  Run the Streamlit app: `streamlit run streamlit_color_detect.py`
2.  The app will open in your web browser.
3.  Click the "Choose an image..." button to upload an image.
4.  The segmented images for Red, Green, and Blue will be displayed below the original image.

## Notes

*   **Color Range Adjustment:** The default color ranges (lower\_red, upper\_red, etc.) may need to be adjusted depending on the specific colors you want to detect in your images.
*   **HSV Color Space:**  The app uses the HSV color space because it's often more robust for color-based segmentation than RGB.

## Requirements

*   Python 3.7 or higher
*   OpenCV (cv2)
*   NumPy
*   Streamlit
