import cv2
from base_camera import BaseCamera


class Camera(BaseCamera):
    video_source = 0

    @staticmethod
    def set_video_source(source):
        Camera.video_source = source

    @staticmethod
    def frames1():
        camera = cv2.VideoCapture(Camera.video_source)
        if not camera.isOpened():
            raise RuntimeError('Could not start camera.')

        while True:
            # read current frame
            _, img = camera.read()

            # encode as a jpeg image and return it
            yield cv2.imencode('.jpg', img)[1].tobytes()

    @staticmethod
    def frames():
        # 获得视频的格式
        videoCapture = cv2.VideoCapture('E:\迅雷下载\[阳光电影www.ygdy8.com].发现.BD.720p.中英双字幕.mkv')
        # 获得码率及尺寸
        fps = videoCapture.get(cv2.CAP_PROP_FPS)
        size = (int(videoCapture.get(cv2.CAP_PROP_FRAME_WIDTH)),
                int(videoCapture.get(cv2.CAP_PROP_FRAME_HEIGHT)))
        while True:
            # read current frame
            _, img = videoCapture.read()
            # encode as a jpeg image and return it
            yield cv2.imencode('.jpg', img)[1].tobytes()

