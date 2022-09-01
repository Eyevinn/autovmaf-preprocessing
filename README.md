# AutoVMAF Preprocessing

Python script that analyzes a video (local file or hls-stream) via a combination of motion and sharpness to determine the most suitable section to be used for VMAF analysis.

The output is a time-code of the frame that contains the most motion and finer details. This can for example be confetti, particles, tree leaves, etc.

Example of a processed frame:
The tool converts motion pixels to white and everything else to black pixels.
The percentage of white pixels in the frame and the overall sharpness of the original frame (how much that is in focus) is then calculated per frame and then compared to the next frame and so on.

## Usage

Example:

```python
from .src.analyze import video_analyzer

threshold = 4 # Motion threshold (higher = more motion required) (default: 25 max: 255)
timecode = video_analyzer(file_path="video.mp4", threshold=threshold)

print(timecode) # HH:MM:SS:FF

# To run the script with the debug option to show the processed frames:
timecode = video_analyzer(file_path="video.mp4", threshold=threshold, debug_video=True)

print(timecode) # HH:MM:SS:FF
```

An example CLI have also been provided that prints the timecode to the console.

```text
usage: cli.py [-h] [-f FILE] [-d] [-t THRESHOLD]

required arguments:
  -f FILE, --file FILE  path to the video file

optional arguments:
  -d, --debug           show the current processed frame
  -t THRESHOLD, --threshold THRESHOLD
                        threshold for motion detection, default: 25 max: 255
```

Example:

```bash
python cli.py -f video.mp4 -t 4

# To run the script with the debug option to show the processed frames:
python cli.py -f video.mp4 -t 4 -d
```

## About Eyevinn Technology

Eyevinn Technology is an independent consultant firm specialized in video and streaming. Independent in a way that we are not commercially tied to any platform or technology vendor.

At Eyevinn, every software developer consultant has a dedicated budget reserved for open source development and contribution to the open source community. This give us room for innovation, team building and personal competence development. And also gives us as a company a way to contribute back to the open source community.

Want to know more about Eyevinn and how it is to work here. Contact us at work@eyevinn.se!
