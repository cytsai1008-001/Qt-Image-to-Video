# from PySide2.QtGui import QFontDatabase
import os
import traceback

from better_ffmpeg_progress import FfmpegProcess
# import os
import sys
import subprocess
import argparse
from PySide2 import QtWidgets

# from PySide2.QtGui import QFontDatabase
from PySide2.QtWidgets import QProgressDialog

TEMP = os.environ.get("TEMP")
TEMP = TEMP.replace("\\", "/")

parser = argparse.ArgumentParser()
parser.add_argument("--input", help="Input Dir", required=True)
parser.add_argument("--output", help="Output File", required=True)
parser.add_argument("--time", help="Time per picture (sec)", required=True)
parser.add_argument("--fps", help="FPS", required=True)
parser.add_argument("--width", help="Width", required=False)
parser.add_argument("--height", help="Height", required=False)
parser.add_argument("--format", help="Format", required=True)

input_dir = parser.parse_args().input
file_format = parser.parse_args().format
output_file = parser.parse_args().output
fps = parser.parse_args().fps
framerate = f"1/{parser.parse_args().time}"
full_input_dir = f"{input_dir}/%03d.{file_format}"

process = FfmpegProcess(
    [
        "ffmpeg.exe",
        "-y",
        "-framerate",
        framerate,
        "-i",
        full_input_dir,
        "-c:v",
        "libx264",
        "-pix_fmt",
        "yuv420p",
        "-vf",
        f"fps={fps}",
        output_file,
    ]
)

perc = 0


# print(f"{perc}% ETA: {eta}")
def handle_progress_info(percentage, speed, eta, estimated_filesize):
    global perc
    perc = str(percentage)


if not os.path.exists(f"{TEMP}/ffmpeg_output"):
    os.makedirs(f"{TEMP}/ffmpeg_output")


class MainProgress(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(MainProgress, self).__init__(parent)
        self.progress = QProgressDialog("正在處理", "取消", 0, 100)
        # self._progress.setMinimumDuration(0)
        self.progress.setWindowTitle("處理中")
        self.progress.setLabelText(f"正在處理{output_file}")
        self.progress.setCancelButton(None)
        self.progress.show()
        self.progress.setValue(0)
        """
        while True:
            try:
                if int(perc) == 100:
                    break
                else:
                    self.progress.setValue(int(perc))
            except:
                traceback.print_exc()
        """
        # pd.canceled.setEnabled(False)
        self.close()


class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        # QFontDatabase.addApplicationFont("NotoSansTC-Regular.otf")
        QtWidgets.QMessageBox.information(
            self, "完成", f"轉檔完成，請查看\n{output_file}", QtWidgets.QMessageBox.Ok
        )
        sys.exit()


if __name__ == "__main__":
    app = QtWidgets.QApplication()
    process.run(
        progress_handler=handle_progress_info,
        ffmpeg_output_file=f"{TEMP}/ffmpeg_output/ffmpeg_output.txt",
    )
    prog = MainProgress()
    prog.show()
    window = MainWindow()
    prog.close()
    window.show()
    sys.exit(app.exec_())
