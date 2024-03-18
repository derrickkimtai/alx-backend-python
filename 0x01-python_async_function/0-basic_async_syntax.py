#!/usr/bin/env python3
"""importance of documtation"""
import asyncio
import random
"""imports those modles they are needed"""


async def wait_random(max_delay: float = 10) -> float:
    """
    Asynchronous function

    Args:
        max_delay (float): The maximum delay in seconds (default is 10).

    Returns:
        float: The random number that was generated.

    """
    random_number = random.uniform(1, max_delay)
    await asyncio.sleep(random_number)
    return random_number
