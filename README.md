# DoorStatusTracker

## work Guidelines
  1) work with git and with reasonably commit message
  2) if you build a env build recored its depends (requirements.txt for example)
  3) pick algorthims which are the simplest at first and then take more complex one (we might need to train the networks)
  4) We are processing video input and it's essential to ensure real-time performance at 25 frames per second (fps).
## Taks
  1) Check if there is an open source solution that can detect and track doors. In my opinion, a simple algorithm with OpenCV can do the job.
  2) get the data and and tagging (timestamp of the close and the open door) and validted that the tagging it true.
  3) create a simple poc where the video is read from file or socket and print to log every time a door is open or close.
  4) Utilize MLflow to establish an evaluation process where the network's output is compared with the tagging. 
     Make this process generic so that it can be used to assess multiple algorithms as needed.
## notes
  1) we have two doors to track
  1) The doors have a specific color
  2) there is a 3 camera in the room so we might need to create a panorama of all the images
