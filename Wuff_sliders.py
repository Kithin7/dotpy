# wulff construction fun
# Feb 2021

# make polar plot of surface free enegery
# find intersection with lines from the origin
# draw a  line at interestion perpendicular to the line from the origin
# look at *pretty* inner most shape
# input equation (manually)

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button


# Step/qualty = feeds theta and determines the number of blue lines drawn
# Coef = coefficient for wulff eqn
# gamma = wulff eqn
# theta = array for 0-360 degrees, used to calc gamma
# x, y = cartesian form for plotting the polar curve red "Line"
# pX, pY = cartesian perpendicular lines, used to draw blue "pLine"


def Gamma(Coef, theta):
    return abs(np.cos(Coef * theta)) + abs(np.sin(Coef * theta))


def polar2cart(Coef, theta):
    return Gamma(Coef, theta) * np.cos(theta), Gamma(Coef, theta) * np.sin(theta)


def Wulff_(x, y, theta):
    # add perpendicular lines (dot) intersections
    # for loop to do each
    pLineX = np.arange(2*min(x), 2*max(x), max(x)/5)
    pLineY = []
    for k in range(0, len(theta)):
        if y[k] == 0 or x[k] == 0:  # need to handle 0,inf case
            continue  # if slope = 0 or inf then skip loop iteration
        else:
            slope = (y[k]) / (x[k])
            pslope = -1/slope
            pLineY.append(pslope*(pLineX-(x[k]))+(y[k]))
    return pLineX, pLineY


def replot(line, pline, Coef, Step):
    theta = np.arange(0, 360 + Step, Step) * np.pi / 180
    x, y = polar2cart(Coef, theta)
    px, py = Wulff_(x, y, theta)
    # plotting
    for i in range(len(theta)):
        ax.pline.pop(0)
        pline.plot(px, py[i])
    line.plot(x, y)


def update_coef(fig, line, pline, new_coef, step):
    replot(line, pline, new_coef, step)
    fig.canvas.draw_idle()


def update_step(fig, line, pline, coef, new_step):
    replot(line, pline, coef, new_step)
    fig.canvas.draw_idle()


def reset(event):
    Step.reset()
    Coef.reset()


if __name__ == "__main__":
    fig, ax = plt.subplots()
    xax = fig.add_axes([0.3, 0, 0.5, 0.05])
    Step = Slider(
        ax=xax,
        label="Step",
        valmin=1,
        valmax=10,
        valinit=3,
        valstep=.5)
    # 12-sides, coef = 3
    # cubic, coef = 1
    # hexagonal, coef = 1.5
    # roughly /4 = # sides??
    yax = fig.add_axes([0.01, 0.3, 0.05, 0.5])
    Coef = Slider(
        ax=yax,
        label="Coef.",
        valmin=1,
        valmax=10,
        valinit=1.5,
        valstep=0.1,
        orientation="vertical")

    theta = np.arange(0, 360 + Step.valinit, Step.valinit) * np.pi / 180
    x, y = polar2cart(Coef.valinit, theta)
    ax.set_xlim(1.2 * min(x), 1.2 * max(x))
    ax.set_ylim(1.2 * min(y), 1.2 * max(y))
    px, py = Wulff_(x, y, theta)

    center, = ax.plot(0, 0, 'g.')
    line, = ax.plot(x, y, 'r', lw=4)
    for i in range(len(py)):
        pline, = ax.plot(px, py[i], 'b', lw=2)

    Coef.on_changed(lambda coef: update_coef(fig, line, pline, coef, Step.val))
    Step.on_changed(lambda step: update_step(fig, line, pline, Coef.val, step))

    resetax = fig.add_axes([.02, .02, 0.08, 0.04])
    button = Button(resetax, 'reset', hovercolor="0.975")
    button.on_clicked(reset)

    plt.show()
