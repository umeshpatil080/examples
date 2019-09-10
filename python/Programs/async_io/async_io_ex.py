import asyncio

class Class1():
    def __init__(self):
        pass

    async def sam(self):
        print("Started Class1 sam\n")
        await asyncio.sleep(2)
        print("Completed Class1 sam\n")

class Class2():
    def __init__(self):
        pass

    async def sam(self):
        print("Started Class2 sam\n")
        await asyncio.sleep(1)
        print("Completed Class2 sam\n")

class BaseClass():
    def __init__(self):
        self._obj_list = []

    def register(self, obj):
        self._obj_list.append(obj)

    async def publish(self):
        loop = asyncio.get_event_loop()
        tasks = []
        for obj in self._obj_list:
            task = loop.create_task(obj.sam())
            tasks.append(task)

        print("Started tasks...")
        await asyncio.wait(tasks)
        print("Completed tasks")

    def publish1(self):
        for obj in self._obj_list:
            obj.sam()

def async_run():
    base = BaseClass()
    c1 = Class1()
    c2 = Class2()
    base.register(c1)
    base.register(c2)

    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.ensure_future(base.publish()))


if __name__ == "__main__":
    async_run()
