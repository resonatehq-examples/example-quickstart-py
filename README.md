<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="./assets/banner-dark.png">
    <source media="(prefers-color-scheme: light)" srcset="./assets/banner-light.png">
    <img alt="Quickstart — Resonate example" src="./assets/banner-dark.png">
  </picture>
</p>

<p align="center">
  <a href="https://resonatehq.github.io/examples-ci/">
    <img src="https://img.shields.io/endpoint?url=https://resonatehq.github.io/examples-ci/status/example-quickstart-py.json" alt="examples-ci status">
  </a>
</p>

# Quickstart | Resonate Python SDK

## The function you are about to activate

A countdown as a loop. Simple, but the function can run for minutes, hours, or days, despite restarts.

```python
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
```

## Steps to run

### 1. Install the Resonate Server & CLI

```shell
brew install resonatehq/tap/resonate
```

### 2. Install the Resonate SDK

```shell
pip install resonate-sdk
```

### 3. Start the server

```shell
resonate dev
```

### 4. Start the worker

```shell
python countdown.py
```

### 5. Activate the function

Activate the function with execution ID `countdown.1`:

```shell
resonate invoke countdown.1 --func countdown --arg 5 --arg 60
```

### Result

You will see the countdown in the terminal

```shell
python countdown.py
Countdown: 5
Countdown: 4
Countdown: 3
Countdown: 2
Countdown: 1
Done!
```

### What to try

After starting the function, inspect the current state of the execution using the `resonate tree` command. The tree command visualizes the call graph of the function execution as a graph of durable promises.

```shell
resonate tree countdown.1
```

Now try killing the worker mid-countdown and restarting. **The countdown picks up right where it left off without missing a beat.**

## Next steps

- [Learn how Resonate works](https://docs.resonatehq.io/evaluate/how-it-works)
- [Explore examples](https://docs.resonatehq.io/get-started/examples)
- [Build a real application](https://docs.resonatehq.io/learn)
