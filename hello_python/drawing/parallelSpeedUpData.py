import matplotlib.pyplot as plt

ax = plt.subplot(111)

threads = [1, 2, 4, 8, 16, 32]
time = {"n=1000000000": [16.79,  8.44, 4.26, 2.18, 1.11, 0.6],
        "n=2000000000": [33.58, 16.88, 8.5, 4.28, 2.18, 1.14],
        "n=4000000000": [66.96, 33.71, 16.95, 8.46, 4.29, 2.27],
        "n=8000000000": [134.26, 67.48, 33.97, 16.99, 8.58, 4.42]}

plt.figure(1)
for key in time.keys():
    plt.loglog(threads, time[key], label=key)
plt.xlabel('processes')
plt.ylabel('seconds')
plt.grid(True)
plt.legend()
plt.title('execution time')

plt.figure(2)
for key in time.keys():
    plt.plot(threads, [time[key][0] / t for t in time[key]], label=key)
plt.xlabel('processes')
plt.ylabel('speedup')
plt.grid(True)
plt.legend(bbox_to_anchor=(0.5, 0.8),
           bbox_transform=plt.gcf().transFigure)
plt.title('speedup')

plt.figure(3)
for key in time.keys():
    plt.plot(threads, [time[key][0] / (time[key][i] * threads[i]) for i in range(len(time[key]))], label=key)
plt.xlabel('processes')
plt.ylabel('efficiency')
plt.grid(True)
plt.legend(bbox_to_anchor=(0.5, 0.5),
           bbox_transform=plt.gcf().transFigure)
plt.title('efficiency')
for key in time.keys():
    a = [time[key][0] / t for t in time[key]]
    print ["{0:0.2f}".format(i) for i in a]

plt.show()
