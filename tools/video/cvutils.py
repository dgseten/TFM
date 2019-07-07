import cv2
import os
import shutil


def print_capture_properties(cap,mode=0):
    print("===== Capture properties, mode {}: =====".format(mode))
    print("Current position of the video file in milliseconds: {}".format(cap.get(cv2.CAP_PROP_POS_MSEC)))
    print("0-based index of the frame to be decoded/captured next: {}".format(cap.get(cv2.CAP_PROP_POS_FRAMES)))
    print("Relative position of the video file: 0=start of the film, 1=end of the film: {}".format(cap.get(cv2.CAP_PROP_POS_AVI_RATIO)))
    print("Width of the frames in the video stream: {}".format(cap.get(cv2.CAP_PROP_FRAME_WIDTH)))
    print("Height of the frames in the video stream: {}".format(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
    print("Frame rate: {}".format(cap.get(cv2.CAP_PROP_FPS)))
    print("4-character code of codec: {}".format(cap.get(cv2.CAP_PROP_FOURCC)))
    print("Number of frames in the video file: {}".format(cap.get(cv2.CAP_PROP_FRAME_COUNT)))
    print("Format of the Mat objects returned by VideoCapture::retrieve() : {}".format(cap.get(cv2.CAP_PROP_FORMAT)))
    print("Backend-specific value indicating the current capture mode: {}".format(cap.get(cv2.CAP_PROP_MODE )))
    print("Brightness of the image (only for those cameras that support): {}".format(cap.get(cv2.CAP_PROP_BRIGHTNESS  )))
    print("Contrast of the image (only for cameras): {}".format(cap.get(cv2.CAP_PROP_CONTRAST  )))
    print("Saturation of the image (only for cameras): {}".format(cap.get(cv2.CAP_PROP_SATURATION  )))
    print("Hue of the image (only for cameras): {}".format(cap.get(cv2.CAP_PROP_HUE  )))
    print("Gain of the image (only for those cameras that support): {}".format(cap.get(cv2.CAP_PROP_GAIN  )))
    print("Exposure (only for those cameras that support): {}".format(cap.get(cv2.CAP_PROP_EXPOSURE  )))
    print("Boolean flags indicating whether images should be converted to RGB: {}".format(cap.get(cv2.CAP_PROP_CONVERT_RGB  )))
    print("CAP_PROP_WHITE_BALANCE_BLUE_U,currently unsupported: {}".format(cap.get(cv2.CAP_PROP_WHITE_BALANCE_BLUE_U  )))
    print("Rectification flag for stereo cameras (note: only supported by DC1394 v 2.x backend currently): {}".format(cap.get(cv2.CAP_PROP_RECTIFICATION  )))
    print("CAP_PROP_MONOCHROME: {}".format(cap.get(cv2.CAP_PROP_MONOCHROME )))
    print("CAP_PROP_SHARPNESS: {}".format(cap.get(cv2.CAP_PROP_SHARPNESS )))
    print("DC1394: exposure control done by camera, user can adjust reference level using this feature: {}".format(cap.get(cv2.CAP_PROP_AUTO_EXPOSURE )))
    print("CAP_PROP_GAMMA: {}".format(cap.get(cv2.CAP_PROP_GAMMA )))
    print("CAP_PROP_TEMPERATURE: {}".format(cap.get(cv2.CAP_PROP_TEMPERATURE )))
    print("CAP_PROP_TRIGGER: {}".format(cap.get(cv2.CAP_PROP_TRIGGER )))
    print("CAP_PROP_TRIGGER_DELAY: {}".format(cap.get(cv2.CAP_PROP_TRIGGER_DELAY )))
    print("CAP_PROP_WHITE_BALANCE_RED_V: {}".format(cap.get(cv2.CAP_PROP_WHITE_BALANCE_RED_V )))
    print("CAP_PROP_ZOOM: {}".format(cap.get(cv2.CAP_PROP_ZOOM )))
    print("CAP_PROP_FOCUS: {}".format(cap.get(cv2.CAP_PROP_FOCUS )))
    print("CAP_PROP_GUID: {}".format(cap.get(cv2.CAP_PROP_GUID )))
    print("CAP_PROP_ISO_SPEED: {}".format(cap.get(cv2.CAP_PROP_ISO_SPEED )))
    print("CAP_PROP_BACKLIGHT: {}".format(cap.get(cv2.CAP_PROP_BACKLIGHT )))
    print("CAP_PROP_PAN: {}".format(cap.get(cv2.CAP_PROP_PAN )))
    print("CAP_PROP_TILT: {}".format(cap.get(cv2.CAP_PROP_TILT )))
    print("CAP_PROP_ROLL: {}".format(cap.get(cv2.CAP_PROP_ROLL )))
    print("CAP_PROP_IRIS: {}".format(cap.get(cv2.CAP_PROP_IRIS )))
    print("Pop up video/camera filter dialog (note: only supported by DSHOW backend currently. The property value is ignored): {}".format(cap.get(cv2.CAP_PROP_SETTINGS )))
    print("CAP_PROP_BUFFERSIZE: {}".format(cap.get(cv2.CAP_PROP_BUFFERSIZE )))
    print("CAP_PROP_AUTOFOCUS: {}".format(cap.get(cv2.CAP_PROP_AUTOFOCUS )))
    print("==================================".format(mode))


def create_dir(path):
    os.makedirs(path, exist_ok=True)