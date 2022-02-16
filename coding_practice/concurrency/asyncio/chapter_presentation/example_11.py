import asyncio


"""
ASYNCIO SUBPROCESSES
"""


async def run_subprocess(command: str) -> None:
    proc = await asyncio.create_subprocess_shell(
        cmd=command,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )
    print("Started process:", command)
    stdout, stderr = await proc.communicate()
    print(f"\n[{command!r} exited with {proc.returncode}]")
    if stdout:
        print(f"[stdout]: {stdout.decode()}")
    if stderr:
        print(f"[stderr]: {stderr.decode()}")


async def main() -> None:
    await asyncio.gather(
        run_subprocess('sleep 1; echo "hello"'),
        run_subprocess('sleep 2; echo "world"'),
        run_subprocess("gsutil ls gs://akl_core/testing/"),
        run_subprocess('docker images --filter "dangling=true"'),
        run_subprocess("makes no sense whatsoever"),
    )


if __name__ == "__main__":
    asyncio.run(main())
