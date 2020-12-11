import os
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from argparse import ArgumentParser
from time import time
from math import floor


def pp(tau: float, solver: int) -> float:
    return np.count_nonzero(r[solver] <= tau) / Np


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument('--path', type=str, default='sample.csv')
    parser.add_argument('--stop', type=float, default=8.)
    parser.add_argument('--step', type=float, default=1e-2)
    parser.add_argument('--ext', type=str, default='pdf')
    parser.add_argument('--rd', type=str, default='.')
    parser.add_argument('--no_grid', action='store_false')

    args = parser.parse_args()
    path = args.path
    stop = args.stop
    step = args.step
    ext = args.ext
    result_dir = args.rd
    no_grid = args.no_grid

    df = pd.read_csv(path)
    solvers = df.columns.values.tolist()

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
        plt.plot(x, y, label=solvers[i])
    
    plt.xlim(1, stop)
    plt.legend()
    if not no_grid:
        plt.no_grid()

    plt.show()

    '''
    ut = floor(time())
    plt.savefig(os.path.join(result_dir, f'result{ut}.{ext}'))
    '''
