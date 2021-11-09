import os
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

from pppy.utils import header_decomposition


def performance_profile(path: str, stop: float=5., step: float=1e-2, tau: str=None, grid: bool=True) -> None:
    df = pd.read_csv(path)
    header = df.columns.values.tolist()
    data = df.values
    if np.min(data) <= 0.:
        raise ValueError('All values ​​in the data must be positive.')
    num_p, num_s = data.shape
    r = data.T / np.min(data, axis=1)

    info = header_decomposition(header)

    def _pp(tau: float, index: int) -> float:
        return np.count_nonzero(r[index] <= tau) / num_p
    
    pp = []
    for idx in range(num_s):
        _temp = []
        x = np.arange(1, stop, step)
        for val in x:
            _temp.append(_pp(val, idx))
        pp.append(_temp)
    
    _pp_plot(pp, info, stop, step, tau, grid)


def _pp_plot(pp, info, stop, step, tau, grid):
    x = np.arange(1, stop, step)
    for idx, y in enumerate(pp):
        plt.plot(x, y, **info[idx])
    
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
