from parse import compile
from functools import reduce
from operator import itemgetter


def read_input():
    with open('input.txt') as f:
        return f.readlines()


guard_asleep = {
    '0': {
        0: 0,
        1: 0,
        # etc ... to 59
    }
}


def add_guard_asleep(guard_id, minute):
    if guard_id not in guard_asleep:
        guard_asleep[guard_id] = {}

    if minute in guard_asleep[guard_id]:
        guard_asleep[guard_id][minute] += 1
    else:
        guard_asleep[guard_id][minute] = 1


def total_minutes(guard_time_dict):
    total = reduce((lambda acc, val: acc + val), guard_time_dict.values())
    return total


def part1():
    records = read_input()
    records.sort()

    record_format = compile("[{}-{}-{} {}:{}] {}")
    action_format = compile("Guard #{} begins shift")

    # print(records)
    guard_on_shift = None
    guard_fell_asleep = None

    for record in records:
        year, month, day, hour, minute, action = record_format.parse(record)

        if action[0] == 'G':  # new guard begins shift
            # previous guard stayed awake until the end of their shift.
            # new guard is counted as "awake" before they begin shift

            guard_on_shift = action_format.parse(action)[0]
            guard_fell_asleep = None
            print("Guard {} begins shift at {}:{}".format(guard_on_shift, hour, minute))

        elif action == 'wakes up':  # current guard awaking from sleep
            # increment all minutes the guard was asleep for
            print("Guard {} wakes up at {}:{}".format(guard_on_shift, hour, minute))
            for i in range(int(guard_fell_asleep), int(minute)):
                print("  Guard {} was sleeping during minute {}".format(guard_on_shift, i))
                add_guard_asleep(guard_on_shift, i)

        elif action == 'falls asleep':  # current guard falling asleep
            print("Guard {} falls asleep at {}:{}".format(guard_on_shift, hour, minute))
            guard_fell_asleep = minute

    guard_total_asleep = {k: total_minutes(v) for k, v in guard_asleep.items()}
    print(guard_total_asleep)

    sleepiest_guard = max(guard_total_asleep, key=guard_total_asleep.get)

    print("Sleepiest guard is ID {} ({} minutes)".format(sleepiest_guard, guard_total_asleep[sleepiest_guard]))
    sleepy_guard_minutes = guard_asleep[sleepiest_guard]
    sleepiest_minute = max(sleepy_guard_minutes, key=sleepy_guard_minutes.get)

    print("Most often asleep at minute {}".format(sleepiest_minute))

    print("Product:", int(sleepiest_guard) * int(sleepiest_minute))

    part2()


def guard_sleepiest_minute(guard_time_dict):
    sleepiest_minute = max(guard_time_dict, key=guard_time_dict.get)
    sleep_count = guard_time_dict[sleepiest_minute]
    return (sleep_count, sleepiest_minute) # sleep_count first to make finding max sleep count easier later


def part2():
    sleepiest_guard_minute = {k: guard_sleepiest_minute(v) for k, v in guard_asleep.items()}

    sleepiest_id = max(sleepiest_guard_minute, key=sleepiest_guard_minute.get)
    sleepiest_stats = sleepiest_guard_minute[sleepiest_id]
    print("Guard {} spent minute {} asleep more than any other guard or minute - {} times in total"
          .format(sleepiest_id, sleepiest_stats[1], sleepiest_stats[0]))
    print("Product:", int(sleepiest_id) * int(sleepiest_stats[1]))


if __name__ == '__main__':
    part1()
