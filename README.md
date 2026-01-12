![quickstart banner](/assets/quickstart-banner.png)

# Quickstart | Resonate Python SDK

## The function you are about to activate

A countdown as a loop. Simple, but the function can run for minutes, hours, or days, despite restarts.

```python
from resonate import Resonate, Context
from threading import Event

def countdown(ctx: Context, count: int, delay: int):
    for i in range(count, 0, -1):
        # Run a function, persist its result
        yield ctx.run(ntfy, i)
        # Sleep
        yield ctx.sleep(delay)
    print("Done!")


def ntfy(_: Context, i: int):
    print(f"Countdown: {i}")


# Instantiate Resonate
resonate = Resonate.remote()
# Register the function
resonate.register(countdown)
resonate.start() # Start Resonate threads
Event().wait()  # Keep the main thread alive
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

- [Learn how Resonate works](/evaluate/how-it-works)
- [Explore examples](/get-started/examples)
- [Build a real application](/learn)
