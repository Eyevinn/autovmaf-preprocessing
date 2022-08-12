import cv2
from .image_processing import get_pixel_counts, motion_detector, get_video_framerate, get_video_timecode


def video_analyzer(file_path, threshold=4, debug_video=False):
    """
    Analyzes a video and returns the timecode
    of the frame with the most motion/detail
    """
    frame = 0
    count = 0
    edgePixels = 0
    motion_percentage = 0
    video = cv2.VideoCapture(file_path)
    success, image = video.read()
    prev_img = image

    print("Analyzing " + file_path)
    while success:
        img_info = get_pixel_counts(img_rgb=image)
        motion = motion_detector(curr_img_rgb=image, prev_img_rgb=prev_img, threshold=threshold, debug_video=debug_video)
        percentage = (motion['white'] /
                      (motion['black'] + motion['white'])) * 100
        if img_info['white'] > edgePixels and percentage > motion_percentage:
            edgePixels = img_info['white']
            motion_percentage = percentage
            frame = count
        prev_img = image
        success, image = video.read()
        count += 1

    framerate = get_video_framerate(video_path=file_path)
    timecode = get_video_timecode(frames=frame, fps=framerate)
    return timecode
