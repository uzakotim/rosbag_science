from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import pandas

simulation = True
if simulation:
    points = pandas.read_csv("./simulation_results_uav4/main.bag_slow_odom_uav4.csv")
else:
    points = pandas.read_csv("./main_results_uav4/main.bag_slow_odom_uav4.csv")

fig = plt.figure()
ax = fig.add_subplot(111,projection='3d')

x = points['x'].values[-100:-1]
y = points['y'].values[-100:-1]
z = points['z'].values[-100:-1]

ax.scatter(x,y,z,c='r',marker ='o')
plt.show()
