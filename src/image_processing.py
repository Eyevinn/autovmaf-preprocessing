import cv2
import numpy as np


def get_pixel_counts(img_rgb):
    """
    Detects edges in an image, converts it to
    a grayscale image and then counts the number of black/white pixels
    """
    image = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2RGB)
    gray_img = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    edge = cv2.Canny(gray_img, 60, 180)
    return get_number_of_pixels(img=edge)


def motion_detector(curr_img_rgb, prev_img_rgb, threshold, debug_video):
    """
    Detects motion in an image and returns the difference as a black and white frame
    Difference is calculated by comparing the current frame with the previous frame

    The white pixels are the motion pixels
    """
    if threshold > 255:
        threshold = 255

    curr_frame = cv2.cvtColor(curr_img_rgb, cv2.COLOR_BGR2GRAY)
    curr_frame = cv2.GaussianBlur(src=curr_frame, ksize=(1, 1), sigmaX=0)

    prev_frame = cv2.cvtColor(prev_img_rgb, cv2.COLOR_BGR2GRAY)
    prev_frame = cv2.GaussianBlur(src=prev_frame, ksize=(1, 1), sigmaX=0)
    diff_frame = cv2.absdiff(src1=curr_frame, src2=prev_frame)

    kernel = np.ones((1, 1))

    diff = cv2.dilate(src=diff_frame, kernel=kernel)
    diff[diff > threshold] = 255

    if debug_video:
        gray_rgb = cv2.cvtColor(diff, cv2.COLOR_GRAY2BGR)
        debug_img = np.concatenate((curr_img_rgb, gray_rgb), axis=0)
        cv2.imshow('AutoVMAF Preprocessing - debug', debug_img)
        cv2.waitKey(1)

    return get_number_of_pixels(img=diff)


def get_number_of_pixels(img):
    """
    Returns the number of black and white pixels in an image
    as a dictionary with the keys 'black' and 'white'
    """
    return {'white': np.sum(img == 255), 'black': np.sum(img == 0)}


def get_video_framerate(video_path):
    """
    Returns the framerate of a video as an integer
    """
    video = cv2.VideoCapture(video_path)
    return int(video.get(cv2.CAP_PROP_FPS))


def get_video_timecode(frames, fps):
    """
    Returns the time-code of a video in the format of HH:MM:SS:FF
    """
    frames = int(frames)
    fps = int(fps)
    return '{0:02d}:{1:02d}:{2:02d}:{3:02d}'.format(int(frames / (3600*fps)),
                                                    int(frames / (60*fps) %
                                                        60),
                                                    int(frames / fps % 60),
                                                    int(frames % fps))
