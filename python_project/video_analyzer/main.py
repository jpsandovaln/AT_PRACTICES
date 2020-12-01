from core.convert.video_manager import VideoManger
from core.deep_network.algorithm_factory import AlgorithmFactory
from core.convert.video_parameter import VideoParameter

import sys
from PyQt5.QtWidgets import QApplication
from view.view import View
from controller.controller import Controller


if __name__ == '__main__':
    '''algorithm_param = 'LeeNet'
    word = 'gazelle' #zebra, #elephant, #impala #hartebeest #gazelle bow buffalo tusker  hippopotamus bison ox maze
    min_accepted_percentage = 50

    video_path = VideoParameter()
    video_path.set_ffmpeg_path('D:\\MAESTRIA\\TecEmergentes\\video_analyzer\\thirdparty\\ffmpeg\\ffmpeg.exe')
    # video_path.set_ffmpeg_path(None)
    video_path.set_video_path('D:\\MAESTRIA\\TecEmergentes\\video_analyzer\\videos\\animales.mp4')
    video_path.set_output_folder('D:\\MAESTRIA\\TecEmergentes\\video_analyzer\\output_image\\')

    video_path.validate()

    video = VideoManger()
    video.convert(video_path)

    algorithm = AlgorithmFactory.instance(algorithm_param)
    print(algorithm.run(video_path.get_output_folder(), word, min_accepted_percentage))'''

    app = QApplication(sys.argv)
    view = View()
    controller = Controller(view)
    sys.exit(app.exec())
