from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

from .ibstore import IBStore
from .ibbroker import IBBroker
from .ibdata import IBData
from .custom_logger import setup_custom_logger


# The modules below should/must define __all__ with the objects wishes
# or prepend an "_" (underscore) to private classes/variables

from .bbroker import BackBroker, BrokerBack

try:
    from .ibbroker import IBBroker
except ImportError:
    pass  # The user may not have ibpy installed

try:
    from .vcbroker import VCBroker
except ImportError:
    pass  # The user may not have something installed

try:
    from .oandabroker import OandaBroker
except ImportError as e:
    pass  # The user may not have something installed

__all__ = [
  'IBStore', 'IBBroker', 'IBData', 'setup_custom_logger',
]
__version__ = '0.1.0'

