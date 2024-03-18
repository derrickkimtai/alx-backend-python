import asyncio

async def my_aysnc():
    print("This is the function before wait")
    await asyncio.sleep(5)
    print("Async after the sleep")


async def main():
    print("we are at the main function before calling the function")
    await my_aysnc()
    print("Back after calling the await function")

asyncio.run(main())