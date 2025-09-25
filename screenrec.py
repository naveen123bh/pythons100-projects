import pyautogui
import cv2
import numpy as np

# Get screen resolution
screen_size = pyautogui.size()
resolution = screen_size

# Codec & output
# Use mp4v for .mp4 (widely supported)
codec = cv2.VideoWriter_fourcc(*"mp4v")
filename = "Recording.mp4"
fps = 20.0

# Initialize video writer
out = cv2.VideoWriter(filename, codec, fps, resolution)

# Create live preview window
cv2.namedWindow("Live", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Live", 480, 270)

while True:
    # Take screenshot
    img = pyautogui.screenshot()
    frame = np.array(img)

    # Convert RGB (PIL/pyautogui) → BGR (OpenCV)
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

    # Ensure resolution matches what VideoWriter expects
    if (frame.shape[1], frame.shape[0]) != resolution:
        frame = cv2.resize(frame, resolution)

    # Write frame to video
    out.write(frame)

    # Show live preview
    cv2.imshow("Live", frame)

    # Press 'q' to stop recording
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release writer and windows
out.release()
cv2.destroyAllWindows()

print("Recording stopped and saved to", filename)