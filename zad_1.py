import matplotlib.pyplot as plt
import numpy as np


def generate_poisson_events(lam, time_duration):
    num_events = np.random.poisson(lam * time_duration)
    assert num_events > 0, "Number of events must be greater than 0"
    event_times = np.sort(np.random.uniform(0, time_duration, num_events))
    return num_events, event_times


def get_N(event_times, t):
    N_t = 0
    for time in event_times:
        if time <= t:
            N_t += 1
        else:
            break
    return N_t


rate, time_duration = 5, 5
num_events, event_times = generate_poisson_events(5, 5)
# plt.step(event_times, np.arange(1, num_events + 1), where='post', color='blue')
# plt.title(f'Poisson Process Simulation (λ = {rate}, Duration = {time_duration} seconds)\n')
# plt.ylabel('N_t')
# plt.xlabel('Time')

num_time_points = 100
time_space = np.linspace(0, time_duration, num_time_points)
result = [get_N(event_times, t) for t in time_space]
# plt.hist(result, bins=50)
# plt.title(f'Distribution of N_t value')
# plt.ylabel('Count')
# plt.xlabel('N_t')
