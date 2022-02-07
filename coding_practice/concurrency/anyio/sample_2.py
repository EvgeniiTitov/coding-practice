import anyio


async def i_sleep_long() -> None:
    print("Sleepy head called")
    await anyio.sleep(3600)


async def i_sleep_long_and_i_care() -> None:
    print("Polite sleepy head called")
    try:
        await anyio.sleep(3600)
    except anyio.get_cancelled_exc_class():  # trio and asyncio use diff exc
        print("Polite sleepy head cancelled, terminating...")


async def main() -> None:
    with anyio.move_on_after(2.0) as scope:
        await i_sleep_long()
    print("Cancel scope left. Cancelled:", scope.cancel_called)

    print()
    try:
        with anyio.fail_after(2.0) as scope:
            await i_sleep_long_and_i_care()
    except BaseException as e:
        print(f"Exception {e} caught. Cancelled:", scope.cancel_called)


if __name__ == "__main__":
    anyio.run(main)
