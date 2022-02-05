import datetime
import os
import subprocess
import sys
import time
import traceback

from PySide2 import QtWidgets
# from PySide2.QtCore import QProcess
from PySide2.QtGui import QFontDatabase

from Main_Window import Ui_Form

date = datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S")


def check_pyinstaller():
    if getattr(sys, "frozen", False) and hasattr(sys, "_MEIPASS"):
        print(
            "[INFO] You are running from PyInstaller packed executable. Hopes there is no bug."
        )
        return True
    else:
        print("[INFO] You are running from normal Python source code.")
        return False


def ffmpeg_process_rework(
        resolution_w, resolution_h, frame_rate, input_dir, output_dir, file_format, fps
):
    if not check_pyinstaller():
        subprocess.Popen(
            [
                "python",
                "runner.py",
                "--input",
                input_dir,
                "--output",
                output_dir,
                "--fps",
                fps,
                "--time",
                f"{frame_rate}",
                "--format",
                file_format,
            ]
        )
    else:
        subprocess.Popen(
            [
                "runner.exe",
                "--input",
                input_dir,
                "--output",
                output_dir,
                "--fps",
                fps,
                "--time",
                f"{frame_rate}",
                "--format",
                file_format,
            ]
        )
    # print(process.communicate()[0].decode("utf-8"))
    # return process.communicate()[1].decode("utf-8")


"""
def ffmpeg_process_qprocess(
        self,
        resolution_w,
        resolution_h,
        frame_rate,
        input_dir,
        output_dir,
        file_format,
        fps,
):
    log_location = f"ErrorLog/ffmpeg_{date}.txt"
    if not check_pyinstaller():
        self.ui.StartButton.setEnabled(False)
        self.ui.StartButton.setText("處理中...")
        self.p = QProcess()
        self.p.setProcessChannelMode(QProcess.ForwardedChannels)
        # self.p.readyRead.connect(self.ui.ErrorLog.setText)
        self.p.start(
            "python",
            [
                "runner.py",
                "--input",
                input_dir,
                "--output",
                output_dir,
                "--fps",
                fps,
                "--time",
                f"{frame_rate}",
                "--format",
                file_format,
            ],
        )
    else:
        self.p = QProcess()
        self.p.setProcessChannelMode(QProcess.ForwardedChannels)
        # self.p.readyReadStandardOutput.connect(self.ui.ErrorLog.setText)
        self.p.start(
            "runner.exe",
            [
                "--input",
                input_dir,
                "--output",
                output_dir,
                "--fps",
                fps,
                "--time",
                f"{frame_rate}",
                "--format",
                file_format,
            ],
        )
    self.p.finished.connect(self.process_finished)
"""

"""
async def ffmpeg_process(
    resolution_w, resolution_h, frame_rate, input_dir, output_dir, file_format, fps
):
    if resolution_w and resolution_h:
        process_log = subprocess.Popen(
            [
                "ffmpeg.exe",
                "-y",
                "-framerate",
                f"1/{frame_rate}",
                "-i",
                f"{input_dir}/%03d.{file_format}",
                "-c:v",
                "libx264",
                "-vf",
                f"fps={fps}",
                "-pix_fmt",
                "yuv420p",
                f"{output_dir}",
                "-s",
                f"{resolution_w}x{resolution_h}",
            ],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
        )
    else:
        process_log = subprocess.Popen(
            [
                "ffmpeg.exe",
                "-y",
                "-framerate",
                f"1/{frame_rate}",
                "-i",
                f"{input_dir}/%03d.{file_format}",
                "-c:v",
                "libx264",
                "-vf",
                f"fps={fps}",
                "-pix_fmt",
                "yuv420p",
                f"{output_dir}",
            ],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            shell=True,
        )
    return process_log.communicate()[1].decode("utf-8")
"""


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.ui = Ui_Form()
        self.ui.setupUi(self)

        QFontDatabase.addApplicationFont("NotoSansTC-Regular.otf")
        # self.ui.Color.addItems(supported_color_space)
        # self.ui.Resolution_W.setText("1920")
        # self.ui.Resolution_H.setText("1080")
        # self.ui.ErrorLog.moveCursor(QtGui.QTextCursor.End)
        self.ui.Resolution_W.setEnabled(False)
        self.ui.Resolution_H.setEnabled(False)
        """
        self.scrollbar = (
            self.ui.ErrorLog.verticalScrollBar()
        )
        """  # the self.scrollbar is the same as your self.console_window
        """
        try:
            time.sleep(0.1)  # needed for the refresh
            self.scrollbar.setValue(10000)  # try input different high value

        except:
            pass  # when it is not available
        """
        self.ui.InputButton.clicked.connect(self.open_folder)
        self.ui.OutputButton.clicked.connect(self.open_file)
        self.ui.StartButton.clicked.connect(self.start)
        # self.ui.Progress.setEnabled(False)

    """
    def message(self, s):
        self.ui.ErrorLog.append(s)
    """

    def process_finished(self):
        # self.ui.StartButton.setEnabled(True)
        # self.ui.StartButton.setText("開始")
        # self.ui.Progress.setValue(100)
        pass

    def open_folder(self):
        if input_dir := QtWidgets.QFileDialog.getExistingDirectory(
                self, "選擇資料夾(請確保只有要輸入的圖片以避免錯誤)"
        ):
            self.ui.InputDir.setText(input_dir)
        else:
            print("No Directory Selected")

    def open_file(self):
        output_dir = QtWidgets.QFileDialog.getSaveFileName(
            self, "選擇輸出檔案", date, "MPEG-4 (*.mp4)"
        )
        if output_dir[0]:
            self.ui.OutputDir.setText(output_dir[0])
        else:
            print("No File Selected")

    def start(self):
        if self.ui.InputDir.text() == "":
            QtWidgets.QMessageBox.information(
                self, "錯誤", "請選擇輸入資料夾", QtWidgets.QMessageBox.Close
            )
            return False

        if self.ui.OutputDir.text() == "":
            QtWidgets.QMessageBox.information(
                self, "錯誤", "請選擇輸出檔案", QtWidgets.QMessageBox.Close
            )
            return False
        input_dir = self.ui.InputDir.text()

        if os.path.isdir(input_dir) is False:
            QtWidgets.QMessageBox.information(
                self, "錯誤", "輸入資料夾不存在", QtWidgets.QMessageBox.Close
            )
            return False
        output_dir = self.ui.OutputDir.text()
        resolution_w = self.ui.Resolution_W.text()
        resolution_h = self.ui.Resolution_H.text()
        frame_rate = self.ui.Framerate.text()
        fps = self.ui.FPS.text()
        file_format = self.ui.FileFormat.text()
        if file_format == "":
            QtWidgets.QMessageBox.information(
                self, "錯誤", "請輸入檔案格式", QtWidgets.QMessageBox.Close
            )
            return False
        elif file_format.find(".") != -1:
            file_format = file_format.replace(".", "")

        if os.path.isfile(output_dir) is True:
            if QtWidgets.QMessageBox.Yes == QtWidgets.QMessageBox.warning(
                    self,
                    "警告",
                    "輸出檔案已存在，是否覆寫",
                    QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                    QtWidgets.QMessageBox.Yes,
            ):
                print("Overwrite")
            else:
                print("Cancel")
                return False

        print("Start")

        try:
            ffmpeg_process_rework(
                resolution_w,
                resolution_h,
                frame_rate,
                input_dir,
                output_dir,
                file_format,
                fps,
            )
            time.sleep(1)
        except:
            self.ui.ErrorLog.setText("處理失敗")
            QtWidgets.QMessageBox.information(
                self, "警告", "處理失敗", QtWidgets.QMessageBox.Close
            )
            error_traceback = traceback.format_exc()
            print(error_traceback)
            if not os.path.isdir("ErrorLog"):
                os.mkdir("ErrorLog")
            with open(
                    "ErrorLog/ErrorLog_{}.txt".format(date), "w", encoding="utf-8"
            ) as f:
                f.write(error_traceback)
            self.ui.ErrorLog.setText(error_traceback)


if __name__ == "__main__":
    app = QtWidgets.QApplication()
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
