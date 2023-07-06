__author__ = "Jianfeng Sun"
__version__ = "v1.0"
__copyright__ = "Copyright 2023"
__license__ = "GPL v3.0"
__email__ = "jianfeng.sunmt@gmail.com"
__maintainer__ = "Jianfeng Sun"

from abc import ABCMeta, abstractmethod


class Tool(metaclass=ABCMeta):
    """
    Abstract base class for all tools.

    Attributes
    ----------
    None

    Methods
    -------
    initializer()
        Abstract method to initialize the tool.
    execute()
        Abstract method to execute the tool.
    """

    @abstractmethod
    def initializer(self) -> None:
        """
        Abstract method to initialize the tool.

        Parameters
        ----------
        None

        Returns
        -------
        None
        """
        pass

    @abstractmethod
    def execute(self) -> None:
        """
        Abstract method to execute the tool.

        Parameters
        ----------
        None

        Returns
        -------
        None
        """
        pass
