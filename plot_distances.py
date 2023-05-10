from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import pandas
import time
simulation = True
if simulation:
    distances = pandas.read_csv("./distances_simulation.csv")
else:
    distances = pandas.read_csv("./distances.csv")

fig = plt.figure()
# first points

t = distances['time'].values
min_t = min(t)
t = [(x-min_t)*1e-9 for x in t]
uav4  = distances['uav4'].values
uav8  = distances['uav8'].values
uav11 = distances['uav11'].values
plt.xlabel("Time [sec]")
plt.ylabel("Distance to the last observed centroid of objects [m]")
plt.plot(t,uav4,t,uav8,t,uav11)
plt.legend(['uav4','uav8','uav11'])
# plt.legend(loc="upper left")
plt.show()
