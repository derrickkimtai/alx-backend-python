#!/usr/bin/env python3
"""importance of documtation length should be longer
"""
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Asynchronous function"""
    delays = [task_wait_random(max_delay) for i in range(n)]
    results = await asyncio.gather(*delays)
    return sorted(results)
