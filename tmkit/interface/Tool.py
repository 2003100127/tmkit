__author__ = "Jianfeng Sun"
__version__ = "v1.0"
__copyright__ = "Copyright 2023"
__license__ = "GPL v3.0"
__email__ = "jianfeng.sunmt@gmail.com"
__maintainer__ = "Jianfeng Sun"

from abc import ABCMeta, abstractmethod


class tool(metaclass=ABCMeta):

    @abstractmethod
    def initializer(self):
        pass

    @abstractmethod
    def execute(self):
        pass