import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 20, .1)
y1 = np.cos(x)
y2 = np.tan(x)

fig, ax = plt.subplots(2)
# plot 1
ax[0].plot(x, y1, 'b,-')
plt.xlabel('x (units)')
ax[0].set(ylabel='y1 (units)')
ax[0].grid()
# plot 2
ax[1].plot(x, y2, 'g,-')
ax[1].set(ylabel='y2 (units)')
ax[1].grid()

# plt.waitforbuttonpress(0) # press any button to close plt
plt.show(block=False)