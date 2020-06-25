#!/usr/bin/python3
import asyncio

loop = asyncio.get_event_loop()


def handle_exception(loop, context):
    print("Inside handle_exception")


#loop.set_exception_handler(handle_exception)

# Async funtion will create a native coroutine
async def demo():

    # Future object can be used to 
    fut = loop.create_future()

    print("Inside demo")
    # import pdb
    # pdb.set_trace()

    def task1complete(fut1):
        loop.call_soon_threadsafe(fut.set_result, 3)

    async def task1():
        print("Inside task1")
        # time.sleep() is a blocking call,asyncio.sleep miimic a minimal non blocking IO operation
        # It means scheduler will go for sleep on current task but might schedule other tasks
        await asyncio.sleep(0)


    # Create task will accept only a coroutine as argument
    t1 = loop.create_task(task1())
    t1.add_done_callback(task1complete)
    res = await fut
    print("result :", res)


    # We cannot return future as it is,We need to await for the future
    return res


def task2complete(fut):
    print("Inside task 2 complete")
    rest = fut.result()
    print("rest :", rest)

async def task2():
    print("Inside task2")
    return 3

## Demontrates How to invoke a coroutine from a normal function
def get():
    print("Inside get")
    res = loop.run_until_complete(task2())
    print("res :", res)
    #t2.add_done_callback(task2complete)
    #asyncio.sleep(3)

async def sample():
    print("Inside sample")
    await asyncio.sleep(0)
    ret = None
    ret = await demo()
    print("retunred :", ret)
    return ret

async def hello():
    await asyncio.sleep(0)
    print("hello")


async def sample2():
    try:
        raise Exception("sample2 exception")
    except Exception as e:
        raise e

async def sample1():
    try:
        await sample2()
    except Exception as e:
        print("Exception :", e)


def main():
    print("Inside main")
    try:
        # loop.create_task(sample())
        # loop.run_until_complete(hello())
        # loop.run_until_complete(sample())

        # get()

        # print("Completed")

        loop.run_until_complete(sample1())

        
        # loop.close()
        #loop.run_forever()
    except Exception as e:
        print("Exception :", e)


if __name__ == '__main__':
    main()
