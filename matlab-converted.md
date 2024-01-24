# Matlab code converted to python

Auto-converted:

```
import numpy as np
import matplotlib.pyplot as plt

# What are inputs?
# A: data
# FY: first year?
# LY: last year? 
# g: 0-4 ?
# s: ?
# REFP: reference period: 1971-2001

def plotshowstripes_forpoppy(A, FY, g, s, REFP):

    LY = len(A)
    plt.close('all')
    SN = 2.6

    if not 'g' in locals():
        g = 0

    if 's' in locals():
        SN = s

    if g == 2:
        pass
        # refperiod = 1951:2000

    if g == 4:
        refperiod = np.arange(1971, 2001)
    if not 'REFP' in locals():
        refperiod = np.arange(1971, 2001)
    else:
        refperiod = REFP

    CM = plt.cm.get_cmap('bwr')
    CM = CM(np.arange(CM.N))
    CM = np.delete(CM, 8, axis=0)
    CM = np.vstack(([0.5, 0.5, 0.5], CM))

    sz = np.shape(A)
    A = A - np.mean(A[refperiod])
    CMAX = SN * np.nanstd(A[1900:2000])

    plt.close('all')
    fig = plt.figure()
    ax = fig.add_axes([0, 0, 1, 1])

    if g == 1:
        ax.set_ylim([-0.75 * 9 / 8, 0.75])
    elif g == 2:
        ax.set_ylim([-0.65 * 9 / 8, 0.65])
    elif g == 5:
        ax.set_ylim([-1.3 * 9 / 8, 1.3])
    else:
        ax.set_ylim([-CMAX * 9 / 8, CMAX])

    cl = ax.get_ylim()

    A[A <= -cl[1]] = -cl[1] + 0.001
    ax.imshow(A[FY:LY], cmap=CM)

    ax.set_ylim(cl)
    ax.axis('off')

    ax.set_xticks([])
    ax.set_yticks([])
    plt.show()

```

