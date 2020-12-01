from common.validation.contexto import Context
from common.validation.null_or_empty_validation import NullOrEmptyValidation
from common.validation.file_validation import FileValidation


class VideoParameter:
    def __init__(self):
        self.ffmpeg_path = ''
        self.video_path = ''
        self.output_folder = ''

    def get_ffmpeg_path(self):
        return self.ffmpeg_path

    def set_ffmpeg_path(self, ffmpeg):
        self.ffmpeg_path = ffmpeg

    def get_video_path(self):
        return self.video_path

    def set_video_path(self, video_path):
        self.video_path = video_path

    def get_output_folder(self):
        return self.output_folder

    def set_output_folder(self, output_folder):
        self.output_folder = output_folder

    def validate(self):
        strategies = [
            NullOrEmptyValidation(self.ffmpeg_path),
            NullOrEmptyValidation(self.video_path),
            NullOrEmptyValidation(self.output_folder),
            FileValidation(self.video_path),
            FileValidation(self.ffmpeg_path)
        ]
        context = Context(strategies)
        context.validate()
