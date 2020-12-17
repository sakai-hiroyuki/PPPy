import os
import re
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from argparse import ArgumentParser
from math import floor

from utils import header_decomposition


def pp(tau: float, solver: int) -> float:
    return np.count_nonzero(r[solver] <= tau) / Np


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument('--path', type=str)
    parser.add_argument('--stop', type=float, default=8.)
    parser.add_argument('--step', type=float, default=1e-2)
    parser.add_argument('--tau', type=str, default=None)
    parser.add_argument('--no_grid', action='store_false')

    args = parser.parse_args()
    path = args.path
    stop = args.stop
    step = args.step
    tau = args.tau
    no_grid = args.no_grid

    df = pd.read_csv(path)
    headers = df.columns.values.tolist()

    data = df.values
    Np = data.shape[0]  # number of probems
    Ns = data.shape[1]  # number of solvers

    m = np.min(data, axis=1)

    r = data.T / m

    for i in range(Ns):
        y = []
        x = np.arange(1, stop, step)
        for v in x:
            y.append(pp(v, i))
        
        plt.plot(x, y, **header_decomposition(headers[i]))
    
    plt.xlim(1, stop)
    if tau is None:
        plt.xlabel(r'$\tau$')
    else:
        plt.xlabel(r'$\tau$' + f' ({tau})')
    plt.ylabel(r'$P_s(\tau)$')
    plt.legend(loc='lower right')
    if no_grid:
        plt.grid()

    plt.show()
