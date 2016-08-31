import matplotlib.pyplot as plt

ax = plt.subplot(111)

threads = [1, 2, 4, 8, 16, 20, 24]
time = {"K1-N16-Inter": [11.9295, 6.4122, 3.1489, 1.697, 0.8873, 0.7202, 0.6016],
        "K7-N16-Inter": [10.1198, 5.1759, 2.6679, 1.4201, 0.7334, 0.5927, 0.5009],
        "K1-N128-Inter": [10.4002, 6.5947, 4.9964, 3.7421, 3.7764, 3.7123, 4.8355],
        "K19-N128-Inter": [10.7097, 5.5312, 2.8784, 1.615, 0.8483, 0.6911, 0.5846]}

# line, = plt.plot(threads, time["K1-N16-Inter"])
# plt.plot(threads, time["K1-N16-Inter"],
#                  threads, time["K7-N16-Inter"],
#                  threads, time["K1-N128-Inter"],
#                  threads, time["K19-N128-Inter"])
plt.figure(1)
for key in time.keys():
    plt.plot(threads, time[key], label=key)
plt.xlabel('threads')
plt.ylabel('seconds')
plt.grid(True)
plt.legend()
plt.title('execution time')

plt.figure(2)
for key in time.keys():
    plt.loglog(threads, time[key], label=key)
plt.xlabel('threads')
plt.ylabel('seconds')
plt.grid(True)
plt.legend()
plt.title('speedup')

plt.show()
