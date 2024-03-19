#!/usr/bin/env python3
"""importance of documtation length should be longer
"""
import asyncio
import random
from typing import AsyncGenerator, float


async def async_generator() -> AsyncGenerator[float, None]:
    """Asynchronous function"""
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
