from __future__ import annotations

import asyncio
import os
from typing import TYPE_CHECKING

from resonate.resonate import Resonate

if TYPE_CHECKING:
    from resonate.context import Context


async def countdown(ctx: Context, count: int, delay: int) -> None:
    for i in range(count, 0, -1):
        # Run a function, persist its result
        await ctx.run(ntfy, i)
        # Sleep
        await ctx.sleep(delay)
    print("Done!")


async def ntfy(_: Context, i: int) -> None:
    print(f"Countdown: {i}")


async def main() -> None:
    r = Resonate(url=os.environ.get("RESONATE_URL", "http://localhost:8001"))
    r.register(countdown)
    r.register(ntfy)
    await asyncio.Event().wait()


if __name__ == "__main__":
    asyncio.run(main())
