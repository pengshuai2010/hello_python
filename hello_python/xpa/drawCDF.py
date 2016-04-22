import numpy as np
from matplotlib import pyplot as plt

from drawHistogram import get_data

if __name__ == '__main__':
    filename = 'itrust3_MCDCCoverage_multiFault_repair_timing.csv'
    data = get_data(filename)
    fig, ax = plt.subplots()
    for key in data.keys():
        l = data.get(key)
        l_sorted = np.sort(l)
        yvals = np.arange(len(l_sorted)) / float(len(l_sorted))
        ax.plot(l_sorted, yvals, label=key)
    ax.legend(shadow=True)
    plt.xlabel('milliseconds')
    plt.ylabel('probability')
    plt.title('empirical cumulative distribution')
    plt.show()
