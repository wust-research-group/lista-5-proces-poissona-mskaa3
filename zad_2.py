import matplotlib.pyplot as plt
import numpy as np


def generate_compound_poisson_events(lam, time_duration):
    num_events = np.random.poisson(lam * time_duration)
    assert num_events > 0, "Number of events must be greater than 0"
    event_times = np.sort(np.random.uniform(0, time_duration, num_events))
    event_sizes = np.random.randint(1, 5, size=num_events)
    return num_events, event_times, event_sizes


rate, time_duration = 5, 5
num_events, event_times, event_sizes = generate_compound_poisson_events(5, 5)

# plt.step(event_times, np.cumsum(event_sizes), where='post', color='blue')
# plt.title(f'Compound Poisson Process Simulation (Duration = {time_duration} seconds)\n')
# plt.ylabel('N_t')
# plt.xlabel('Time')
# plt.grid(True)
# plt.show()
