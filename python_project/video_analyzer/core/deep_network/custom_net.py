from core.deep_network.algorithm import Algorithm


class CustomNet(Algorithm):
    def run(self, folder_path, word):
        print('execute CustomNet')
        return ['dog']
