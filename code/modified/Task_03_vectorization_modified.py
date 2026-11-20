import numpy as np
import timeit

rng = np.random.default_rng(7)
voltage_mv = rng.uniform(-500, 500, 1_000_000)
resistance_ohm = 1000.0


def loop_version():
    power = []
    for value in voltage_mv:
        volts = value / 1000.0
        power.append(volts ** 2 / resistance_ohm)
    return power


def vectorized_version():
    volts = voltage_mv / 1000.0
    return volts ** 2 / resistance_ohm


loop_time = timeit.timeit(loop_version, number=1)
vector_time = timeit.timeit(vectorized_version, number=3) / 3

result = vectorized_version()

print("First five power values (W):", result[:5])
print(f"Mean power: {result.mean():.6e} W")
print(f"Loop time: {loop_time:.4f} s")
print(f"Vectorized time: {vector_time:.4f} s")
print(f"Approximate speed-up: {loop_time/vector_time:.1f}x")
