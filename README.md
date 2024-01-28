---

# Video to Frame and Frame to Video Converter

## Overview

This Python script, `V2F_and_F2V.py`, is designed to convert a video file into individual frames and then reconstruct those frames back into a video. It uses the OpenCV library for video processing.

## Requirements

- Python 3
- OpenCV library (`cv2`)

## Usage

1. Clone or download the repository.
2. Ensure that you have Python 3 installed.
3. Install the required library using:

    ```bash
    pip install opencv-python
    ```

4. Run the script:

    ```bash
    python V2F_and_F2V.py
    ```

5. Enter the full path of the video file when prompted.

6. The script will process the video, converting it into individual frames and then reconstructing those frames back into a video.

## Output

The script will generate an output video file named `Output.avi` in the same directory as the script.

## Notes

- Make sure the video file exists at the specified path.
- The script uses the DIVX codec for the output video. Ensure that your system supports this codec.

## Author

[Bharat_Sharma]


---
