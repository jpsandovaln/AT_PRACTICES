from core.deep_network.lee_net import LeeNet
from core.deep_network.custom_net import CustomNet


class AlgorithmFactory:
    @staticmethod
    def instance(algorithm_param):
        print(algorithm_param)
        if algorithm_param == 'LeeNet':
            return LeeNet()
        else:
            return CustomNet()
