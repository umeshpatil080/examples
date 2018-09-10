import os

class TestDB():
    def __init__(self):
        self._pid = os.getpid()

    def get_process_id(self):
        return self._pid