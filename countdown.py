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
