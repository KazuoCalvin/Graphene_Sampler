from PyQt5 import QtWidgets, QtCore, QtGui, uic
import cv2

class SampleTab:

    def __init__(self, parent: QtWidgets.QWidget):

        self.parent = parent
        uic.loadUi("src/app/ui/Sample_Tab.ui", self.parent)

        # Initialize camera timer
        self.fps = 30
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(int(1000 / self.fps))

        self.camera_index = 0
        self.cap = None
        self.select_camera()

        self.last_frame = None



    def select_camera(self):

        if self.cap:
            self.cap.release()
            self.cap = None

        self.cap = cv2.VideoCapture(self.camera_index)

    def update_frame(self):
        ret, frame = self.cap.read()

        if ret:

            self.last_frame = frame
            qt_img = self._cv_to_pixmap(frame)

            self.parent.live_feed_label.setPixmap(qt_img)
            self.parent.live_feed_label.setScaledContents(True)


    def  _cv_to_pixmap(self, cv_img):
        """Convert from an opencv image to QPixmap"""

        rgb_image = cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB)
        h, w, ch = rgb_image.shape
        bytes_per_line = ch * w

        convert_to_Qt_format = QtGui.QImage(rgb_image.data, w, h, bytes_per_line, QtGui.QImage.Format_RGB888)
        p = convert_to_Qt_format.scaled(640, 480, QtCore.Qt.KeepAspectRatio)

        return QtGui.QPixmap.fromImage(p)