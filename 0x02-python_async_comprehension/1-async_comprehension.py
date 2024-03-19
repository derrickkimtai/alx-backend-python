#!/usr/bin/env python3
"""importance of documtation length should be longer
"""
import asyncio
import random
from typing import List


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Asynchronous function"""
    return [i async for i in async_generator()]
