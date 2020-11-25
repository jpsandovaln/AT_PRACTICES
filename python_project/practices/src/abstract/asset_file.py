from src.abstract.asset_base import AssetBase


class AssetFile(AssetBase):
    def get_value(self):
        print('test value......')

    def get_other_value(self):
        print('value two ......')
