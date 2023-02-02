import sys
import cv2
import argparse
import os


print("OpenCV version"+cv2.__version__)


def variance_of_laplacian(image):
    """
    compute the Laplacian of the image and return the focus measure
    """
    return cv2.Laplacian(image, cv2.CV_64F).var()


parser = argparse.ArgumentParser()
parser._action_groups.pop()
required = parser.add_argument_group('required arguments')
optional = parser.add_argument_group('optional arguments')
required.add_argument("-p", "--path", type=str, default="",
                      help="path to the video file", required=True)
optional.add_argument("-t", "--threshold", type=float, default=100.0,
                      help="default threshold is 100.0. Use 10-30 for motion")
optional.add_argument("-s", "--step", type=int,
                      default=1, help="frame step size")
optional.add_argument("--save", default= "", type= str, help= "path to save the frames in a directory")
args = vars(parser.parse_args())

if not args["path"]:
    sys.exit("Please supply a video file '-p <path>'")

vidcap = cv2.VideoCapture(args["path"])

success, image = vidcap.read()
count = 0
blurryFrame = 0
savedFrame = 0
frameStep = 0
step = args["step"]

print("Working...")

while success:
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    fm = variance_of_laplacian(gray)

    if frameStep == step:
        if fm > args["threshold"]:
            savedFrame += 1
            image_path = os.path.join(args["save"], "frame%d.png" % count)
            cv2.imwrite(image_path, image)
        frameStep = 0

    if fm < args["threshold"]:
        blurryFrame += 1

    success, image = vidcap.read()
    count += 1
    frameStep += 1

sys.exit("Done!")
