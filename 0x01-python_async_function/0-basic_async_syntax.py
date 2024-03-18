#!/usr/bin/env python3
"""importance of documtation length should be longer
"""
import asyncio
import random


async def wait_random(max_delay: float = 10) -> float:
    """
    Asynchronous function
    Returns:float: The random number that was generated.
    """
    random_number = random.uniform(0, max_delay)
    await asyncio.sleep(random_number)
    return random_number
