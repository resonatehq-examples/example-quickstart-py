from resonate import Resonate, Context
import time

resonate = Resonate.local()


def ntfy(_: Context, i: int):
    print(f"Countdown: {i}")


@resonate.register
def countdown(ctx: Context, count: int, delay: int):
    for i in range(count, 0, -1):
        # Run a function, persist its result
        yield ctx.run(ntfy, i=i)
        # Sleep
        yield ctx.sleep(delay)
    print("Done!")


def main():
    try:
        print("Starting countdown...")
        promise_id = f"countdown-{int(time.time() * 1000)}"  # Unique ID to avoid caching
        result = countdown.run(promise_id, count=3, delay=500)  # Count from 3 with 0.5s delay
        print("Countdown completed!")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
