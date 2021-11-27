from abc import ABCMeta, abstractmethod, abstractproperty
import os
from pathlib import Path
from typing import Iterator


class _AudioSplitter(metaclass=ABCMeta):
    """Splits an MP4 file at a regular spacing"""

    @abstractproperty
    def ext(self) -> str:
        """The file extension for this AudioSplitter"""

    @abstractmethod
    def split(self, filepath: str) -> None:
        """Split the given `mp4_filepath`. Results are saved in a child directory of `self._output_dir` with the same
        basename as `mp4_filepath`"""

    def __init__(self, seconds_per_split: float, output_dir: str):
        self._seconds_per_split = seconds_per_split
        self._output_dir = output_dir

        if not os.path.isdir(self._output_dir):
            os.mkdir(self._output_dir)

    def get_sub_output_dir(self, subdir: str) -> str:
        """Join `self._output_dir` with a `subdir`"""
        return os.path.join(self._output_dir, subdir)

    def iter_audio_ext_filepaths(self, audio_file_dir: str) -> Iterator[str]:
        """Yield each filepath matching `self.ext` in `audio_file_dir`. This includes the base of `audio_file_dir`"""
        for filename in os.listdir(audio_file_dir):
            filepath = os.path.join(audio_file_dir, filename)
            if Path(filepath).suffix.lower() == self.ext:
                yield filepath

    def split_dir(self, mp4_dir: str) -> None:
        """Call `split()` on all MP4 files in `mp4_dir`"""
        for filepath in self.iter_audio_ext_filepaths(mp4_dir):
            self.split(filepath)
