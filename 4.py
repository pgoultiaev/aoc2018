from util import readinput, vector
from datetime import datetime


def sort_by_date(data):
    d = [l.rstrip('\n') for l in data]
    d.sort(key=lambda x: datetime.strptime(x[1:17], "%Y-%m-%d %H:%M"))
    return d


def calculate_sleep(data):
    all_guards = {}
    start_sleep, end_sleep, current_guard_id = 0, 0, 0

    for line in data:
        v = vector(line, sep=' ')

        if v[2] == 'Guard':
            current_guard_id = v[3].lstrip('#')
            if current_guard_id not in all_guards:
                all_guards[current_guard_id] = [0 for t in range(60)]
        elif v[2] == 'falls':
            start_sleep = int(vector(v[1], sep=':')[1].rstrip(']'))
        else:
            end_sleep = int(vector(v[1], sep=':')[1].rstrip(']'))
            for t in range(start_sleep, end_sleep):
                all_guards[current_guard_id][t] += 1

    return all_guards


def solve(all_guards, function):
    sleep_reindex = {function(s): g for g, s in all_guards.items()}
    guard = sleep_reindex[max(sleep_reindex.keys())]
    minute = all_guards[guard].index(max(all_guards[guard]))

    return int(guard) * minute


all_guards = calculate_sleep(sort_by_date(readinput('4')))
print(solve(all_guards, sum))
print(solve(all_guards, max))
