# Video to images

Simple script to convert a video to an image sequence with blur detection using OpenCV.

## Usage

### Dependencies

* OpenCV

### Example

```shell
required arguments:
  -p PATH, --path PATH  path to the video file

optional arguments:
  -t THRESHOLD, --threshold THRESHOLD
                        default threshold is 100.0. Use 10-30 for motion
  -s STEP, --step STEP  frame step size
  --save SAVE           path to save the frames in a directory
```

Example usage:

```shell
python3 vid2img.py -p video.mp4
```
