from parse import compile
from functools import reduce

from Worker import Worker, NO_STEP


def read_input():
    with open('input.txt') as f:
        return f.readlines()


def get_blocked_steps(graph):
    return {step for sublist in graph.values() for step in sublist}


def get_step_graph():
    raw_instructions = read_input()
    instruction_format = compile('Step {} must be finished before step {} can begin.\n')
    instructions = list(map(lambda instruction: instruction_format.parse(instruction), raw_instructions))
    # construct directed graph from instruction set
    graph = {}
    for instruction in instructions:
        node, dependant = instruction
        if node not in graph:
            graph[node] = []
        if dependant not in graph:
            graph[dependant] = []

        graph[node].append(dependant)

    return graph


def part1():
    graph = get_step_graph()

    incomplete_steps = graph.keys()
    steps = ""
    while len(incomplete_steps) > 0:
        incomplete_steps = graph.keys()
        blocked_steps = get_blocked_steps(graph)

        available_steps = list(incomplete_steps - blocked_steps)
        available_steps.sort()

        executing_step = available_steps[0]
        steps += executing_step
        del graph[executing_step]

    print("Took steps: {}".format(steps))


def print_progress(current_second, workers, done):
    worker_output = reduce((lambda acc, worker: acc + "{}         ".format(worker.step)), workers, "")
    print("   {}\t   {}\b\b\b{}".format(current_second, worker_output, done))


def part2():
    num_workers = 5

    worker_text = reduce((lambda acc, i: acc + "Worker {}  ".format(i + 1)), range(num_workers), "")
    print("Second\t{}Done".format(worker_text))

    workers = [Worker(i+1) for i in range(num_workers)]

    graph = get_step_graph()

    untouched_steps = graph.keys()
    steps = ""

    seconds_elapsed = 0
    while len(untouched_steps) > 0:
        # determine available steps
        untouched_steps = graph.keys()
        blocked_steps = get_blocked_steps(graph)
        working_steps = {worker.step for worker in workers if worker.step != NO_STEP}

        available_steps = list(untouched_steps - blocked_steps - working_steps)
        available_steps.sort()

        # find workers to assign tasks to
        for step in available_steps:
            can_assign_step = True
            for worker in workers:
                if can_assign_step and worker.step == NO_STEP:
                    worker.assign_step(step)
                    can_assign_step = False

        print_progress(seconds_elapsed, workers, steps)

        # carry out one second of execution
        for worker in workers:
            worker_finished = worker.work()
            if worker_finished != NO_STEP:
                steps += worker_finished
                del graph[worker_finished]

        seconds_elapsed += 1

    print_progress(seconds_elapsed, workers, steps)


if __name__ == '__main__':
    part1()
    part2()
