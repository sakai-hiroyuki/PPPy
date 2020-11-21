import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from argparse import ArgumentParser


def pp(tau: float, solver: int) -> float:
    return np.count_nonzero(r[solver] <= tau) / Np


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument('--path', type=str, default='sample.csv')
    parser.add_argument('--stop', type=float, default=5.)
    parser.add_argument('--step', type=float, default=1e-2)
    parser.add_argument('--ext', type=str, default='pdf')

    args = parser.parse_args()
    path = args.path
    stop = args.stop
    step = args.step
    ext = args.ext

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

    plt.legend()
    plt.savefig(f'result.{ext}')
