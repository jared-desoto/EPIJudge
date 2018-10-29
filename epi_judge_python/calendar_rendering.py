import collections
import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

# Event is a tuple (start_time, end_time)
Event = collections.namedtuple('Event', ('start', 'finish'))

Endpoint = collections.namedtuple('Endpoint', ('time', 'isStart'))

def find_max_simultaneous_events(A):
    endpoint_array = ([Endpoint(event.start, True) for event in A] +
                      [Endpoint(event.finish, False) for event in A])
    endpoint_array.sort(key=lambda x: (x.time, not x.isStart))

    counter, max_counter = 0, 0
    for endpoint in endpoint_array:
        if endpoint.isStart:
            counter += 1
            max_counter = max(max_counter, counter)
        else:
            counter -= 1

    return max_counter


@enable_executor_hook
def find_max_simultaneous_events_wrapper(executor, events):
    events = [Event(*x) for x in events]
    return executor.run(
        functools.partial(find_max_simultaneous_events, events))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("calendar_rendering.py",
                                       'calendar_rendering.tsv',
                                       find_max_simultaneous_events_wrapper))
