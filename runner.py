# from PySide2.QtGui import QFontDatabase
import argparse
import os
# from better_ffmpeg_progress import FfmpegProcess
# import os
# import sys
import subprocess
import traceback
from datetime import datetime

# from PySide2.QtGui import QFontDatabase
# from PySide2.QtWidgets import QProgressDialog
from PySide2 import QtWidgets

# from PySide2 import QtWidgets

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

try:
    subprocess.Popen(
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
        ],
        creationflags=subprocess.CREATE_NEW_CONSOLE,
    )
except Exception:
    date = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    traceback_data = traceback.format_exc()
    if not os.path.isdir("ErrorLog"):
        os.mkdir("ErrorLog")
    with open(f"ErrorLog/traceback_{date}.txt", "w") as f:
        f.write(traceback_data)

    class MainWindow(QtWidgets.QMainWindow):
        def __init__(self, parent=None):
            super(MainWindow, self).__init__(parent)
            QtWidgets.QMessageBox.critical(
                self,
                "Error",
                "Something went wrong.\n"
                'Please go to "ErrorLog" folder and report to developer.',
            )

    app = QtWidgets.QApplication()
    window = MainWindow()
    window.show()
