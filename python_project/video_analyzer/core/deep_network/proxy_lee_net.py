from core.deep_network.algorithm import Algorithm
from core.deep_network.lee_net import LeeNet


class ProxyLeeNet(Algorithm):

    def run(self, folder_path, word, min_percentage):
        print('code to validate user')
        lee_net = LeeNet()
        data = lee_net.run(folder_path, word, min_percentage)
        f = open('D:\\proxyfile.txt', 'w+')
        f.write(str(data) + '/n')
        return data
