#!/usr/bin/env python3
"""async function module"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """waits for random number"""
    delay = random.uniform(0, max_delay)

    await asyncio.sleep(delay)

    return delay
