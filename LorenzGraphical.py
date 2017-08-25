import numpy as np
from scipy import integrate
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.colors import cnames
from matplotlib import animation

from ipywidgets import interact, interactive
from IPython.display import clear_output, display, HTML


def lorenz(n=10, angle=0.0, maxTime=4.0, sigma=1.0, beta=8 / 3, rho=28.0):
    fig = plt.figure();
    ax = fig.add_axes([0, 0, 1, 1, ], projection='3d')
    ax.axis('off')

    ax.set_xlim((-25, 25))
    ax.set_ylim((-35, 35))
    ax.set_zlim((5, 55))

    def lorenz_de(x_y_z, t0, sigma=sigma, beta=beta, rho=rho):
        x, y, z = x_y_z
        return [sigma * (y - x), x * (rho - z), x * y - beta * z]

    np.random.seed(2)
    x0 = -15 + 30 * np.random.random((n, 3))

    t = np.linspace(0, maxTime, int(250 * maxTime))
    x_t = np.asarray([integrate.odeint(lorenz_de, x0i, t) for x0i in x0])

    colors = plt.cm.jet(np.linspace(0, 1, n))

    for i in range(n):
        x, y, z = x_t[i, :, :].T
        lines = ax.plot(x, y, z, '-', c=colors[i])
        _ = plt.setp(lines, linewidth=2);

    ax.view_init(30, angle)
    _ = plt.show();

    return t, x_t


t, x_t = lorenz(angle=0, n=10)

o = interactive(lorenz, angle=(0., 360.), n=(0, 50), sigma=(0.0, 50.0), rho=(0.0, 50.0))
display(o)
