from . import fetch
from . import cath
from . import edge
from . import seq
from . import qc
from . import feature
from . import mapping
from . import msa
from . import collate
from . import topo
from . import rrc
from . import ppi
from . import mut
from . import vs

__all__ = [
    "cath",
    "edge",
    "seq",
    "qc",
    "msa",
    "mapping",
    "collate",
    "feature",
    "topo",
    "rrc",
    "ppi",
    "mut",
    "vs",
]

# from typing import TYPE_CHECKING
# if TYPE_CHECKING:
#     from . import cath
# if TYPE_CHECKING:
#     from . import edge
# if TYPE_CHECKING:
#     from . import seq
# if TYPE_CHECKING:
#     from . import qc
# if TYPE_CHECKING:
#     from . import msa
# if TYPE_CHECKING:
#     from . import collate
# if TYPE_CHECKING:
#     from . import feature
# if TYPE_CHECKING:
#     from . import topo
# if TYPE_CHECKING:
#     from . import rrc
# if TYPE_CHECKING:
#     from . import ppi
# if TYPE_CHECKING:
#     from . import mut
# if TYPE_CHECKING:
#     from . import vs
# import importlib.util
# spam_spec = importlib.util.find_spec("vs")
# found = spam_spec is not None