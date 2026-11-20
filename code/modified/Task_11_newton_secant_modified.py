from scipy.optimize import root_scalar


P = 50000.0
pmt = 1300.0
n = 48


def f(r):
    return P - pmt * (1 - (1 + r)**(-n)) / r


def df(r):
    return -pmt * (
        n * r * (1 + r)**(-n - 1) - (1 - (1 + r)**(-n))
    ) / r**2


newton = root_scalar(
    f,
    fprime=df,
    x0=0.01,
    method="newton",
    xtol=1e-12
)

secant = root_scalar(
    f,
    x0=0.005,
    x1=0.03,
    method="secant",
    xtol=1e-12
)

print(f"Monthly rate using Newton-Raphson: {newton.root:.6%}")
print(f"Monthly rate using Secant method: {secant.root:.6%}")
print(f"Annual nominal rate: {12*newton.root:.4%}")
print(f"Residual at Newton solution: {f(newton.root):.6e}")
