from sympy import Point, Line, pi, symbols, plot
from sympy.plotting import plot3d, plot3d_parametric_surface
import matplotlib.pyplot as plt 
import numpy as np
from mpl_toolkits import mplot3d


p1, p2 = Point(0,0), Point(1,1)
l = Line(p1,p2)
t = symbols('t')
plot(3+5*t, (t, -5, 5))



x, y = symbols('x y')
plot3d(3+5*x, (x, -5, 5), (y, -5, 5))



z = symbols('x y z')
plot3d(x**2+y**2, (x, -5, 5), (y, -5, 5))


xx, yy = np.meshgrid(range(10), range(10))

z = 0*xx + 0*yy + 475

plt3d = plt.figure().gca(projection='3d')
plt3d.plot_surface(xx, yy, z, alpha=0.2)
ar1, ar2, ar3 = t_df['x_kb'], t_df['y_kb'], t_df['z_kb']
#plt3d.plot(ar1, ar2, ar3)

# Ensure that the next plot doesn't overwrite the first plot
ax = plt.gca()