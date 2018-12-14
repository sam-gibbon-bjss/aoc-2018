from parse import compile


def read_input():
    with open('input.txt') as f:
        return f.readlines()


def get_blocked_steps(graph):
    return {step for sublist in graph.values() for step in sublist}


def part1():
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

    print(graph)

    incomplete_steps = graph.keys()
    steps = ""
    while len(incomplete_steps) > 0:
        incomplete_steps = graph.keys()
        blocked_steps = get_blocked_steps(graph)

        available_steps = list(incomplete_steps - blocked_steps)
        available_steps.sort()
        print("Available steps: {}".format(available_steps))

        executing_step = available_steps[0]
        print("\tExecuting step {}".format(executing_step))
        steps += executing_step
        del graph[executing_step]

    print("Took steps: {}".format(steps))


if __name__ == '__main__':
    part1()
