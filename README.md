---

# V2F_and_F2V.py

## Overview

This Python script is designed to convert a video file into individual frames and vice versa using the OpenCV library. It takes a user-input video file path, extracts frames from the video, and saves them as individual image files. Additionally, it can convert a sequence of frames back into a video.

## Requirements

- Python 3.x
- OpenCV (cv2) library

## How to Use

1. **Install Dependencies:**

   Make sure you have Python installed on your system. You can install the required libraries using the following command:

   ```bash
   pip install opencv-python
   ```

2. **Run the Script:**

   Execute the script using a Python interpreter. You will be prompted to enter the path of the video file. The script will then process the video and save the frames in the same directory as the script.

   ```bash
   python V2F_and_F2V.py
   ```

3. **Output:**

   - For Video to Frames (V2F):

     The frames will be saved as individual image files (e.g., `frame0.jpg`, `frame1.jpg`, ...) in the same directory as the script.

   - For Frames to Video (F2V):

     The script will convert the frames (assuming they follow a sequential naming pattern) back into a video file.

## Notes

- Make sure the video file exists at the specified path.
- The frame interval is set to match the frames per second (fps) of the input video.
- The script will raise an error if the file is not found.

---
