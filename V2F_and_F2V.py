# Vedio to Frame and Frame to Vedio
import cv2
import os

path=input("Enter Vedio Path : ")
if (os.path.exists(path)):
    vedio = cv2.VideoCapture(path)
    fps = vedio.get(cv2.CAP_PROP_FPS)
    frame_interval = int(fps)

    success, image = vedio.read()
    count = 0

    while success:
        frame_filename = os.path.join(output_directory, f"frame{count}.jpg")
        cv2.imwrite(frame_filename, image)

        if not os.path.isfile(frame_filename):
            print(f"Error: Failed to save frame {count}.")
            exit()

        for i in range(frame_interval):
            success, image = vidcap.read()

        print(f"Saved frame {count} to {frame_filename}")
        count += 1

    vidcap.release()
else:
    raise IOError("Error: File  not Found. ")