#!/usr/bin/env python3
"""importance of documtation length should be longer
"""
import asyncio
import time
aync_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Asynchronous function"""
    start = time.time()
    await aync_comprehension()
    end = time.time()
    return end - start
