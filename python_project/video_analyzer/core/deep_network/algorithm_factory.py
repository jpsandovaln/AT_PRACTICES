from core.deep_network.lee_net import LeeNet
from core.deep_network.proxy_lee_net import ProxyLeeNet
from core.deep_network.custom_net import CustomNet


class AlgorithmFactory:
    @staticmethod
    def instance(algorithm_param):
        print(algorithm_param)
        if algorithm_param == 'LeeNet':
            return LeeNet()
        if algorithm_param == 'ProxyLeeNet':
            return ProxyLeeNet()
        else:
            return CustomNet()
