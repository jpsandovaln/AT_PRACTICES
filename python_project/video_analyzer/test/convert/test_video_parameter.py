import unittest
from core.convert.video_parameter import VideoParameter
from common.exception.validate_error import ValidateError


class TestVideoParameter(unittest.TestCase):
    def test_invalid_parameter_none(self):
        param = VideoParameter()
        param.set_ffmpeg_path(None)
        param.set_video_path(None)
        param.set_output_folder(None)

        with self.assertRaises(ValidateError):
            param.validate()

    def test_invalid_parameter_empty(self):
        param = VideoParameter()
        param.set_ffmpeg_path('')
        param.set_video_path('')
        param.set_output_folder('')

        with self.assertRaises(ValidateError):
            param.validate()

    def test_invalid_parameter_video_path(self):
        param = VideoParameter()
        param.set_ffmpeg_path('D:\\MAESTRIA\\TecEmergentes\\video_analyzer\\thirdparty\\ffmpeg\\ffmpeg.exe')
        param.set_video_path('xd:/video.mp4')
        param.set_output_folder('D:\\MAESTRIA\\TecEmergentes\\video_analyzer\\output_image\\')

        with self.assertRaises(ValidateError):
            param.validate()
