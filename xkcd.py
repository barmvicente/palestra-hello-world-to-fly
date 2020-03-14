
import matplotlib.pyplot as plt
import numpy as np


with plt.xkcd():

    fig = plt.figure()
    ax = fig.add_axes((0.1, 0.2, 0.8, 0.7))
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_ylim([-50, 10])

    data = np.ones(100)
    data[50:] += 0.25*np.arange(50)

    ax.annotate(
        'O DIA QUE EU\nCONHECI O PYLADIES <3',
        xy=(50, 1), arrowprops=dict(arrowstyle='->'), xytext=(15, -10))

    ax.plot(data)

    ax.set_xlabel('tempo')
    ax.set_ylabel('meu amor por Python')
    fig.text(
        0.5, 0.05,
        '"Pyladies" me acolheu <3',
        ha='center')

plt.show()
