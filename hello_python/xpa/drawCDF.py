import numpy as np
from matplotlib import pyplot as plt

from drawHistogram import get_data

if __name__ == '__main__':
    policyname = 'itrust3'
    filename = policyname + '_MCDCCoverage_multiFault_repair_timing.csv'
    data = get_data(filename)
    fig, ax = plt.subplots()
    for key in data.keys():
        l = data.get(key)
        l_sorted = np.sort(l)
        yvals = np.arange(len(l_sorted)) / float(len(l_sorted))
        ax.plot(l_sorted, yvals, label=key)
    if policyname == 'itrust3':
        # itrust 3
        plt.annotate('{} milliseconds'.format(715), xy=(851, 0.04), textcoords='data')
        ax.axvline(715, color='b', linestyle='--')
        # set axis ticks
        x_major_ticks = np.arange(0, 12001, 1000)
        x_minor_ticks = np.arange(0, 12001, 500)
        ax.set_xticks(x_major_ticks)
        ax.set_xticks(x_minor_ticks, minor=True)
    elif policyname == 'conference3':
        # conference 3
        # ax.axvline(715, color='b', linestyle='--')
        # plt.annotate('{} milliseconds'.format(715), xy=(851, 0.04), textcoords='data')
        # set axis ticks
        x_major_ticks = np.arange(0, 501, 100)
        x_minor_ticks = np.arange(0, 501, 50)
        ax.set_xticks(x_major_ticks)
        ax.set_xticks(x_minor_ticks, minor=True)
    elif policyname == 'itrust3-5':
        # itrust 3-5
        plt.annotate('{} milliseconds'.format(12764), xy=(13000, 0.04), textcoords='data')
        ax.axvline(12764, color='b', linestyle='--')
        # set axis ticks
        x_major_ticks = np.arange(0, 500001, 100000)
        x_minor_ticks = np.arange(0, 500001, 50000)
        ax.set_xticks(x_major_ticks)
        ax.set_xticks(x_minor_ticks, minor=True)

    y_major_ticks = np.arange(0, 1.01, 0.1)
    y_minor_ticks = np.arange(0, 1.01, 0.05)
    ax.set_yticks(y_major_ticks)
    ax.set_yticks(y_minor_ticks, minor=True)

    ax.legend(shadow=True)
    plt.xlabel('milliseconds')
    plt.ylabel('ratio')
    plt.grid()
    # plt.title('empirical cumulative distribution')
    plt.savefig('/home/shuaipeng/Pictures/{}.png'.format(policyname))
    plt.show()