import csv


def get_data(filename):
    # data = {'cbi':cbi, 'naish2':naish2, 'sokal': sokal, 'tarantula': tarantula, 'random': random}
    data = {'cbi': [], 'naish2': [], 'sokal': [], 'tarantula': [], 'random': []}
    with open(filename) as csvfile:
        reader = csv.reader(csvfile)
        next(reader, None)
        for row in reader:
            # cbi.append(float(row[1]))
            data.get('cbi').append(float(row[1]))
            # naish2.append(float(row[2]))
            data.get('naish2').append(float(row[2]))
            # sokal.append(float(row[3]))
            data.get('sokal').append(float(row[3]))
            # tarantula.append(float(row[4]))
            data.get('tarantula').append(float(row[4]))
            # random.append(float(row[5]))
            data.get('random').append(float(row[5]))
    return data


if __name__ == '__main__':
    filename = 'itrust3_MCDCCoverage_multiFault_repair_timing.csv'
    data = get_data(filename)
    import matplotlib.pyplot as plt

    # import plotly.plotly as py  # tools to communicate with Plotly's server
    # py.sign_in('pengshuai2010', 'dfp6n6u4t5')
    fig = plt.figure()

    plt.hist([data.get('cbi'), data.get('naish2'), data.get('sokal'), data.get('tarantula'), data.get('random')],
             bins=21,
             alpha=0.5, label=['cbi', 'naish2', 'sokal', 'tarantula', 'random'])
    # plt.hist([cbi, naish2, sokal, tarantula, random], bins=11, alpha=0.5, label=['cbi', 'naish2', 'sokal', 'tarantula', 'random'])
    # n, bins, patches = plt.hist([cbi])
    plt.title("distribution")
    plt.xlabel("milliseconds")
    plt.ylabel("frequency")
    plt.legend()
    plt.show()
    # plot_url = py.plot_mpl(fig, filename='docs/histogram-mpl-legend')
