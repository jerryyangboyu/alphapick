import warnings
import urllib3
urllib3.disable_warnings(urllib3.exceptions.NotOpenSSLWarning)

import qlib
qlib.init(provider_uri='~/.qlib/qlib_data/cn_data')
