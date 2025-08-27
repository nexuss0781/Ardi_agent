import time

class RateLimiter:
    def __init__(self, calls_per_minute: int):
        self.calls_per_minute = calls_per_minute
        self.interval = 60 / calls_per_minute
        self.last_call_time = 0

    def wait_for_next_call(self):
        current_time = time.time()
        elapsed_time = current_time - self.last_call_time

        if elapsed_time < self.interval:
            time_to_wait = self.interval - elapsed_time
            time.sleep(time_to_wait)

        self.last_call_time = time.time()


