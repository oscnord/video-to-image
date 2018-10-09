import argparse
import cv2

print("OpenCV version",cv2.__version__)

def variance_of_laplacian(image):
	# compute the Laplacian of the image and return the focus measure
	return cv2.Laplacian(image, cv2.CV_64F).var()

# construct and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-t", "--threshold", type=float, default=100.0,
	help="default threshold is 100.0. Use 10-30 for motion")
args = vars(ap.parse_args())

path = raw_input("Enter path to video file: ")

vidcap = cv2.VideoCapture(path)

success, image = vidcap.read()
count = 0
blurryFrame = 0
savedFrame = 0
success = True

print("Working...")

while success:
  gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
  fm = variance_of_laplacian(gray)
  if fm >  args["threshold"]:
    savedFrame += 1
    cv2.imwrite("frame%d.png" % count, image)
    
  if fm < args["threshold"]:
    blurryFrame += 1

  success,image = vidcap.read()
  count += 1

print("Done!", "Number of frames: ", count)
print("Saved frames: ", savedFrame)
print("Discarded frames: ", blurryFrame)
