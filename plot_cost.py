from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import pandas
import time
costs = pandas.read_csv("./costs.csv")

fig = plt.figure()
# first points

t = costs['time'].values
min_t = min(t)
t = [(x-min_t)*1e-9 for x in t]
uav4  = costs['uav4'].values
uav8  = costs['uav8'].values
uav11 = costs['uav11'].values
start = int(0.45*len(uav4))
finish =int(0.7*len(uav4))

ct = t[start:finish]
c4 = uav4[start:finish]
c8 = uav8[start:finish]
c11 = uav11[start:finish]
plt.title("Form formation mode, returning to found objects")
plt.xlabel("Time [sec]")
plt.ylabel("Cost function value [-]")
plt.plot(ct,c4,ct,c8,ct,c11)
plt.legend(['uav4','uav8','uav11'])
# plt.legend(loc="upper left")
plt.show()
