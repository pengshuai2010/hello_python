import matplotlib.pyplot as plt

ax = plt.subplot(111)

threads = [1, 2, 4, 8, 16, 32]
time = {"n=1000000000": [15.55, 7.82, 4.31, 2.21, 1.13, 0.6],
        "n=2000000000": [31.09, 15.57, 8.71, 4.34, 2.19, 1.16],
        "n=4000000000": [62.28, 31.11, 17.22, 8.62, 4.3, 2.23],
        "n=8000000000": [124.3, 62.18, 34.41, 17.12, 8.58, 4.49]}

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
plt.legend(bbox_to_anchor=(0.5, 0.8),
           bbox_transform=plt.gcf().transFigure)
plt.title('efficiency')

plt.show()
