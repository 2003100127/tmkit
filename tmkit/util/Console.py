__version__ = "v1.0"
__copyright__ = "Copyright 2022"
__license__ = "MIT"
__lab__ = "Adam Cribbs lab"

from datetime import datetime
from pyfiglet import Figlet


class console:

    def __init__(self, placeholder='logger: ', verbose=False):
        self._verbose = verbose
        self.placeholder = placeholder
        self.vignette1 = Figlet(font='standard')
        print(self.vignette1.renderText('TMKit'))

    @property
    def verbose(self, ):
        return self._verbose

    @verbose.setter
    def verbose(self, value):
        self._verbose = value

    def print(self, content):
        if self._verbose:
            now = datetime.now()
            dt_format = now.strftime("%d/%m/%Y %H:%M:%S ")
            print(dt_format + self.placeholder + str(content))

    def check(self, content):
        if self._verbose:
            print(content)