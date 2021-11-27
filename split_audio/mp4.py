import os
from pathlib import Path
from typing import Iterator

from moviepy.editor import AudioFileClip
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip

from .audio_splitter import _AudioSplitter


class MP4Splitter(_AudioSplitter):
    """Splits an MP4 file at a regular spacing"""

    @property
    def ext(self) -> str:
        return ".mp4"

    def split(self, filepath: str) -> None:
        subdir = self.get_sub_output_dir(Path(filepath).stem)
        if not os.path.exists(subdir):
            os.mkdir(subdir)

        idx = 0
        lsplit = 0
        while lsplit < AudioFileClip(filepath).duration:
            rsplit = lsplit + self._seconds_per_split
            ffmpeg_extract_subclip(filepath, lsplit, rsplit, os.path.join(subdir, f"{idx}.mp4"))
            idx += 1
            lsplit = rsplit

        return
