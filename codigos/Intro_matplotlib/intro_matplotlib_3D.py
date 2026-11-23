

import matplotlib
import matplotlib.pyplot as plt
import numpy as np

import matplotlib.pyplot as plt
import numpy as np

#dibujamos un muelle en 3D
x=np.linspace(0,2,100)
y=np.sin(2*np.pi*x)
z=np.cos(2*np.pi*x)
fig,ax=plt.subplots(subplot_kw={"projection": "3d"})
ax.scatter(x,y,z)
plt.show()

#dibujamos reticula en 3D
x = np.arange(0,4)
y = np.arange(0,4)
Xm, Ym = np.meshgrid(x, y)
Zm = np.zeros((4, 4))
fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
ax.plot_wireframe(Xm, Ym, Zm)
plt.show()
#dibujamos una superficie en 3D
x=np.linspace(-1.5,1.5,25)
y=np.linspace(-2,2,50)
[Xm,Ym]=np.meshgrid(x,y)
Zm = Xm**3+Ym**2
fig, ax = plt.subplots(1,2,subplot_kw={"projection": "3d"})
ax[0].plot_wireframe(Xm, Ym, Zm)
ax[1].plot_surface(Xm, Ym, Zm)
plt.show()