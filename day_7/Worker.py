NO_STEP = "."


def get_task_timer(step):
    base_time = 60
    uniq_time = ord(step) - 64

    return base_time + uniq_time


class Worker:
    def __init__(self, id):
        self.step = NO_STEP
        self.timer = 0
        self.id = id

    def assign_step(self, step):
        self.step = step
        self.timer = get_task_timer(step)
        # print("Worker {} starting task {} ({} seconds)".format(self.id, self.step, self.timer))

    def work(self):
        self.timer -= 1
        if self.timer == 0:
            finished_step = self.step
            self.step = NO_STEP
            # print("Worker {} finished task {}".format(self.id, finished_step))
            return finished_step
        return NO_STEP
