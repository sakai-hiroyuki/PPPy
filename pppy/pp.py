import os
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

from pppy.utils import name_decomposition


def performance_profile(path: str, stop: float=5., step: float=1e-2, tau: str=None, grid: bool=True) -> None:
    df = pd.read_csv(path)
    header = df.columns.values.tolist()

    line_info = []
    for name in header:
        line_info.append(name_decomposition(name))

    data = df.values
    num_p = data.shape[0]  # number of probems
    num_s = data.shape[1]  # number of solvers

    m = np.min(data, axis=1)
    r = data.T / m

    def _pp(tau: float, index: int) -> float:
        return np.count_nonzero(r[index] <= tau) / num_p
    
    pp = []
    for idx in range(num_s):
        _temp = []
        x = np.arange(1, stop, step)
        for val in x:
            _temp.append(_pp(val, idx))
        
        pp.append(_temp)
        plt.plot(x, _temp, **line_info[idx])
    
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

    return pp
