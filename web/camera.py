import time
from base_camera import BaseCamera
import cv2

class Camera(BaseCamera):
    """An emulated camera implementation that streams a repeated sequence of
    files 1.jpg, 2.jpg and 3.jpg at a rate of one frame per second."""
    imgs = [open(f + '.jpg', 'rb').read() for f in ['1', '2', '3']]
    # 开启一个摄像头
    cap = cv2.VideoCapture(0)
    @staticmethod
    def frames():

        while True:
            time.sleep(1)
            Camera.imgs[int(time.time()) % 3]
            ret, frame = Camera.cap.read()
            # (2).先将数组类型编码成 jepg 类型的数据,然后转字节数组,最后将其用base64编码
            r, buf = cv2.imencode(".jpeg", frame)
            yield frame
