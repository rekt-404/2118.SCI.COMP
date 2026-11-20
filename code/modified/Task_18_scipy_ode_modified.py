import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt


N = 1000.0
beta = 0.3    
gamma = 0.1    
S0, I0, R0 = 999.0, 1.0, 0.0


def sir(t, y):
    S, I, R = y
    return [
        -beta * S * I / N,
        beta * S * I / N - gamma * I,
        gamma * I
    ]


t_eval = np.linspace(0, 160, 400)

solution = solve_ivp(
    sir,
    (0, 160),
    [S0, I0, R0],
    t_eval=t_eval,
    rtol=1e-8,
    atol=1e-10
)

S, I, R = solution.y
peak_index = np.argmax(I)

print("Solver success:", solution.success)
print(f"Peak infected: {I[peak_index]:.1f} people")
print(f"Day of peak: {solution.t[peak_index]:.1f}")
print(f"Total recovered at day 160: {R[-1]:.1f}")
print(f"Population check (S+I+R): {S[-1] + I[-1] + R[-1]:.2f}")

plt.plot(solution.t, S, label="Susceptible")
plt.plot(solution.t, I, label="Infected")
plt.plot(solution.t, R, label="Recovered")
plt.xlabel("Time (days)")
plt.ylabel("People")
plt.title("SIR epidemic model")
plt.legend()
plt.grid(True)
plt.show()
