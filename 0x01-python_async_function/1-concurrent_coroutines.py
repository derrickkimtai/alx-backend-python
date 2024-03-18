#!/usr/bin/env python3
"""importance of documtation length should be longer
"""
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Asynchronous function"""
    delays = [wait_random(max_delay) for i in range(n)]
    results = await asyncio.gather(*delays)
    return sorted(results)
