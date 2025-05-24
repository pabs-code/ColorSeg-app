# HSV Color Segmentation

> A Streamlit-based application for detecting and segmenting specific colors in images using HSV color space.

---

## Table of Contents

- [**Color Segmentation App**](#color-segmentation-app)
  - [Table of Contents](#table-of-contents)
  - [About the Project](#about-the-project)
  - [Features](#features)
  - [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Installation](#installation)
  - [Running Script](#running-script)
  - [Expectations When Running This App](#expectations-when-running-this-app)
  - [Demo](#demo)
  - [Acknowledgments](#acknowledgments)
  - [License](#license)

---

## About the Project

**Color Segmentation App** is a simple yet powerful Streamlit application that allows users to upload an image and detect segments of specific colors (Red, Green, Blue) using the **HSV color space**. The app is ideal for learning about image processing and OpenCV.

This project is designed to be **easy to use**, **educational**, and **extendable** for more advanced color detection or segmentation tasks.

---

## Features

- Upload images in JPG, JPEG, or PNG format.
- Detect and display segments of Red, Green, and Blue colors in the image.
- Visualize the original image alongside segmented color regions.
- Built with **Streamlit**, **OpenCV**, and **NumPy** for performance and clarity.

---

## Getting Started

### Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.8 or higher
- [Streamlit](https://streamlit.io/)
- [OpenCV (cv2)](https://pypi.org/project/opencv-python/)
- [NumPy](https://numpy.org/)

---

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-username/hsv-colorseg.git
   ```

2. **Navigate to the project directory:**

   ```bash
   cd hsv-colorseg
   ```

3. **Install the required dependencies:**

   ```bash

   pip install streamlit opencv-python numpy
   ```

---

## Running Script

1. Run the Streamlit app:

   ```bash
   streamlit run app.py
   ```

2. A new browser window will open with the Color Segmentation App.

3. Use the file uploader to select an image (JPG, JPEG, or PNG).

4. The app will display:
   - The original image.
   - Segmented images for Red, Green, and Blue.

---

## Expectations When Running This App

| Feature                     | Description                                                                 |
| --------------------------- | --------------------------------------------------------------------------- |
| **Image Upload**            | Users can upload images in JPG, JPEG, or PNG format.                        |
| **Color Detection**         | The app detects segments of Red, Green, and Blue using HSV color space.     |
| **Visualization**           | Segmented images are displayed alongside the original image for comparison. |
| **User-Friendly Interface** | Built with Streamlit, it provides a simple and interactive experience.      |

---

## Demo


https://github.com/user-attachments/assets/657113d9-62fb-46af-82e3-ab3f595e0268

---

## Acknowledgments

- [Streamlit](https://streamlit.io/) – for the web interface.
- [OpenCV (cv2)](https://pypi.org/project/opencv-python/) – for image processing.
- [NumPy](https://numpy.org/) – for numerical operations.

---

## License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

