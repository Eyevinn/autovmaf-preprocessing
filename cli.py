import sys
import argparse
from src.analyze import video_analyzer


parser = argparse.ArgumentParser()
parser._action_groups.pop()
required = parser.add_argument_group('required arguments')
optional = parser.add_argument_group('optional arguments')
required.add_argument("-f", "--file", type=str, help="path to the video file")
optional.add_argument("-d", "--debug", action='store_true',
                      help="show the current processed frame", default=False)
optional.add_argument("-t", "--threshold", type=int,
                      help="threshold for motion detection, default: 4 max: 255", default=4)
args = vars(parser.parse_args())

if not args["file"]:
    sys.exit("Please supply a video file '-f <path>'")

timecode = video_analyzer(args["file"], args["threshold"], debug_video=args["debug"])
sys.stdout.write(timecode)
sys.exit(0)
