#!/usr/bin/env python3
"""importance of documtation length should be longer
"""
import asyncio
import random
from typing import List


async def async_generator() -> List[float]:
    """Asynchronous function"""
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
