import argparse
from src.analyze import video_analyzer


ap = argparse.ArgumentParser()
ap.add_argument("-f", "--file", type=str, help="path to the video file")
ap.add_argument("-d", "--debug", action='store_true', help="show debug video", default=False)
args = vars(ap.parse_args())

if not args["file"]:
    print("Please supply a video file '-f <path>'")
    exit()

timecode = video_analyzer(args["file"], debug_video=args["debug"])
print(timecode)
