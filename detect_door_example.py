import cv2
import numpy as np

# Initialize video capture from a file or camera
video_path = 'path_to_your_video.mp4'  # Replace with the path to your video file
cap = cv2.VideoCapture(video_path)

# Define the color range for blue
lower_blue = np.array([100, 50, 50])
upper_blue = np.array([140, 255, 255])

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    
    # Convert frame to HSV color space
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    # Create a mask for the blue color range
    blue_mask = cv2.inRange(hsv_frame, lower_blue, upper_blue)
    
    # Apply morphological operations to remove noise
    kernel = np.ones((5, 5), np.uint8)
    blue_mask = cv2.morphologyEx(blue_mask, cv2.MORPH_OPEN, kernel)
    
    # Find contours in the mask
    contours, _ = cv2.findContours(blue_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    door_open = False
    
    for contour in contours:
        # You might need to adjust these parameters based on your video and door size
        if cv2.contourArea(contour) > 1000:
            # Draw a bounding rectangle around the detected object
            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            
            # Check if the detected area is wide enough to consider it as a door open
            if w > h * 2:
                door_open = True
                
    if door_open:
        cv2.putText(frame, 'Door Open', (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    else:
        cv2.putText(frame, 'Door Closed', (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    
    cv2.imshow('Sliding Door Detection', frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
