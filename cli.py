import argparse
from .src.analyze import video_analyzer


ap = argparse.ArgumentParser()
ap.add_argument("-f", "--file", type=str, help="path to the video file")
args = vars(ap.parse_args())

if not args["file"]:
  print("Please supply a video file '-f <path>'")
  exit()

timecode = video_analyzer(args["file"])
print(timecode)
