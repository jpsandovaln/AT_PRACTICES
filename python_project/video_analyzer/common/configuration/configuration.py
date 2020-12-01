from common.configuration.config_manager import ConfigManager


class Configuration:

    @staticmethod
    def get_ffmpeg_path():
        con = ConfigManager()
        return con.get_value_as_string('ffmpeg_path')

    @staticmethod
    def get_output_image_path():
        con = ConfigManager()
        return con.get_value_as_string('output_path')

    @staticmethod
    def get_video_format_list():
        con = ConfigManager()
        return con.get_value_as_list('video_format')

