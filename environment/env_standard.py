from pipeline.serialization import Serializable
from pipeline.module import (
    DataProvider,
    Module
)
import os, re

class EnvStandard(Module, DataProvider, Serializable):

    def __init__(self, context, params):
        Module.__init__(self, context, params)
        DataProvider.__init__(self)
        Serializable.__init__(self, cache_path=params['cachePath'])

    def build(self):
        pass

    def fetch_single_data(self, data_name):
        if not self.cache_exist():
            self.build()
        if self.data_loaded[data_name] is False:
            self.load_single_data(data_name)
            return getattr(self, data_name)

    def provide_data(self):
        self.di_list = []
        self.ii_list = []

        self.register_data('di_list', self.di_list)
        self.register_data('ii_list', self.ii_list)

    def caches(self):
        self.register_cache('di_list')
        self.register_cache('ii_list')

    def initialize(self):
        pass

    def dependencies(self):
        pass



            # class EnvStandard(Serializable):
#
#     def __init__(self, params, context):
#         self.data_path = params['dataPath'] #路径和字符串
#         self.cache_path = params['cachePath']
#         self.start_date = params['startDate']
#         self.end_date = params['endDate']
#
#         super().__init__(self.cache_path)
#
#         self.di_list = []
#         self.ii_list = []
#         self.add_cache()
#
#     def add_cache(self):
#         self.register_serialization('di_list')
#         self.register_serialization('ii_list')
#
#     def register_context(self, context):
#         """
#         Register standard environment into context
#         :param context: sim_engine.context.Context
#         :return:
#         """
#         context.di_list = self.di_list
#         context.ii_list = self.ii_list
#
#     def compute_cache(self):
#         with open(os.path.join(self.data_path,'listing_date.csv')) as fp:
#             content = fp.read().splitlines()
#
#         for line in content[1:]:
#             items = line.replace('"', '').replace('-', '').split(',')
#             if items[2] == '1':
#                 self.di_list.append(items[1])
#
#         address = self.data_path + '\\raw_stock_daily_data'
#         files = os.listdir(address)
#
#         for file_ in files:
#             with open(address + '\\' + file_) as fp:
#                 content = fp.read().splitlines()
#             for line in content[1:]:
#                 items = line.replace('"', '').split(',')
#                 ticker = re.sub('\D', '', items[1])
#                 if ticker not in self.ii_list:
#                     self.ii_list.append(ticker)