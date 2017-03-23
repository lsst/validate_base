# See COPYRIGHT file at the top of the source tree.
"""Framework for measuring and defining performance metrics that can be
submitted to the SQUASH service.
"""

try:
    # version.py is auto-generated by sconsUtils
    from .version import *
except:
    __version__ = "unknown"

from .errors import *
from .datum import *
from .spec import *
from .metric import *
from .measurement import *
from .blob import *
from .job import *
from .output import *
