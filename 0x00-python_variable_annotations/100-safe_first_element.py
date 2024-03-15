#!/usr/bin/env python3
"""the shebang part"""
from typing import Sequence, Any, Union
"""impoerts the above packages and libraries"""


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """return any or none"""
    if lst:
        return lst[0]
    else:
        return None
