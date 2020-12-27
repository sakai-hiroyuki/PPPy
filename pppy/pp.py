import os
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

from pppy.utils import header_decomposition


def performance_profile(path: str, stop: float=5., step: float=1e-2, tau: str=None, grid: bool=True) -> None:
    df = pd.read_csv(path)
    headers = df.columns.values.tolist()

    data = df.values
    Np = data.shape[0]  # number of probems
    Ns = data.shape[1]  # number of solvers

    m = np.min(data, axis=1)

    r = data.T / m

    def _pp(tau: float, solver: int) -> float:
        return np.count_nonzero(r[solver] <= tau) / Np

    for i in range(Ns):
        y = []
        x = np.arange(1, stop, step)
        for v in x:
            y.append(_pp(v, i))
        
        plt.plot(x, y, **header_decomposition(headers[i]))
    
    plt.xlim(1, stop)
    if tau is None:
        plt.xlabel(r'$\tau$')
    else:
        plt.xlabel(r'$\tau$' + f' ({tau})')
    plt.ylabel(r'$P_s(\tau)$')
    plt.legend(loc='lower right')
    if grid:
        plt.grid()

    plt.show()
