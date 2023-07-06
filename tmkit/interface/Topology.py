__author__ = "Jianfeng Sun"
__version__ = "v1.0"
__copyright__ = "Copyright 2023"
__license__ = "GPL v3.0"
__email__ = "jianfeng.sunmt@gmail.com"
__maintainer__ = "Jianfeng Sun"

from abc import ABCMeta, abstractmethod


class topology(metaclass=ABCMeta):

    @abstractmethod
    def run(self, *args):
        pass

    @abstractmethod
    def extract(self, arr_2d):
        pass