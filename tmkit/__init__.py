import sys
from importlib import metadata as importlib_metadata

from . import (
    cath,
    collate,
    edge,
    feature,
    fetch,
    mapping,
    msa,
    mut,
    ppi,
    qc,
    rrc,
    seq,
    topo,
    vs,
)

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


def get_version() -> str:
    try:
        return importlib_metadata.version(__name__)
    except importlib_metadata.PackageNotFoundError:  # pragma: no cover
        return "unknown"


version: str = get_version()
