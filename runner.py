# from PySide2.QtGui import QFontDatabase
# from better_ffmpeg_progress import FfmpegProcess
# import os
import sys
import subprocess
import argparse
from PySide2 import QtWidgets

# from PySide2.QtGui import QFontDatabase
"""
TEMP = os.environ.get("TEMP")
TEMP = TEMP.replace("\\", "/")
"""
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

process = subprocess.check_output(
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

"""
def handle_progress_info(percentage, speed, eta, estimated_filesize):
    print(f"{percentage}% ETA: {eta}")
"""
"""
if not os.path.exists(f"{TEMP}/ffmpeg_output"):
    os.makedirs(f"{TEMP}/ffmpeg_output")
"""
"""
process.run(
    progress_handler=handle_progress_info,
    ffmpeg_output_file=f"{TEMP}/ffmpeg_output/ffmpeg_output.txt",
)
"""


class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        # QFontDatabase.addApplicationFont("NotoSansTC-Regular.otf")
        QtWidgets.QMessageBox.information(
            self, "完成", f"轉檔完成\n請查看\n{output_file}", QtWidgets.QMessageBox.Ok
        )
        sys.exit()


if __name__ == "__main__":
    app = QtWidgets.QApplication()
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
