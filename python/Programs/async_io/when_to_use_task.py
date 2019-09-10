import asyncio

async def long_running_operation():
    print("Started long_running_operation... ")
    await asyncio.sleep(2)
    print("Completed long_running_operation.")
    return "abc"

async def short_operation(msg):
    print("short_operation: " + msg)

async def main(wait_type=0):
    await short_operation("first")

    # Schedule task on event_loop.
    # task will be started when event_loop gets chance to examine
    # scheduled tasks to be run. This happens immediatedly after
    #  "await short_operation("second")"
    task = asyncio.ensure_future(long_running_operation())
    print("type of task:" + str(type(task)))
    if isinstance(task, asyncio.Task):
        print("Type of matching")
    else:
        print("Type not matching")
    await short_operation("second")

    # Wait for task to complete.
    # If await is not used then, main process will be completed
    # before event_loop wakes-up to finish the remaing task execuytion.

    if wait_type == 0:
        # First way to wait
        # Only one task can be waited
        res = await task
        print("wait_type: {0}\nresult: {1}".format(wait_type, res))
    elif wait_type == 1:
        # Second way to wait
        # Multiple tasks can be waited
        await asyncio.wait([task])
        res = task.result()
        print("wait_type: {0}\nresult: {1}".format(wait_type, res))
    else:
        # Third way to wait
        # Multiple tasks can be waited
        tasks = [task]
        task_group = asyncio.gather(*tasks)
        await task_group
        res = task.result()
        print("wait_type: {0}\nresult: {1}".format(wait_type, res))


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    #task = asyncio.ensure_future(main())
    task = loop.create_task(main(2))
    loop.run_until_complete(task)
